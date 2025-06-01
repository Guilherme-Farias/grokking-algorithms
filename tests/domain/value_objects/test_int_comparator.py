import pytest

from src.domain.value_objects import IntComparator


@pytest.mark.parametrize(
    "a,b,expected_sign",
    [
        (1, 2, -1),
        (5, 5, 0),
        (10, 4, 1),
    ],
)
def test_compare_sign(a, b, expected_sign):
    result = IntComparator().compare(a, b)

    if expected_sign < 0:
        assert result < 0
    elif expected_sign == 0:
        assert result == 0
    else:
        assert result > 0
