from .fetcher import PageFetcher
from .pipeline import Pipeline
from .parser_oop import VacancyParser
from pathlib import Path

pkg_dir = Path(__file__).resolve().parent   # .../hh_kazan_qa
data_dir = pkg_dir / 'data'                 # .../hh_kazan_qa/data

fetcher = PageFetcher(base_url="https://kazan.hh.ru/search/vacancy?text=тестировщик", out_path=data_dir)
parser = VacancyParser(max_items=30)
pipe = Pipeline(fetcher, parser, data_dir)
pipe.run_once(page=0)


print("Ok: Pipeline constructed")