# 🕸️ Web Scraping & Data Parsing Portfolio

This repository contains a collection of professional **web-scraping** and **data-parsing** projects built with Python.  
Each project focuses on extracting structured information from websites of different types — from static HTML to dynamically rendered pages using JavaScript.

The portfolio demonstrates clean code practices, modular design, and reliable data export to CSV / Excel formats.

---

## ⚙️ Technologies & Tools

| Category | Tools & Libraries |
|-----------|------------------|
| **Core** | Python 3.10+, requests, BeautifulSoup4 (bs4), lxml |
| **Data Handling** | pandas, openpyxl |
| **Automation / Dynamic Pages** | Selenium, Playwright *(planned integration)* |
| **Logging & Utilities** | logging, pathlib, re |
| **Testing** | pytest *(for later integration)* |

---

## 📁 Project Structure
```
scrapping_portfolio/
├── hh_kazan_qa/ # parser for QA vacancies on hh.ru
│ ├── data/
│ ├── logs/
│ ├── fetch_page.py
│ ├── parse_page.py
│ └── README.md
├── (future projects...)
│ ├── ozon_prices/
│ ├── avito_cars/
│ └── yandex_news/
└── README.md # this file
```
---

## 🧩 Current Projects

| Project | Description | Technologies |
|----------|--------------|---------------|
| [hh_kazan_qa](hh_kazan_qa/) | Static HTML parsing of QA vacancies from hh.ru (Kazan region). | requests, BeautifulSoup, pandas, openpyxl |

---

## 🧭 Roadmap

✅ **Stage 1:** Static HTML scraping (`requests + BeautifulSoup`)  
✅ **Stage 2:** Data processing and export (`pandas + openpyxl`)  
🔄 **Stage 3:** Dynamic content scraping (`Selenium` / `Playwright`)  
🔜 **Stage 4:** API parsing and integration testing with `pytest`  
🚀 **Stage 5:** Building CLI-ready parsers with caching and error handling

---

## 📦 Requirements

```bash
pip install requests beautifulsoup4 pandas openpyxl lxml
# optional, for dynamic scraping:
pip install selenium playwright
```
## Notes

All parsers are designed for educational and portfolio purposes.

Each project folder contains its own README.md with setup instructions and details.

Please respect each website’s robots.txt and Terms of Service before scraping.
