from pathlib import Path
from .entities import Vacancy
from bs4 import BeautifulSoup


class VacancyParser:
    def __init__(self, max_items: int =30):
        self.max_items = max_items

    def _safe_text(self, el):
        return el.get_text(strip=True) if el else None

    def parse(self, html_path: Path) -> list[Vacancy]:
        html = html_path.read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "lxml")
        items: list[Vacancy] = []
        print(len(soup.select('a[data-qa="serp-item__title"]')))
        # берём все заголовки вакансий
        for title_el in soup.select('a[data-qa="serp-item__title"]'):
            card = title_el.find_parent(attrs={"data-qa": "serp-item"})
            container = card or title_el  # если карточки нет — работаем от title_el

            company_el = (
                    container.select_one('[data-qa="vacancy-serp__vacancy-employer"]')
                    or title_el.find_next(attrs={'data-qa': 'vacancy-serp__vacancy-employer'})
            )
            exp_el = (
                    container.select_one('[data-qa*="vacancy-work-experience"]')
                    or title_el.find_next(attrs={'data-qa': 'vacancy-work-experience'})
            )

            items.append(
                Vacancy(
                    title=self._safe_text(title_el),
                    company=self._safe_text(company_el),
                    experience=self._safe_text(exp_el),
                    url=title_el.get("href")
                )
            )

            if len(items) >= self.max_items:
                break

        return items

