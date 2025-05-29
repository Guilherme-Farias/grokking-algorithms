from src.core.binary_search.v3.comparator.comparator import Comparator
from src.core.binary_search.v3.entities.product import Product


class ProductByIdComparator(Comparator[Product]):
    def compare(self, a: Product, b: Product) -> int:
        return a.id - b.id
