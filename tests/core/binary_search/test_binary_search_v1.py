from src.core.binary_search.binary_search_v1_leet_code import binary_search


def test_binary_search_found():
    assert binary_search([1, 3, 5, 7, 9], 3) == 1


def test_binary_search_not_found():
    assert binary_search([1, 3, 5, 7, 9], -1) is None
