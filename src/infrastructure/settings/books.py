from dataclasses import dataclass


@dataclass(frozen=True)
class BooksSettings:
    limit: int
