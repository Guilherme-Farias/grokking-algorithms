from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class SearchStrategy(ABC, Generic[T]):
    @abstractmethod
    def search(self, data: List[T], target: T) -> Optional[int]:
        pass
