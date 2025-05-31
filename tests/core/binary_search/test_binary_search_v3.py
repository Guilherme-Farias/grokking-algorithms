import pytest

from src.core._common.comparator import IntComparator, ProductByIdComparator
from src.core._common.entities import Product
from src.core.binary_search.v3.iterative_binary_search import IterativeBinarySearch
from src.core.binary_search.v3.recursive_binary_search import RecursiveBinarySearch


@pytest.mark.parametrize(
    "search_class, comparator, data, target, expected",
    [
        # IntComparator - encontrado
        (IterativeBinarySearch, IntComparator(), [1, 3, 5, 7, 9], 3, 1),
        (RecursiveBinarySearch, IntComparator(), [1, 3, 5, 7, 9], 3, 1),
        # ProductByIdComparator - encontrado
        (
            IterativeBinarySearch,
            ProductByIdComparator(),
            [Product(1, "A"), Product(3, "B"), Product(5, "C")],
            Product(3, "qualquer"),
            1,
        ),
        (
            RecursiveBinarySearch,
            ProductByIdComparator(),
            [Product(1, "A"), Product(3, "B"), Product(5, "C")],
            Product(3, "qualquer"),
            1,
        ),
    ],
)
def test_binary_search_found(search_class, comparator, data, target, expected):
    search = search_class(comparator)
    assert search.search(data, target) == expected


@pytest.mark.parametrize(
    "search_class, comparator, data, target",
    [
        # IntComparator - não encontrado
        (IterativeBinarySearch, IntComparator(), [1, 3, 5, 7, 9], -1),
        (RecursiveBinarySearch, IntComparator(), [1, 3, 5, 7, 9], -1),
        # ProductByIdComparator - não encontrado
        (
            IterativeBinarySearch,
            ProductByIdComparator(),
            [Product(1, "A"), Product(3, "B"), Product(5, "C")],
            Product(4, "irrelevante"),
        ),
        (
            RecursiveBinarySearch,
            ProductByIdComparator(),
            [Product(1, "A"), Product(3, "B"), Product(5, "C")],
            Product(4, "irrelevante"),
        ),
    ],
)
def test_binary_search_not_found(search_class, comparator, data, target):
    search = search_class(comparator)
    assert search.search(data, target) is None
