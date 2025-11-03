from dataclasses import dataclass

@dataclass
class Vacancy:
    title: str
    company: str | None
    experience: str | None
    url: str | None