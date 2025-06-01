import time

import numpy as np
import pytest

from src.domain.entities import Product
from src.domain.services.search import SearchContext
from src.domain.value_objects import IntComparator, ProductByIdComparator
from src.infra.searches import IterativeBinarySearch, RecursiveBinarySearch

# ----------------------------------
# Fixtures reutilizáveis
# ----------------------------------


@pytest.fixture
def int_list():
    return [1, 3, 5, 7, 9]


@pytest.fixture
def product_list():
    return [
        Product(1, "A"),
        Product(3, "B"),
        Product(5, "C"),
    ]


@pytest.fixture
def comparators():
    return {"int": IntComparator(), "product": ProductByIdComparator()}


# ----------------------------------
# Testes para casos encontrados
# ----------------------------------


@pytest.mark.parametrize("search_class", [IterativeBinarySearch, RecursiveBinarySearch])
@pytest.mark.parametrize(
    "data_key, target, expected_index",
    [
        ("int", 3, 1),
        ("product", Product(3, "qualquer"), 1),
    ],
    ids=["int-found", "product-found"],
)
def test_binary_search_found(
    search_class, data_key, target, expected_index, comparators, int_list, product_list
):
    data_map = {"int": int_list, "product": product_list}
    comparator = comparators[data_key]
    search = search_class(comparator)
    assert search.search(data_map[data_key], target) == expected_index


# ----------------------------------
# Testes para casos não encontrados
# ----------------------------------


@pytest.mark.parametrize("search_class", [IterativeBinarySearch, RecursiveBinarySearch])
@pytest.mark.parametrize(
    "data_key, target",
    [
        ("int", -1),
        ("product", Product(4, "irrelevante")),
    ],
    ids=["int-not-found", "product-not-found"],
)
def test_binary_search_not_found(
    search_class, data_key, target, comparators, int_list, product_list
):
    data_map = {"int": int_list, "product": product_list}
    comparator = comparators[data_key]
    search = search_class(comparator)
    assert search.search(data_map[data_key], target) is None


# ----------------------------------
# Testes de performance com listas grandes
# ----------------------------------

n = 1_000_000
list_with_n_items = np.arange(n + 1).tolist()


@pytest.mark.parametrize("search_class", [IterativeBinarySearch, RecursiveBinarySearch])
def test_binary_vs_linear_execution_time_middle(search_class):
    item = np.random.randint(n // 2, n)
    expected_index = item

    context = SearchContext(search_class(IntComparator()))

    start = time.time()
    binary_index = context.execute_search(list_with_n_items, item)
    bs_time = time.time() - start

    start = time.time()
    linear_index = list_with_n_items.index(item)
    ls_time = time.time() - start

    assert binary_index == expected_index
    assert linear_index == expected_index
    assert bs_time < ls_time


@pytest.mark.parametrize("search_class", [IterativeBinarySearch, RecursiveBinarySearch])
def test_binary_vs_linear_execution_time_beginning(search_class):
    item = 10
    expected_index = item

    context = SearchContext(search_class(IntComparator()))

    start = time.time()
    binary_index = context.execute_search(list_with_n_items, item)
    bs_time = time.time() - start

    start = time.time()
    linear_index = list_with_n_items.index(item)
    ls_time = time.time() - start

    assert binary_index == expected_index
    assert linear_index == expected_index
    assert bs_time > ls_time  # linear deve ser mais rápido no início
