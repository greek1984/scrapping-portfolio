from pathlib import Path
from .fetcher import PageFetcher
from .parser_oop import VacancyParser


class Pipeline:
    def __init__(self, fetcher: PageFetcher, parser: VacancyParser, workdir: Path):
        self.fetcher = fetcher
        self.parser = parser
        self.workdir = workdir

    def run_once(self, page: int = 0) -> None:
        path = self.fetcher.fetch(page)
        items =self.parser.parse(path)
        print(len(items))
        self.workdir.mkdir(parents=True, exist_ok=True)
        out_path = self.workdir / f"hh_page{page}.xlsx"
        self.fetcher._to_excel(items, out_path)
        print(f"Сохранено в {out_path}")