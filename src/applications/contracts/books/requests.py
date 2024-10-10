from dataclasses import dataclass


@dataclass(frozen=True)
class GetBooksRequest:
    offset: int
    limit: int = 10


@dataclass(frozen=True)
class GetBookByIDRequest:
    id: int
