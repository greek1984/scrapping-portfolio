import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class OzoneParser:
    """Парсер для маркетплэйса Ozon с локацией Казахстан. Выполняет сбор данных по заданному поисковому запросу
       с выборкой 3-х элементов для найденных карточек: названия, "чистой" цены и ссылки. Затем сохраняет данные
       в файл .xlsx"""
    def __init__(self, search_query):
        self.search_query = search_query
        self.driver = None
        self.results = []

    def setup_driver(self):
        """Настраивает драйвер для парсера, подключая необходимые опции"""
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--start-maximized")
        self.driver = uc.Chrome(
            # version_main=141,
            options=chrome_options)

    def run_search(self):
        """Запуск поиска данных на странице с ожиданием загрузки.
        Поиск элементов страницы с вводом запроса и кликом на кнопку"""
        self.driver.get("https://www.ozon.kz/")
        # Драйвер ожидает 20 секунд до загрузки >>>
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )

        print(f"Начинаю поиск по запросу: {self.search_query}")

        search_input = self.driver.find_element(By.NAME, "text")
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Поиск']")
        search_input.send_keys(self.search_query)
        search_button.click()

    def _clean_price(self, raw_price_text):
        """Очищает 'грязную' строку с ценой от 'мусора' (валюта, пробелы).
            Корректно обрабатывает цены с рассрочкой (вида '10000 ₸ × 6 мес').
            Args:
                raw_price_text (str): 'Грязная' строка цены (e.g., "26 339 ₸ × 6 мес").

            Returns:
                str: 'Чистая' цена в виде строки (e.g., "158034")."""

        # "Убираем весь "мусор" (тонкие пробелы, валюту)
        price = raw_price_text.replace("₸", "").replace(" ", "").replace("\u2009", "")
        # Проверяем, "это" "рассрочка" или нет?
        if "×" in price:
            parts = price.split("×") # Это "рассрочка". Разбиваем ее:
            part_price = int(parts[0])
            part_months = int(parts[1].strip("мес"))  # Убираем "мес"
            # Возвращаем полную стоимость
            return str(part_price * part_months)  # Возвращаем строку, а не число
        else:
            # Это обычная цена. Просто возвращаем ее
            return price

    def scrape_results(self):
        """Метод сбора данных по указанным якорям. Сначала происходит поиск карточек на странице,
        а затем в каждой картотчке находится название, цена и ссылка. Внутри для 'очистки' цены
        применяется вспомогательный метод, чтобы передать затем 'чистую' цену в словарь"""
        card_anchor = "div.tile-root"
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, card_anchor))
        )
        print("Сетка товаров прогрузилась. Начинаю сбор...")

        cards = self.driver.find_elements(By.CSS_SELECTOR, card_anchor)
        print(f"Найдено {len(cards)} карточек на странице.")

        for card in cards:
            try:
                link = card.find_element(By.CSS_SELECTOR, "a.tile-clickable-element").get_attribute("href")
                title = card.find_element(By.CSS_SELECTOR, "span.tsBody500Medium").text

                # Получаем "грязную" цену(рассрочка и прочее)
                raw_price = card.find_element(By.CSS_SELECTOR, "span.tsHeadline500Medium").text

                # Вызываем метод для очистки цены
                clean_price = self._clean_price(raw_price)
                # При условии извлечения всех 3-х запрашиваемых элементов
                if title and clean_price and link:
                    print(f"[УСПЕХ] {title} | {clean_price} ₸ | {link[:30]}...")  # Печатаем "чистую цену"

                    # Добавление "чистой цены"
                    self.results.append({"title": title, "price": clean_price, "link": link})
                else:
                    print(f"[ПРОПУСК] Карточка пуста.")

            except Exception as e:
                print(f"[ПРОПУСК] Карточка пропущена.")

    def close_driver(self):
        """Подведение итогов по сбору, распечатка статистики по найденному, закрытие браузера"""
        print(f"Сбор завершен. Собрано {len(self.results)} товаров.")
        print("Закрываю браузер...")
        self.driver.quit()

    def run_process(self):
        """Главный метод-оркестратор.
        Запускает все этапы парсинга (setup, search, scrape) в блоке try...finally
        для гарантированного закрытия драйвера."""
        try:
            self.setup_driver()
            self.run_search()
            self.scrape_results()
        finally:
            self.close_driver()

    def save_to_xlsx(self, xlsx_path):
        """Сохранение найденных после парсинга табличных данных в формат .xlsx(для Excel)"""
        df = pd.DataFrame(self.results)
        try:
            with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Ozon Results', index=False)
                worksheet = writer.sheets['Ozon Results']
                worksheet.column_dimensions['A'].width = 90
                worksheet.column_dimensions['B'].width = 15
                worksheet.column_dimensions['C'].width = 75
        # Если запущен Excel и открыт ранее созданный скриптом файл
        except PermissionError:
            print(f"\n[ОШИБКА СОХРАНЕНИЯ] Не удалось сохранить файл: {xlsx_path}")
            print("--- Убедись, что у тебя есть права на запись и файл не открыт в Excel! ---")
        except Exception as e:
            # Например, диск переполнен
            print(f"\n[ОШИБКА СОХРАНЕНИЯ] Произошла неизвестная ошибка: {e}")
