import numpy as np
import pytest

from src.infra.lists import DoublyLinkedList, LinkedList


# ---------- Fixture parametrizada ----------
@pytest.fixture(params=[LinkedList, DoublyLinkedList])
def list_class(request):
    return request.param


# Common
def test_append(list_class):
    _list = list_class[int]()
    _list.append(1)
    _list.append(2)
    assert len(_list) == 2
    assert _list.to_list() == [1, 2]
    assert _list.head.value == 1
    assert _list.tail.value == 2


def test_prepend(list_class):
    _list = list_class[int]()
    _list.prepend(2)
    _list.prepend(1)
    assert _list.to_list() == [1, 2]


def test_insert_middle(list_class):
    _list = list_class([1, 2, 4])
    _list.insert(2, 3)
    assert _list.to_list() == [1, 2, 3, 4]


def test_insert_beginning(list_class):
    _list = list_class([2, 3])
    _list.insert(0, 1)
    assert _list.to_list() == [1, 2, 3]


def test_insert_end(list_class):
    _list = list_class([1, 2])
    _list.insert(2, 3)
    assert _list.to_list() == [1, 2, 3]


def test_insert_invalid_index(list_class):
    _list = list_class([1])
    with pytest.raises(IndexError):
        _list.insert(5, 10)


def test_pop(list_class):
    _list = list_class([1, 2, 3])
    val = _list.pop()
    assert val == 3
    assert _list.to_list() == [1, 2]


def test_pop_single(list_class):
    _list = list_class([1])
    val = _list.pop()
    assert val == 1
    assert _list.to_list() == []


def test_pop_empty(list_class):
    _list = list_class[int]()
    assert _list.pop() is None


def test_pop_first(list_class):
    _list = list_class([1, 2])
    val = _list.pop_first()
    assert val == 1
    assert _list.to_list() == [2]


def test_pop_first_empty(list_class):
    _list = list_class[int]()
    assert _list.pop_first() is None


def test_remove_from_empty_list(list_class):
    _list = list_class()
    assert _list.remove(10) is False


def test_remove_value_in_head(list_class):
    _list = list_class([1, 2, 3])
    assert _list.remove(1) is True
    assert _list.to_list() == [2, 3]
    assert len(_list) == 2


def test_remove_value_in_middle(list_class):
    _list = list_class([1, 2, 3])
    assert _list.remove(2) is True
    assert _list.to_list() == [1, 3]


def test_remove_value_in_tail(list_class):
    _list = list_class([1, 2, 3])
    assert _list.remove(3) is True
    assert _list.to_list() == [1, 2]
    assert len(_list) == 2


def test_remove_value_not_found(list_class):
    _list = list_class([1, 2])
    assert _list.remove(99) is False
    assert _list.to_list() == [1, 2]


def test_remove_only_element(list_class):
    _list = list_class([42])
    assert _list.remove(42) is True
    assert _list.to_list() == []
    assert len(_list) == 0
    assert _list.head is None
    assert _list.tail is None


def test_remove_duplicates_removes_first_only(list_class):
    _list = list_class([1, 2, 2, 3])
    assert _list.remove(2) is True
    assert _list.to_list() == [1, 2, 3]
    assert len(_list) == 3


def test_find_found(list_class):
    _list = list_class([1, 2, 3])
    node = _list.find(2)
    assert node is not None
    assert node.value == 2


def test_find_not_found(list_class):
    _list = list_class([1, 2])
    assert _list.find(99) is None


def test_get_valid_index(list_class):
    _list = list_class([10, 20, 30])
    assert _list.get(1) == 20


def test_get_invalid_index(list_class):
    _list = list_class([10])
    assert _list.get(5) is None


def test_set_valid(list_class):
    _list = list_class([1, 2])
    assert _list.set(1, 99) is True
    assert _list.to_list() == [1, 99]


def test_set_invalid(list_class):
    _list = list_class([1])
    assert _list.set(2, 99) is False


def test_reverse(list_class):
    _list = list_class([1, 2, 3])
    _list.reverse()
    assert _list.to_list() == [3, 2, 1]


def test_reverse_empty(list_class):
    _list = list_class[int]()
    _list.reverse()
    assert _list.to_list() == []


def test_clear(list_class):
    _list = list_class([1, 2])
    _list.clear()
    assert len(_list) == 0
    assert _list.to_list() == []


def test_to_list(list_class):
    _list = list_class([1, 2, 3])
    assert _list.to_list() == [1, 2, 3]


def test_len(list_class):
    _list = list_class([1, 2])
    assert len(_list) == 2


def test_iteration(list_class):
    _list = list_class([1, 2, 3])
    values = [x for x in _list]  # noqa: C416
    assert values == [1, 2, 3]


def test_getitem(list_class):
    _list = list_class([10, 20])
    assert _list[1] == 20


def test_getitem_out_of_bounds(list_class):
    _list = list_class([10])
    with pytest.raises(IndexError):
        _ = _list[3]


def test_setitem(list_class):
    _list = list_class([1, 2])
    _list[1] = 99
    assert _list.to_list() == [1, 99]


def test_setitem_out_of_bounds(list_class):
    _list = list_class([1])
    with pytest.raises(IndexError):
        _list[2] = 10


def test_contains_true(list_class):
    _list = list_class([1, 2, 3])
    assert 2 in _list


def test_contains_false(list_class):
    _list = list_class([1])
    assert 99 not in _list


def test_complex_operations_consistency(list_class):
    _list = list_class([1, 2, 3])
    assert _list.to_list() == [1, 2, 3]

    _list.append(4)
    assert _list.to_list() == [1, 2, 3, 4]
    assert _list.tail.value == 4
    assert len(_list) == 4

    _list.prepend(0)
    assert _list.to_list() == [0, 1, 2, 3, 4]
    assert _list.head.value == 0
    assert len(_list) == 5

    _list.insert(2, 1.5)
    assert _list.to_list() == [0, 1, 1.5, 2, 3, 4]
    assert _list.get(2) == 1.5
    assert len(_list) == 6

    _list.pop()
    assert _list.to_list() == [0, 1, 1.5, 2, 3]
    assert _list.tail.value == 3
    assert len(_list) == 5

    _list.pop_first()
    assert _list.to_list() == [1, 1.5, 2, 3]
    assert _list.head.value == 1
    assert len(_list) == 4

    _list.remove(2)
    assert _list.to_list() == [1, 1.5, 3]
    assert len(_list) == 3


def test_reverse_integrity(list_class):
    _list = list_class([10, 20, 30])
    assert _list.to_list() == [10, 20, 30]
    _list.reverse()
    assert _list.to_list() == [30, 20, 10]
    assert _list.get(0) == 30
    assert _list.get(1) == 20
    assert _list.get(2) == 10
    assert len(_list) == 3


def test_large_list_behavior(list_class):
    data = np.arange(1000).tolist()
    _list = list_class(data)
    assert _list.to_list() == data
    assert _list.get(500) == 500

    _list[500] = -1
    assert _list.get(500) == -1
    assert _list.to_list()[500] == -1

    _list.insert(1000, 1001)
    assert _list.to_list()[-1] == 1001
    assert len(_list) == 1001


def test_all_access_patterns(list_class):
    _list = list_class([5, 10, 15])
    assert _list.to_list() == [5, 10, 15]
    assert 10 in _list
    assert list(iter(_list)) == [5, 10, 15]
    for i, val in enumerate([5, 10, 15]):
        assert _list[i] == val


# DoublyLinkedList specific
def test_doubly_linked_list_prev_pointers(list_class):
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
