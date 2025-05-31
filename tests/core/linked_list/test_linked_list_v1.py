# import numpy as np
import numpy as np
import pytest

from src.core.linked_list.v1.doubly_linked_list import DoublyLinkedList
from src.core.linked_list.v1.linked_list import LinkedList


# ---------- Fixture parametrizada ----------
@pytest.fixture(params=[LinkedList, DoublyLinkedList])
def list_class(request):
    return request.param


# ---------- append ----------
def test_append(list_class):
    ll = list_class[int]()
    ll.append(1)
    ll.append(2)
    assert len(ll) == 2
    assert ll.to_list() == [1, 2]
    assert ll.head.value == 1
    assert ll.tail.value == 2


# ---------- prepend ----------
def test_prepend(list_class):
    ll = list_class[int]()
    ll.prepend(2)
    ll.prepend(1)
    assert ll.to_list() == [1, 2]


# ---------- insert ----------
def test_insert_middle(list_class):
    ll = list_class([1, 2, 4])
    ll.insert(2, 3)
    assert ll.to_list() == [1, 2, 3, 4]


def test_insert_beginning(list_class):
    ll = list_class([2, 3])
    ll.insert(0, 1)
    assert ll.to_list() == [1, 2, 3]


def test_insert_end(list_class):
    ll = list_class([1, 2])
    ll.insert(2, 3)
    assert ll.to_list() == [1, 2, 3]


def test_insert_invalid_index(list_class):
    ll = list_class([1])
    with pytest.raises(IndexError):
        ll.insert(5, 10)


# ---------- pop ----------
def test_pop(list_class):
    ll = list_class([1, 2, 3])
    val = ll.pop()
    assert val == 3
    assert ll.to_list() == [1, 2]


def test_pop_single(list_class):
    ll = list_class([1])
    val = ll.pop()
    assert val == 1
    assert ll.to_list() == []


def test_pop_empty(list_class):
    ll = list_class[int]()
    assert ll.pop() is None


# ---------- pop_first ----------
def test_pop_first(list_class):
    ll = list_class([1, 2])
    val = ll.pop_first()
    assert val == 1
    assert ll.to_list() == [2]


def test_pop_first_empty(list_class):
    ll = list_class[int]()
    assert ll.pop_first() is None


# ---------- remove ----------
def test_remove_existing(list_class):
    ll = list_class([1, 2, 3])
    assert ll.remove(2) is True
    assert ll.to_list() == [1, 3]


def test_remove_non_existing(list_class):
    ll = list_class([1, 2])
    assert ll.remove(99) is False
    assert ll.to_list() == [1, 2]


# ---------- find ----------
def test_find_found(list_class):
    ll = list_class([1, 2, 3])
    node = ll.find(2)
    assert node is not None
    assert node.value == 2


def test_find_not_found(list_class):
    ll = list_class([1, 2])
    assert ll.find(99) is None


# ---------- get ----------
def test_get_valid_index(list_class):
    ll = list_class([10, 20, 30])
    assert ll.get(1) == 20


def test_get_invalid_index(list_class):
    ll = list_class([10])
    assert ll.get(5) is None


# ---------- set ----------
def test_set_valid(list_class):
    ll = list_class([1, 2])
    assert ll.set(1, 99) is True
    assert ll.to_list() == [1, 99]


def test_set_invalid(list_class):
    ll = list_class([1])
    assert ll.set(2, 99) is False


# ---------- reverse ----------
def test_reverse(list_class):
    ll = list_class([1, 2, 3])
    ll.reverse()
    assert ll.to_list() == [3, 2, 1]


def test_reverse_empty(list_class):
    ll = list_class[int]()
    ll.reverse()
    assert ll.to_list() == []


# ---------- clear ----------
def test_clear(list_class):
    ll = list_class([1, 2])
    ll.clear()
    assert len(ll) == 0
    assert ll.to_list() == []


# ---------- to_list ----------
def test_to_list(list_class):
    ll = list_class([1, 2, 3])
    assert ll.to_list() == [1, 2, 3]


# ---------- __len__ ----------
def test_len(list_class):
    ll = list_class([1, 2])
    assert len(ll) == 2


# ---------- __iter__ ----------
def test_iteration(list_class):
    ll = list_class([1, 2, 3])
    values = [x for x in ll]
    assert values == [1, 2, 3]


# ---------- __getitem__ ----------
def test_getitem(list_class):
    ll = list_class([10, 20])
    assert ll[1] == 20


def test_getitem_out_of_bounds(list_class):
    ll = list_class([10])
    with pytest.raises(IndexError):
        _ = ll[3]


# ---------- __setitem__ ----------
def test_setitem(list_class):
    ll = list_class([1, 2])
    ll[1] = 99
    assert ll.to_list() == [1, 99]


def test_setitem_out_of_bounds(list_class):
    ll = list_class([1])
    with pytest.raises(IndexError):
        ll[2] = 10


# ---------- __contains__ ----------
def test_contains_true(list_class):
    ll = list_class([1, 2, 3])
    assert 2 in ll


def test_contains_false(list_class):
    ll = list_class([1])
    assert 99 not in ll


def test_complex_operations_consistency(list_class):
    ll = list_class([1, 2, 3])
    assert ll.to_list() == [1, 2, 3]

    ll.append(4)
    assert ll.to_list() == [1, 2, 3, 4]
    assert ll.tail.value == 4
    assert len(ll) == 4

    ll.prepend(0)
    assert ll.to_list() == [0, 1, 2, 3, 4]
    assert ll.head.value == 0
    assert len(ll) == 5

    ll.insert(2, 1.5)
    assert ll.to_list() == [0, 1, 1.5, 2, 3, 4]
    assert ll.get(2) == 1.5
    assert len(ll) == 6

    ll.pop()
    assert ll.to_list() == [0, 1, 1.5, 2, 3]
    assert ll.tail.value == 3
    assert len(ll) == 5

    ll.pop_first()
    assert ll.to_list() == [1, 1.5, 2, 3]
    assert ll.head.value == 1
    assert len(ll) == 4

    ll.remove(2)
    assert ll.to_list() == [1, 1.5, 3]
    assert len(ll) == 3


def test_doubly_linked_list_prev_pointers():
    dll = DoublyLinkedList([1, 2, 3])
    assert dll.to_list() == [1, 2, 3]
    assert dll.head.prev is None
    assert dll.head.next.value == 2
    assert dll.head.next.prev == dll.head

    middle = dll.head.next
    assert middle.value == 2
    assert middle.prev.value == 1
    assert middle.next.value == 3

    assert dll.tail.value == 3
    assert dll.tail.prev.value == 2
    assert dll.tail.next is None


def test_reverse_integrity(list_class):
    ll = list_class([10, 20, 30])
    assert ll.to_list() == [10, 20, 30]
    ll.reverse()
    assert ll.to_list() == [30, 20, 10]
    assert ll.get(0) == 30
    assert ll.get(1) == 20
    assert ll.get(2) == 10
    assert len(ll) == 3


def test_large_list_behavior(list_class):
    data = np.arange(1000).tolist()
    ll = list_class(data)
    assert ll.to_list() == data
    assert ll.get(500) == 500

    ll[500] = -1
    assert ll.get(500) == -1
    assert ll.to_list()[500] == -1

    ll.insert(1000, 1001)
    assert ll.to_list()[-1] == 1001
    assert len(ll) == 1001


def test_all_access_patterns(list_class):
    ll = list_class([5, 10, 15])
    assert ll.to_list() == [5, 10, 15]
    assert 10 in ll
    assert list(iter(ll)) == [5, 10, 15]
    for i, val in enumerate([5, 10, 15]):
        assert ll[i] == val
