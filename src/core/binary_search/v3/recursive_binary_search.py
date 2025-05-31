from typing import List, Optional, TypeVar

from .base_binary_search import BaseBinarySearch

T = TypeVar("T")


class RecursiveBinarySearch(BaseBinarySearch[T]):
    def _do_search(
        self, data: List[T], target: T, left: int, right: int
    ) -> Optional[int]:
        if not self._has_elements_to_search(left, right):
            return None

        mid = self._get_middle_index(left, right)
        mid_value = data[mid]

        if self._is_target_found(mid_value, target):
            return mid
        elif self._is_target_greater_than(mid_value, target):
            return self._do_search(data, target, mid + 1, right)
        elif self._is_target_less_than(mid_value, target):
            return self._do_search(data, target, left, mid - 1)

        return None
