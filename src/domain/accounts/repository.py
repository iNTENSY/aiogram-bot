from typing import Protocol

from src.domain.accounts.entity import Account


class IAccountRepository(Protocol):
    async def create(self, entity: Account) -> None:
        raise NotImplementedError

    async def find_all(self, limit: int = 10, offset: int = 0, **parameters) -> list[Account]:
        raise NotImplementedError

    async def filter_by(self, **parameters) -> list[Account]:
        raise NotImplementedError

    async def update(self, entity: Account) -> None:
        raise NotImplementedError

    async def delete(self, **parameters) -> None:
        raise NotImplementedError
