from pathlib import Path
from .entities import Vacancy

class VacancyParser:
    def parse(self, html_path: Path) -> list[Vacancy]:
        """Возвращает список Vacancy из сохранённого HTML."""
        raise NotImplementedError