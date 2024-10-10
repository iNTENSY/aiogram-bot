from dataclasses import dataclass

from src.domain.books.entity import Book


@dataclass(frozen=True)
class BookResponse:
    id: int
    title: str
    author: str
    file_path: str

    @staticmethod
    def create(entity: Book) -> "BookResponse":
        return BookResponse(
            id=entity.id.value,
            title=entity.title.value,
            author=entity.author.value,
            file_path=entity.file_path.value
        )
