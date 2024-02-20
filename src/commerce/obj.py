class Category:
    """Класс для вывода списка товаров"""
    # Название категории
    name: str
    # Описание категории
    description: str
    # Список продуктов в категории
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


class Product:
    """Класс для вывода информации о товаре"""
    # Название продукта
    name: str
    # Стоимость продукта
    price: float
    # Количество продукта в наличии
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity


cat1 = Category('aboba', 'products', [1, 2, 3, 4, 5])

