from src.core.binary_search.v1.binary_search import binary_search


def test_binary_search_found():
    assert binary_search([1, 3, 5, 7, 9], 3) == 1


def test_binary_search_not_found():
    assert binary_search([1, 3, 5, 7, 9], -1) is None
