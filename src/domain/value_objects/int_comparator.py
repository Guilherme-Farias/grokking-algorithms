from src.domain.interfaces import Comparator


class IntComparator(Comparator[int]):
    def compare(self, a: int, b: int) -> int:
        return a - b
