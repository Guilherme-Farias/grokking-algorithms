from src.domain.entities import Product
from src.domain.interfaces import Comparator


class ProductByIdComparator(Comparator[Product]):
    def compare(self, a: Product, b: Product) -> int:
        return a.id - b.id
