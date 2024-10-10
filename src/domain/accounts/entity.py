import uuid
from dataclasses import dataclass

from src.domain.core.entity import DomainEntity
from src.domain.core.value_objects import (UuidVO,
                                           BooleanVO,
                                           ValueObject,
                                           PhoneNumberVO, PositiveIntegerVO, EmptyVO, StringVO)


@dataclass
class Account(DomainEntity):
    id: UuidVO
    username: StringVO
    telegram_id: PositiveIntegerVO
    phone: PhoneNumberVO | EmptyVO
    is_verified: BooleanVO
    is_active: BooleanVO
    is_staff: BooleanVO
    is_superuser: BooleanVO

    @staticmethod
    def create(
            username: str,
            phone: str | None,
            telegram_id: int,
            is_verified: bool = False,
            is_active: bool = True,
            is_staff: bool = False,
            is_superuser: bool = False
    ) -> "Account":
        return Account(
            id=UuidVO(uuid.uuid4()),
            username=StringVO(username),
            phone=PhoneNumberVO(phone) if phone else EmptyVO(phone),
            telegram_id=PositiveIntegerVO(telegram_id),
            is_verified=BooleanVO(is_verified),
            is_active=BooleanVO(is_active),
            is_staff=BooleanVO(is_staff),
            is_superuser=BooleanVO(is_superuser),
        )

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                attribute: ValueObject = getattr(self, key)
                value_object_type = attribute.__class__
            else:
                continue
            setattr(self, key, value_object_type(value))
