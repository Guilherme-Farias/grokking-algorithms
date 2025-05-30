from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class ListNode(Generic[T]):
    def __init__(self, value: T, next: Optional["ListNode[T]"] = None) -> None:
        self.value: T = value
        self.next: Optional["ListNode[T]"] = next
