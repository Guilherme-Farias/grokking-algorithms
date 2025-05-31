from typing import Generic, List, Optional, TypeVar

from .search_strategy import SearchStrategy

T = TypeVar("T")


class SearchContext(Generic[T]):
    def __init__(self, strategy: SearchStrategy[T]):
        self._strategy = strategy

    def execute_search(self, data: List[T], target: T) -> Optional[int]:
        return self._strategy.search(data, target)
