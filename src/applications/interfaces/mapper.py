from typing import Protocol

from src.domain.core.entity import DomainEntity


class IMapper(Protocol):
    @staticmethod
    def generate_to_entity(obj: dict, **inner_entities) -> DomainEntity:
        raise NotImplementedError

    @staticmethod
    def generate_to_dict(obj: DomainEntity) -> dict:
        raise NotImplementedError
