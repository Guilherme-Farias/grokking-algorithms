import pytest

from src.domain.entities import Product
from src.domain.value_objects import ProductByIdComparator


@pytest.mark.parametrize(
    "a_id, b_id, expected_sign",
    [
        (1, 3, -1),
        (7, 7, 0),
        (9, 4, 1),
    ],
)
def test_compare_signs(a_id, b_id, expected_sign):
    a = Product(id=a_id, name="A")
    b = Product(id=b_id, name="B")
    result = ProductByIdComparator().compare(a, b)

    if expected_sign < 0:
        assert result < 0
    elif expected_sign == 0:
        assert result == 0
    else:
        assert result > 0
