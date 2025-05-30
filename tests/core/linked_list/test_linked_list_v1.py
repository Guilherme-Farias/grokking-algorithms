import pytest

from src.core.linked_list.v1.linked_list import LinkedList


# ---------- append ----------
def test_append():
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    assert len(ll) == 2
    assert ll.to_list() == [1, 2]
    assert ll.head.value == 1
    assert ll.tail.value == 2


# ---------- prepend ----------
def test_prepend():
    ll = LinkedList[int]()
    ll.prepend(2)
    ll.prepend(1)
    assert ll.to_list() == [1, 2]


# ---------- insert ----------
def test_insert_middle():
    ll = LinkedList([1, 2, 4])
    ll.insert(2, 3)
    assert ll.to_list() == [1, 2, 3, 4]


def test_insert_beginning():
    ll = LinkedList([2, 3])
    ll.insert(0, 1)
    assert ll.to_list() == [1, 2, 3]


def test_insert_end():
    ll = LinkedList([1, 2])
    ll.insert(2, 3)
    assert ll.to_list() == [1, 2, 3]


def test_insert_invalid_index():
    ll = LinkedList([1])
    with pytest.raises(IndexError):
        ll.insert(5, 10)


# ---------- pop ----------
def test_pop():
    ll = LinkedList([1, 2, 3])
    val = ll.pop()
    assert val == 3
    assert ll.to_list() == [1, 2]


def test_pop_single():
    ll = LinkedList([1])
    val = ll.pop()
    assert val == 1
    assert ll.to_list() == []


def test_pop_empty():
    ll = LinkedList[int]()
    assert ll.pop() is None


# ---------- pop_first ----------
def test_pop_first():
    ll = LinkedList([1, 2])
    val = ll.pop_first()
    assert val == 1
    assert ll.to_list() == [2]


def test_pop_first_empty():
    ll = LinkedList[int]()
    assert ll.pop_first() is None


# ---------- remove ----------
def test_remove_existing():
    ll = LinkedList([1, 2, 3])
    assert ll.remove(2) is True
    assert ll.to_list() == [1, 3]


def test_remove_non_existing():
    ll = LinkedList([1, 2])
    assert ll.remove(99) is False
    assert ll.to_list() == [1, 2]


# ---------- find ----------
def test_find_found():
    ll = LinkedList([1, 2, 3])
    node = ll.find(2)
    assert node is not None
    assert node.value == 2


def test_find_not_found():
    ll = LinkedList([1, 2])
    assert ll.find(99) is None


# ---------- get ----------
def test_get_valid_index():
    ll = LinkedList([10, 20, 30])
    assert ll.get(1) == 20


def test_get_invalid_index():
    ll = LinkedList([10])
    assert ll.get(5) is None


# ---------- set ----------
def test_set_valid():
    ll = LinkedList([1, 2])
    assert ll.set(1, 99) is True
    assert ll.to_list() == [1, 99]


def test_set_invalid():
    ll = LinkedList([1])
    assert ll.set(2, 99) is False


# ---------- reverse ----------
def test_reverse():
    ll = LinkedList([1, 2, 3])
    ll.reverse()
    assert ll.to_list() == [3, 2, 1]


def test_reverse_empty():
    ll = LinkedList[int]()
    ll.reverse()
    assert ll.to_list() == []


# ---------- clear ----------
def test_clear():
    ll = LinkedList([1, 2])
    ll.clear()
    assert len(ll) == 0
    assert ll.to_list() == []


# ---------- to_list ----------
def test_to_list():
    ll = LinkedList([1, 2, 3])
    assert ll.to_list() == [1, 2, 3]


# ---------- __len__ ----------
def test_len():
    ll = LinkedList([1, 2])
    assert len(ll) == 2


# ---------- __iter__ ----------
def test_iteration():
    ll = LinkedList([1, 2, 3])
    values = [x for x in ll]
    assert values == [1, 2, 3]


# ---------- __getitem__ ----------
def test_getitem():
    ll = LinkedList([10, 20])
    assert ll[1] == 20


def test_getitem_out_of_bounds():
    ll = LinkedList([10])
    with pytest.raises(IndexError):
        _ = ll[3]


# ---------- __setitem__ ----------
def test_setitem():
    ll = LinkedList([1, 2])
    ll[1] = 99
    assert ll.to_list() == [1, 99]


def test_setitem_out_of_bounds():
    ll = LinkedList([1])
    with pytest.raises(IndexError):
        ll[2] = 10


# ---------- __contains__ ----------
def test_contains_true():
    ll = LinkedList([1, 2, 3])
    assert 2 in ll


def test_contains_false():
    ll = LinkedList([1])
    assert 99 not in ll


# ---------- for_each ----------
def test_for_each():
    ll = LinkedList([1, 2, 3])
    result = []
    ll.for_each(lambda x: result.append(x * 2))
    assert result == [2, 4, 6]
