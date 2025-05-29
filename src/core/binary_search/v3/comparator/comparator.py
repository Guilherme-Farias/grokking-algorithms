from typing import Protocol, TypeVar

T = TypeVar("T")


class Comparator(Protocol[T]):
    def compare(self, a: T, b: T) -> int: ...
