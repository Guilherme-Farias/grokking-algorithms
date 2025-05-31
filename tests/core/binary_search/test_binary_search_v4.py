import time

import numpy as np
import pytest

from src.core._common.comparator import IntComparator
from src.core._common.search_strategy import SearchContext
from src.core.binary_search.v3.iterative_binary_search import IterativeBinarySearch
from src.core.binary_search.v3.recursive_binary_search import RecursiveBinarySearch

n = 1000000
list_with_n_items = np.arange(n + 1).tolist()


@pytest.mark.parametrize("search_class", [IterativeBinarySearch, RecursiveBinarySearch])
def test_binary_search_and_linear_search_execution_time(search_class):
    random_number = np.random.randint(n // 2, n)
    item, expected_index = random_number, random_number

    strategy = search_class(IntComparator())
    context = SearchContext(strategy)

    start_time = time.time()
    binary_search_index = context.execute_search(list_with_n_items, item)
    bs_time = time.time() - start_time

    start_time = time.time()
    linear_search_index = list_with_n_items.index(item)
    ls_time = time.time() - start_time

    assert expected_index == binary_search_index
    assert expected_index == linear_search_index
    assert bs_time < ls_time


@pytest.mark.parametrize("search_class", [IterativeBinarySearch, RecursiveBinarySearch])
def test_execution_time_for_item_at_the_beginning(search_class):
    item, expected_index = 10, 10

    strategy = search_class(IntComparator())
    context = SearchContext(strategy)

    start_time = time.time()
    binary_search_index = context.execute_search(list_with_n_items, item)
    bs_time = time.time() - start_time

    start_time = time.time()
    linear_search_index = list_with_n_items.index(item)
    ls_time = time.time() - start_time

    assert expected_index == binary_search_index
    assert expected_index == linear_search_index
    assert bs_time > ls_time
