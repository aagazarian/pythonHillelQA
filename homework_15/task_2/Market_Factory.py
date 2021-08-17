from homework_15.task_2.All_Products import AppleProduct, BananaProduct, CelleryProduct, StrawberryProduct
from homework_15.task_2.All_Products.Product import Product


class MarketFactory:
    @staticmethod
    def get_product(name: str) -> Product:
        if name == "apple":
            return AppleProduct()
        elif name == "banana":
            return BananaProduct()
        elif name == "cellery":
            return CelleryProduct()
        elif name == "strawberry":
            return StrawberryProduct()
        else:
            raise Exception("Incorrect name of product(")


if __name__ == '__main__':
    product_1 = MarketFactory.get_product("apple")
    print(product_1.name)
    product_2 = MarketFactory.get_product("banana")
    print(product_2.name)
    product_3 = MarketFactory.get_product("cellery")
    print(product_3.name)
    product_4 = MarketFactory.get_product("strawberry")
    print(product_4.name)
