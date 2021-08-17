from abc import ABC


class Product(ABC):
    _name: str

    @property
    def name(self):
        return self._name
