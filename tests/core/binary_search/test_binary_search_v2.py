import pytest

from src.core.binary_search.binary_search_v2_clean_code import (
    IterativeBinarySearch,
    RecursiveBinarySearch,
)


@pytest.mark.parametrize("search_class", [IterativeBinarySearch, RecursiveBinarySearch])
def test_binary_search_found(search_class):
    search = search_class()
    assert search.search([1, 3, 5, 7, 9], 3) == 1


@pytest.mark.parametrize("search_class", [IterativeBinarySearch, RecursiveBinarySearch])
def test_binary_search_not_found(search_class):
    search = search_class()
    assert search.search([1, 3, 5, 7, 9], -1) is None
