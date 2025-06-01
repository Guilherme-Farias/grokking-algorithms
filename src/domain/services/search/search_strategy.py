from abc import ABC, abstractmethod
from typing import Generic, List, Optional

from src.domain.types import T


class SearchStrategy(ABC, Generic[T]):
    @abstractmethod
    def search(self, data: List[T], target: T) -> Optional[int]:
        pass  # pragma: no cover
