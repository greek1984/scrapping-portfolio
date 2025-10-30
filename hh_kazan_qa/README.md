# 🧩 hh_kazan_qa — парсер вакансий QA (hh.ru, Казань)

Проект выполняет статический парсинг HTML-страницы вакансий QA-тестировщиков в Казани с сайта [hh.ru](https://hh.ru).  
Скрипт загружает страницу локально, извлекает ключевые данные (`Название вакансии`, `Компания`, `Опыт`)  
и сохраняет результат в **.xlsx** с автоматическим форматированием таблицы.

---

## 🛠️️ Технологии

| Модуль | Назначение |
|--------|-------------|
| `requests` | загрузка HTML-страниц |
| `BeautifulSoup (bs4)` | извлечение данных по CSS-селекторам |
| `pandas` | очистка и обработка данных, экспорт в таблицу |
| `openpyxl` | создание Excel-отчёта с форматированием |
| `logging` | логирование процесса |
| `pathlib` | работа с файловой системой |

---

## 📂 Структура проекта
```
hh_kazan_qa/
├── data/
│ ├── page0.html # сохранённая HTML-страница hh.ru
│ ├── hh_kazan_qa.csv # выгрузка в CSV
│ └── hh_kazan_qa.xlsx # финальный Excel-отчёт
├── logs/
│ ├── fetch_page.log # лог загрузки страницы
│ └── parse_page.log # лог парсинга
├── fetch_page.py # модуль загрузки страницы
├── parse_page.py # модуль парсинга и экспорта
├── config.py # базовые настройки (URL, заголовки, MIN_BYTES)
└── README.md
```
## ⚙ Как запустить

### 1️⃣ Загрузить HTML-страницу
```bash
python -m hh_kazan_qa.fetch_page
```
### 2️⃣ Распарсить страницу и создать Excel-отчёт
```bash
python -m hh_kazan_qa.parse_page
```
Результат сохранится в data/hh_kazan_qa.xlsx.
## Особенности реализации
- Используется устойчивый поиск карточек через:
```bash
card = title_el.find_parent(
    lambda t: t and t.has_attr('data-qa') and 'vacancy-serp' in t['data-qa']
)
```
что делает парсер устойчивым к изменениям структуры сайта.
- Безопасное извлечение текста:
```bash
def safe_text(el):
    return " ".join(el.get_text(" ", strip=True).split()) if el else ""

```
- Автоочистка и форматирование данных:
```bash
df = df.applymap(lambda x: " ".join(x.split()) if isinstance(x, str) else x)
df = df.replace({"": "-"}).fillna("-")
```
## 📦 Требования
```bash
pip install requests beautifulsoup4 pandas openpyxl lxml
```
