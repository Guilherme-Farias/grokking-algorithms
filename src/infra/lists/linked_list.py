from typing import Generic, Iterator, List, Optional

from src.domain.entities import BaseList, ListNode
from src.domain.types import T


class LinkedList(BaseList[T], Generic[T]):
    def __init__(self, items: Optional[List[T]] = None) -> None:
        self.head: Optional[ListNode[T]] = None
        self.tail: Optional[ListNode[T]] = None
        self._length: int = 0
        super().__init__(items)

    def append(self, value: T) -> None:
        new_node = ListNode(value)
        if self._length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def prepend(self, value: T) -> None:
        new_node = ListNode(value, self.head)
        self.head = new_node
        if self._length == 0:
            self.tail = new_node
        self._length += 1

    def insert(self, index: int, value: T) -> None:
        if index < 0 or index > self._length:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(value)
            return
        if index == self._length:
            self.append(value)
            return

        new_node = ListNode(value)
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        new_node.next = prev.next
        prev.next = new_node
        self._length += 1

    def pop(self) -> Optional[T]:
        if self._length == 0:
            return None
        if self._length == 1:
            val = self.head.value
            self.head = self.tail = None
            self._length = 0
            return val
        prev = self.head
        while prev.next and prev.next is not self.tail:
            prev = prev.next

        val = self.tail.value
        prev.next = None
        self.tail = prev
        self._length -= 1
        return val

    def pop_first(self) -> Optional[T]:
        if self._length == 0:
            return None
        val = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self._length -= 1
        return val

    def remove(self, value: T) -> bool:
        if self._length == 0:
            return False
        if self.head.value == value:
            self.pop_first()
            return True
        if self.tail.value == value:
            self.pop()
            return True

        prev = self.head
        while prev.next and prev.next.value != value:
            prev = prev.next

        if prev.next:
            prev.next = prev.next.next
            self._length -= 1
            return True
        return False

    def find(self, value: T) -> Optional[ListNode[T]]:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def get(self, index: int) -> Optional[T]:
        if index < 0 or index >= self._length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set(self, index: int, value: T) -> bool:
        if index < 0 or index >= self._length:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
        return True

    def reverse(self) -> None:
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def clear(self) -> None:
        self.head = self.tail = None
        self._length = 0

    def to_list(self) -> List[T]:
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __getitem__(self, index: int) -> T:
        val = self.get(index)
        if val is None:
            raise IndexError("Index out of range")
        return val

    def __setitem__(self, index: int, value: T) -> None:
        if not self.set(index, value):
            raise IndexError("Index out of range")

    def __contains__(self, value: T) -> bool:
        return self.find(value) is not None
