from src.domain.entities import ListNode


def test_single_node_creation():
    node = ListNode(42)
    assert node.value == 42
    assert node.next is None


def test_node_linking():
    node1 = ListNode("first")
    node2 = ListNode("second", next=node1)

    assert node2.value == "second"
    assert node2.next == node1
    assert node2.next.value == "first"
    assert node1.next is None


def test_chained_nodes():
    node3 = ListNode(3)
    node2 = ListNode(2, next=node3)
    node1 = ListNode(1, next=node2)

    assert node1.value == 1
    assert node1.next == node2
    assert node1.next.value == 2
    assert node1.next.next == node3
    assert node1.next.next.value == 3
    assert node1.next.next.next is None
