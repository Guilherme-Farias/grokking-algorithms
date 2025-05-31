from ..entities import Product
from .comparator import Comparator


class ProductByIdComparator(Comparator[Product]):
    def compare(self, a: Product, b: Product) -> int:
        return a.id - b.id
