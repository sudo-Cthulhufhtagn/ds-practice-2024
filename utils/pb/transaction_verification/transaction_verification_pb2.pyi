from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionRequest(_message.Message):
    __slots__ = ("expiration_date",)
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    expiration_date: str
    def __init__(self, expiration_date: _Optional[str] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...
