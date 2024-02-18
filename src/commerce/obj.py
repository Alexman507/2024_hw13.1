class Category:
    """Класс для вывода списка товаров"""
    # todo: название, описание, товары
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


class Product:
    """Класс для вывода информации о товаре"""
    # todo: название, описание, цена, количество в наличии
    name: str
    price: float
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity


cat1 = Category('aboba', 'products', [1, 2, 3, 4, 5])

