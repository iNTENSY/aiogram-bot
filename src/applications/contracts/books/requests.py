from dataclasses import dataclass


@dataclass(frozen=True)
class GetBooksRequest:
    page: int = 1


@dataclass(frozen=True)
class GetBookByIDRequest:
    id: int
