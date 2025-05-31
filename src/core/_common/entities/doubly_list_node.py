from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class DoublyListNode(Generic[T]):
    def __init__(
        self,
        value: T,
        prev: Optional["DoublyListNode[T]"] = None,
        next: Optional["DoublyListNode[T]"] = None,
    ):
        self.value = value
        self.prev = prev
        self.next = next
