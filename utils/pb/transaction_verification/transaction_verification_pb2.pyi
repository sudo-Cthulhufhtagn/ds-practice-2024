from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BookRequest(_message.Message):
    __slots__ = ("book", "id", "clock")
    BOOK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    book: str
    id: str
    clock: str
    def __init__(self, book: _Optional[str] = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class BookResponse(_message.Message):
    __slots__ = ("status2", "id", "clock")
    STATUS2_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    status2: bool
    id: str
    clock: str
    def __init__(self, status2: bool = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class CardRequest(_message.Message):
    __slots__ = ("card", "id", "clock")
    CARD_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    card: str
    id: str
    clock: str
    def __init__(self, card: _Optional[str] = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class TransactionRequest(_message.Message):
    __slots__ = ("name", "contact", "address", "id", "clock")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    name: str
    contact: str
    address: str
    id: str
    clock: str
    def __init__(self, name: _Optional[str] = ..., contact: _Optional[str] = ..., address: _Optional[str] = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ("status", "id", "clock")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    status: bool
    id: str
    clock: str
    def __init__(self, status: bool = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class CardResponse(_message.Message):
    __slots__ = ("status3", "id", "clock")
    STATUS3_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    status3: bool
    id: str
    clock: str
    def __init__(self, status3: bool = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...
