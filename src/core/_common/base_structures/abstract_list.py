from abc import ABC, abstractmethod
from typing import Generic, Iterator, List, Optional, TypeVar

T = TypeVar("T")


class AbstractList(ABC, Generic[T]):
    def __init__(self, items: Optional[List[T]] = None) -> None:
        if items:
            for item in items:
                self.append(item)

    @abstractmethod
    def append(self, value: T) -> None:
        pass

    @abstractmethod
    def prepend(self, value: T) -> None:
        pass

    @abstractmethod
    def insert(self, index: int, value: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> Optional[T]:
        pass

    @abstractmethod
    def pop_first(self) -> Optional[T]:
        pass

    @abstractmethod
    def remove(self, value: T) -> bool:
        pass

    @abstractmethod
    def get(self, index: int) -> Optional[T]:
        pass

    @abstractmethod
    def set(self, index: int, value: T) -> bool:
        pass

    @abstractmethod
    def reverse(self) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def to_list(self) -> List[T]:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass

    @abstractmethod
    def __setitem__(self, index: int, value: T) -> None:
        pass

    @abstractmethod
    def __contains__(self, value: T) -> bool:
        pass
