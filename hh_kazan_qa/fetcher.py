from pathlib import Path

class PageFetcher:
    def __init__(self, base_url: str, out_dir: Path, min_bytes: int = 50_000, headers: dict | None = None):
        self.base_url = base_url
        self.out_dir = out_dir
        self.min_bytes = min_bytes
        self.headers = headers or {}

    def fetch(self, page: int = 0) -> Path:
        """Скачивает страницу и возвращает путь к сохранённому HTML.
        Пока: raise NotImplementedError — логику добавим следующим шагом."""
        raise NotImplementedError