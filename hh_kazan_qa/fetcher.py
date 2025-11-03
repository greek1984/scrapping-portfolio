import pandas as pd
import requests
from pathlib import Path

class PageFetcher:
    """Класс для загрузки HTML-страниц и проверки их целостности"""
    def __init__(
            self,
            base_url: str,
            out_path: Path,
            min_bytes: int = 50_000,
            headers: dict[str,str] | None = None,
            timeout: int = 20,
            pause: float = 1.0,
            max_items: int = 30
    ):
        # если заголовок не будет передан
        if headers is None:
            self.headers = {"User-Agent": "Mozilla/5.0 (compatible; PortfolioFetcher/1.0)"}
        else:
            self.headers = headers

        self.base_url = base_url
        self.out_path = out_path
        self.min_bytes = min_bytes
        self.timeout = timeout
        self.pause = pause
        self.max_items = max(1, (max_items))

        default_dir = Path(__file__).resolve().parent / 'data'
        self.out_path = Path(out_path or default_dir)
        self.out_path.mkdir(parents=True, exist_ok=True)

    def fetch(self, page: int = 0) -> Path:
        # Формирование URL
        sep = "&" if "?" in self.base_url else "?"
        url = self.base_url if page == 0 else f"{self.base_url}{sep}page={page}"
        # Выполнение запроса GET
        r = requests.get(url, headers=self.headers, timeout=self.timeout)
        # Обработка неподходящих запросов
        r.raise_for_status()
        # Получение данных в виде текста
        html = r.text
        # Проверка размера сохранённого в кэш файла HTML
        if len(html) < self.min_bytes:
           raise ValueError(f"HTML too small")
        # Сохранение HTML в 'data'
        saving_path = self.out_path / f"page{page}.html"
        saving_path.write_text(html, encoding='utf-8')
        # Возврат пути
        return saving_path

    def _safe_text(self, el) -> str:
        """Безопасно берёт текст из тега."""
        if not el:
            return ""
        return " ".join(el.get_text(" ", strip=True).split())

    def _to_excel(self, items: list[dict], path: Path):
        """Экспорт (запись) данных в файл формата """
        try:
            df = pd.DataFrame(items)
            df.to_excel(path, index=False)
            print(f'Данные сохранены в {path}')
        except Exception as e:
            print(f'Ошибка сохранения данных: {e}')

