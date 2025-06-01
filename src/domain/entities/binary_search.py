from abc import ABC, abstractmethod
from typing import Generic, List, Optional

from src.domain.interfaces import Comparator
from src.domain.types import T


class BinarySearch(
    ABC,
    Generic[T],
):
    def __init__(self, compare: Comparator[T]):
        self._compare = compare

    def search(self, data: List[int], target: int) -> Optional[int]:
        return self._do_search(data, target, 0, len(data) - 1)

    @abstractmethod
    def _do_search(
        self, data: List[int], target: int, left: int, right: int
    ) -> Optional[int]:
        pass  # pragma: no cover

    def _has_elements_to_search(self, left: int, right: int) -> bool:
        return left <= right

    def _get_middle_index(self, left: int, right: int) -> int:
        return (left + right) // 2

    def _is_target_found(self, mid_value: T, target: T) -> bool:
        return self._compare.compare(mid_value, target) == 0

    def _is_target_less_than(self, mid_value: T, target: T) -> bool:
        return self._compare.compare(mid_value, target) > 0

    def _is_target_greater_than(self, mid_value: T, target: T) -> bool:
        return self._compare.compare(mid_value, target) < 0
