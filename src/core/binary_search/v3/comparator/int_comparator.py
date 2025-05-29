from src.core.binary_search.v3.comparator.comparator import Comparator


class IntComparator(Comparator[int]):
    def compare(self, a: int, b: int) -> int:
        return a - b
