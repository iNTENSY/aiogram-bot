from src.domain.accounts.entity import Account
from src.domain.core.value_objects import BooleanVO, UuidVO, StringVO, PositiveIntegerVO, PhoneNumberVO, EmptyVO
from src.infrastructure.persistence.mappers.core import AbstractMapper


class AccountMapper(AbstractMapper):
    @staticmethod
    def generate_to_entity(obj: dict, **inner_entities) -> Account:
        return Account(
            id=UuidVO(obj["id"]),
            username=StringVO(obj["username"]),
            telegram_id=PositiveIntegerVO(obj["telegram_id"]),
            phone=PhoneNumberVO(obj["phone"]) if obj["phone"] else EmptyVO(obj["phone"]),
            is_verified=BooleanVO(obj["is_verified"]),
            is_active=BooleanVO(obj["is_active"]),
            is_staff=BooleanVO(obj["is_staff"]),
            is_superuser=BooleanVO(obj["is_superuser"]),
        )
