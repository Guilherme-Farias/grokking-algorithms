from src.domain.entities import DoublyListNode


def test_single_node_creation():
    node = DoublyListNode(10)
    assert node.value == 10
    assert node.prev is None
    assert node.next is None


def test_node_linking_forward_and_backward():
    node1 = DoublyListNode(1)
    node2 = DoublyListNode(2, prev=node1)
    node1.next = node2

    assert node1.next == node2
    assert node2.prev == node1
    assert node2.next is None
    assert node1.prev is None


def test_chained_nodes():
    node1 = DoublyListNode("a")
    node2 = DoublyListNode("b", prev=node1)
    node3 = DoublyListNode("c", prev=node2)
    node1.next = node2
    node2.next = node3

    assert node1.next == node2
    assert node2.prev == node1
    assert node2.next == node3
    assert node3.prev == node2
    assert node3.next is None
