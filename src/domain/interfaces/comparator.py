from typing import Protocol

from src.domain.types import T


class Comparator(Protocol[T]):
    def compare(self, a: T, b: T) -> int: ...
