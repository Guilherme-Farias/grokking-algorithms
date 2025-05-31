from typing import Generic, Iterator, List, Optional, TypeVar

from src.core._common.base_structures import AbstractList
from src.core._common.entities import DoublyListNode

T = TypeVar("T")


class DoublyLinkedList(AbstractList[T], Generic[T]):
    def __init__(self, items: Optional[List[T]] = None) -> None:
        self.head: Optional[DoublyListNode[T]] = None
        self.tail: Optional[DoublyListNode[T]] = None
        self._length: int = 0
        super().__init__(items)

    def append(self, value: T) -> None:
        new_node = DoublyListNode(value)
        if self._length == 0:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def prepend(self, value: T) -> None:
        new_node = DoublyListNode(value, next=self.head)

        if self._length == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node

        self.head = new_node
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

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        new_node = DoublyListNode(value, prev=prev, next=prev.next)
        prev.next.prev = new_node
        prev.next = new_node
        self._length += 1

    def pop(self) -> Optional[T]:
        if self._length == 0:
            return None
        val = self.tail.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self._length -= 1
        return val

    def pop_first(self) -> Optional[T]:
        if self._length == 0:
            return None
        val = self.head.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
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
            prev.next.prev = prev
            self._length -= 1
            return True
        return False

    def find(self, value: T) -> Optional[DoublyListNode[T]]:
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
        current = self.head
        self.head, self.tail = self.tail, self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

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
