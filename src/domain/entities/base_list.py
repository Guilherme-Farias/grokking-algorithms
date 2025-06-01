from abc import ABC, abstractmethod
from typing import Generic, Iterator, List, Optional

from src.domain.types import T


class BaseList(ABC, Generic[T]):
    def __init__(self, items: Optional[List[T]] = None) -> None:
        if items:
            for item in items:
                self.append(item)

    @abstractmethod
    def append(self, value: T) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def prepend(self, value: T) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def insert(self, index: int, value: T) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def pop(self) -> Optional[T]:
        pass  # pragma: no cover

    @abstractmethod
    def pop_first(self) -> Optional[T]:
        pass  # pragma: no cover

    @abstractmethod
    def remove(self, value: T) -> bool:
        pass  # pragma: no cover

    @abstractmethod
    def get(self, index: int) -> Optional[T]:
        pass  # pragma: no cover

    @abstractmethod
    def set(self, index: int, value: T) -> bool:
        pass  # pragma: no cover

    @abstractmethod
    def reverse(self) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def clear(self) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def to_list(self) -> List[T]:
        pass  # pragma: no cover

    @abstractmethod
    def __len__(self) -> int:
        pass  # pragma: no cover

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        pass  # pragma: no cover

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass  # pragma: no cover

    @abstractmethod
    def __setitem__(self, index: int, value: T) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def __contains__(self, value: T) -> bool:
        pass  # pragma: no cover
