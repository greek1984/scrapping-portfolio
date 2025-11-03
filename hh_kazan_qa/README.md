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

## Как запустить
Из корня проекта выполнить:

```bash
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

