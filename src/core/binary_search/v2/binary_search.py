from abc import ABC, abstractmethod
from typing import List, Optional


class BaseBinarySearch(ABC):
    def search(self, data: List[int], target: int) -> Optional[int]:
        return self._do_search(data, target, 0, len(data) - 1)

    @abstractmethod
    def _do_search(
        self, data: List[int], target: int, left: int, right: int
    ) -> Optional[int]:
        pass

    def _has_elements_to_search(self, left: int, right: int) -> bool:
        return left <= right

    def _get_middle_index(self, left: int, right: int) -> int:
        return (left + right) // 2

    def _is_target_found(self, guess: int, target: int) -> bool:
        return guess == target

    def _should_search_right(self, guess: int, target: int) -> bool:
        return guess < target


class IterativeBinarySearch(BaseBinarySearch):
    def _do_search(
        self, data: List[int], target: int, left: int, right: int
    ) -> Optional[int]:
        while self._has_elements_to_search(left, right):
            mid = self._get_middle_index(left, right)
            guess = data[mid]

            if self._is_target_found(guess, target):
                return mid

            if self._should_search_right(guess, target):
                left = mid + 1
            else:
                right = mid - 1

        return None


class RecursiveBinarySearch(BaseBinarySearch):
    def _do_search(
        self, data: List[int], target: int, left: int, right: int
    ) -> Optional[int]:
        if not self._has_elements_to_search(left, right):
            return None

        mid = self._get_middle_index(left, right)
        guess = data[mid]

        if self._is_target_found(guess, target):
            return mid

        if self._should_search_right(guess, target):
            return self._do_search(data, target, mid + 1, right)

        return self._do_search(data, target, left, mid - 1)
