# HH Kazan QA Parser

## Описание проекта
Парсер вакансий **QA-тестировщиков** для региона **Казань** с сайта [hh.ru](https://hh.ru).  
Собирает данные о вакансиях, компаниях и опыте работы, сохраняет их в `.xlsx`.

## Архитектура
Проект реализован в **ООП-стиле** с разделением на модули:
- `fetcher.py` — загрузка HTML-страниц;
- `parser_oop.py` — извлечение данных с помощью BeautifulSoup;
- `pipeline.py` — объединяет загрузку, парсинг и сохранение;
- `test_fetcher.py` — тестовый запуск пайплайна;
- `data/` — результаты (HTML + Excel).

## Технологии
- Python 3.10  
- requests  
- beautifulsoup4 + lxml  
- pandas + openpyxl  

## Установка и запуск
**1. Клонируйте репозиторий(если еще не скачан):**
```
git clone [https://github.com/greek1984/scrapping-portfolio.git](https://github.com/greek1984/scrapping-portfolio.git)
```
**2. Перейдите в каталог проекта:**
```commandline
cd scrapping-portfolio/hh_kazan_qa
```
**3. Создайте и активируйте виртуальное окружение:**
```
# Для Windows
python -m venv venv
venv\Scripts\activate

# Для macOS/Linux
python3 -m venv venv
source venv/bin/activate``
 ```
**4. Установите зависимости:**
```
pip install -r requirements.txt
```
**5. Из корня проекта запустите парсер:**
```
python -m hh_kazan_qa.test_fetcher
```
## Результат:

HTML-страница → hh_kazan_qa/data/page0.html

Excel-файл → hh_kazan_qa/data/hh_page0.xlsx

## Структура каталогов

```hh_kazan_qa/
│
├── data/
│   ├── page0.html
│   └── hh_page0.xlsx
│
├── fetcher.py
├── parser_oop.py
├── pipeline.py
└── test_fetcher.py
```
### Примечания

Код разработан с учётом хорошей читаемости и логирования.

При необходимости можно задать другие параметры (город, ключевые слова, лимит вакансий).

