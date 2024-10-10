import abc

from src.domain.core.entity import DomainEntity


class AbstractMapper(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def generate_to_entity(obj: dict, **inner_entities) -> DomainEntity:
        raise NotImplementedError

    @staticmethod
    def generate_to_dict(obj: DomainEntity) -> dict:
        return {key: value.value for key, value in vars(obj).items()}
