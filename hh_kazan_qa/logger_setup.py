from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file: str) -> logging.Logger:
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)  # гарантируем папку logs

    logger = logging.getLogger()          # корневой логгер
    logger.setLevel(logging.INFO)

    # убираем старые хендлеры, чтобы не было дублей записей
    for h in list(logger.handlers):
        logger.removeHandler(h)

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_h = RotatingFileHandler(
        str(log_path),                    # на всякий случай приводим к str (Windows)
        maxBytes=5 * 1024 * 1024,         # 5 МБ
        backupCount=3,                    # хранить 3 архива
        encoding="utf-8",
    )
    file_h.setFormatter(fmt)
    logger.addHandler(file_h)

    # поток в консоль — удобно видеть ошибки сразу
    stream_h = logging.StreamHandler()
    stream_h.setFormatter(fmt)
    logger.addHandler(stream_h)

    return logger
