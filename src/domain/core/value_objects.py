import datetime
import re
import uuid
from dataclasses import dataclass
from typing import TypeVar, Generic

from src.domain.core.exceptions import DomainValidationError


ValueT = TypeVar("ValueT")


@dataclass(frozen=True)
class ValueObject(Generic[ValueT]):
    value: ValueT

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        """
        Must be implemented by subclasses.
        Raises a :class:`DomainValidationError` if the value is invalid.
        """

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value!r})"


@dataclass(frozen=True)
class IntegerVO(ValueObject):
    value: int

    def validate(self) -> None:
        if isinstance(self.value, bool) or not isinstance(self.value, int):
            raise DomainValidationError(message=f"Value ({self.value}) must be of type INTEGER")


@dataclass(frozen=True)
class PositiveIntegerVO(IntegerVO):
    def validate(self) -> None:
        super().validate()

        if self.value <= 0:
            raise DomainValidationError(message=f"Value ({self.value}) must be greater then 0")


@dataclass(frozen=True)
class UuidVO(ValueObject):
    value: uuid.UUID


@dataclass(frozen=True)
class BooleanVO(ValueObject):
    value: bool

    def validate(self) -> None:
        if not isinstance(self.value, bool):
            raise DomainValidationError(message=f"Value ({self.value}) must be of type BOOLEAN")


@dataclass(frozen=True)
class StringVO(ValueObject):
    value: str

    def validate(self) -> None:
        if not isinstance(self.value, str):
            raise DomainValidationError(
                message=f"Value ({self.value}) must be of type STRING"
            )


@dataclass(frozen=True)
class IntegerIDVO(PositiveIntegerVO):
    """Should be used to implements positive integer ID."""


@dataclass(frozen=True)
class PhoneNumberVO(StringVO):
    def validate(self) -> None:
        pattern = r'^\+[0-9]{11}$'
        if not re.match(pattern, self.value):
            raise DomainValidationError(
                message="Incorrect phone number pattern",
            )


@dataclass(frozen=True)
class DatetimeVO(ValueObject):
    value: datetime.datetime

    def validate(self) -> None:
        if not isinstance(self.value, datetime.datetime):
            raise DomainValidationError(f"{self.value} must be datetime`s type")


@dataclass(frozen=True)
class EmptyVO(ValueObject):
    value: None

    def validate(self) -> None:
        pass
