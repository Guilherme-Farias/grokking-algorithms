from src.domain.entities import Product


def test_product_equality_same_id():
    p1 = Product(id=1, name="Product A")
    p2 = Product(id=1, name="Product B")

    assert p1 == p2


def test_product_inequality_different_id():
    p1 = Product(id=1, name="Product A")
    p2 = Product(id=2, name="Product A")

    assert p1 != p2


def test_product_inequality_different_type():
    p1 = Product(id=1, name="Product A")
    not_a_product = {"id": 1, "name": "Product A"}

    assert p1 != not_a_product


def test_product_repr_and_fields():
    p = Product(id=99, name="Widget")
    assert p.id == 99
    assert p.name == "Widget"
    assert repr(p) == "Product(id=99, name='Widget')"
