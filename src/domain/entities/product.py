from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return False
        return self.id == other.id
