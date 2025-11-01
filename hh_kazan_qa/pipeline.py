from pathlib import Path
from .fetcher import PageFetcher
from .parser_oop import VacancyParser

class Pipeline:
    def __init__(self, fetcher: PageFetcher, parser: VacancyParser, workdir: Path):
        self.fetcher = fetcher
        self.parser = parser
        self.workdir = workdir

    def run_once(self, page: int = 0) -> None:
        """fetch → parse → (пока просто print(len(vacancies)))."""
        raise NotImplementedError