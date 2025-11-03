"""
Скрипт для загрузки и сохранения HTML-страницы с результатами поиска
вакансий с сайта hh.kz.

Функциональность:
- Отправляет GET-запрос по URL, указанному в 'config.py'.
- Проверяет ответ на наличие HTTP-ошибок.
- Проверяет, что размер полученной страницы превышает минимальный порог.
- Сохраняет HTML-код страницы в файл 'data/page0.html'.
"""

from pathlib import Path
import requests
import logging
from datetime import datetime

if __package__ is None or __package__ == "":
    import sys, pathlib
    sys.path.append(str(pathlib.Path(__file__).resolve().parent))
from config import HEADERS, BASE, MIN_BYTES
from logger_setup import setup_logger

print('sys.path[0]=', sys.path[0])
print('here=', pathlib.Path(__file__).parent)
print('-' * 60)

# Определяем пути для сохранения данных
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
html_path = DATA_DIR / 'page0.html'

setup_logger(str(BASE_DIR / "logs" / "fetch_page.log"))
log_dir = Path('data')
log_dir.mkdir(exist_ok=True)

response_text = None
try:
    logging.info("Загрузка страницы...")
    # Сохраняем данные после запроса в переменную
    r = requests.get(BASE, headers=HEADERS, timeout=15)
    # Проверяем ответ сервера на ошибки (4xx, 5xx)
    r.raise_for_status()
    # Проверка HTML-файла на минимально допустимый размер
    response_text = r.text
    if len(response_text) < MIN_BYTES:
        raise ValueError(f"Слишком маленький размер HTML ({len(response_text)}байт)")
except ValueError as e:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    bad_path = DATA_DIR / f'page0_bad_{timestamp}.html'
    if response_text is not None:
        bad_path.write_text(response_text, encoding='utf-8')
    else:
        bad_path.write_text("", encoding='utf-8')
    logging.warning(f"{e} -> сохранён {bad_path.name}")
except requests.exceptions.ConnectionError:
    logging.error("Нет соединения: проверь интернет/прокси/DNS.")
except requests.exceptions.SSLError:
    logging.error("SSL-ошибка: проблемы с сертификатом/HTTPS.")
except requests.exceptions.HTTPError as e:
    logging.error(f"HTTP {e.response.status_code}: {e}")
except requests.exceptions.RequestException as e:
    logging.error(f"Ошибка сети или HTTP: {e}")
else:
    html_path.write_text(response_text, encoding='utf-8')
    logging.info(f"Сохранено: {html_path.name}, {len(response_text)} байт")
