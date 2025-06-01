from typing import Generic, List, Optional

from src.domain.types import T

from .search_strategy import SearchStrategy


class SearchContext(Generic[T]):
    def __init__(self, strategy: SearchStrategy[T]):
        self._strategy = strategy

    def execute_search(self, data: List[T], target: T) -> Optional[int]:
        return self._strategy.search(data, target)
