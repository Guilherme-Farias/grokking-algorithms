from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, List, Optional, Protocol, TypeVar

T = TypeVar("T")


class Comparator(Protocol[T]):
    def compare(self, a: T, b: T) -> int: ...


class IntComparator(Comparator[int]):
    def compare(self, a: int, b: int) -> int:
        return a - b


@dataclass
class Product:
    id: int
    name: str


class ProductByIdComparator(Comparator[Product]):
    def compare(self, a: Product, b: Product) -> int:
        return a.id - b.id


class BaseBinarySearch(ABC, Generic[T]):
    def __init__(self, compare: Comparator[T]):
        self._compare = compare

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

    def _is_target_found(self, mid_value: T, target: T) -> bool:
        return self._compare.compare(mid_value, target) == 0

    def _is_target_less_than(self, mid_value: T, target: T) -> bool:
        return self._compare.compare(mid_value, target) > 0

    def _is_target_greater_than(self, mid_value: T, target: T) -> bool:
        return self._compare.compare(mid_value, target) < 0


class IterativeBinarySearch(BaseBinarySearch[T]):
    def _do_search(
        self, data: List[T], target: T, left: int, right: int
    ) -> Optional[int]:
        while self._has_elements_to_search(left, right):
            mid = self._get_middle_index(left, right)
            mid_value = data[mid]

            if self._is_target_found(mid_value, target):
                return mid
            elif self._is_target_greater_than(mid_value, target):
                left = mid + 1
            elif self._is_target_less_than(mid_value, target):
                right = mid - 1

        return None


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
