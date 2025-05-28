import time

import numpy as np
import pytest

from src.core.binary_search.binary_search_v3_generic import (
    IntComparator,
    IterativeBinarySearch,
    RecursiveBinarySearch,
)

n = 1000000
list_with_n_items = np.arange(n + 1).tolist()


@pytest.mark.parametrize(
    "search_class, comparator",
    [
        (IterativeBinarySearch, IntComparator()),
        (RecursiveBinarySearch, IntComparator()),
    ],
)
def test_binary_search_and_linear_search_execution_time(search_class, comparator):
    random_number = np.random.randint(n // 2, n)
    item, expected_index = random_number, random_number

    bs = search_class(comparator)
    start_time = time.time()
    binary_search_index = bs.search(list_with_n_items, item)
    bs_time = time.time() - start_time

    start_time = time.time()
    linear_search_index = list_with_n_items.index(item)
    ls_time = time.time() - start_time

    assert expected_index == binary_search_index
    assert expected_index == linear_search_index
    assert bs_time < ls_time


@pytest.mark.parametrize(
    "search_class, comparator",
    [
        (IterativeBinarySearch, IntComparator()),
        (RecursiveBinarySearch, IntComparator()),
    ],
)
def test_execution_time_for_item_at_the_beginning(search_class, comparator):
    item, expected_index = 10, 10

    bs = search_class(comparator)
    start_time = time.time()
    binary_search_index = bs.search(list_with_n_items, item)
    bs_time = time.time() - start_time

    start_time = time.time()
    linear_search_index = list_with_n_items.index(item)
    ls_time = time.time() - start_time

    assert expected_index == binary_search_index
    assert expected_index == linear_search_index
    assert bs_time > ls_time
