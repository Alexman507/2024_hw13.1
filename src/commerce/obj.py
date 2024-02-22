class Category:
    """Класс для вывода списка товаров"""
    # Количество категорий
    len_category: int = 0
    # Количество продуктов
    len_products: int = 0
    # Список продуктов
    list_products: list = []

    def __init__(self, name, description, products):
        self.name = name
        self.description = description

        self.__products = products
        if len(products):
            Category.len_products += len(self.__products)
        Category.len_category += 1

    @staticmethod
    def if_repeat_category(self, name):
        """Проверяет, есть ли такая категория в списке"""
        if self.name == name:
            return True
        return False

    @classmethod
    def add_product(cls, product):
        """Добавляет товар в список"""
        name = product.name
        description = product.description
        price = product.price
        quantity = product.quantity
        to_dict = {
            "name": name,
            "description": description,
            "price": price,
            "quantity": quantity
        }
        cls.list_products.append(to_dict)
        # print(cls.list_products)

    @property
    def products(self):
        """Выводит информацию об имеющихся продуктах
        :return: Список продуктов, стоимость и остаток
        """
        for category in self.__products:
            # print(category)
            return f'{category.get('name')}, {category.get('price')} руб. Остаток: {category.get('quantity')} шт.'


class Product:
    """Класс для вывода информации о товаре"""
    # Список продуктов
    list_products: list = []
    prev_price = None

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        if name in Category.list_products:
            self.quantity += quantity
            if price > Product.prev_price:
                self.price = price
                Product.prev_price = self.price
        else:
            self.quantity = quantity
            self.price = price
            Product.prev_price = self.price
            Category.add_product(self)
        self.price = price

    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def get_price(self):
        return self.price

    @get_price.setter
    def get_price(self, value):
        if value > 0:
            self.price = value
        else:
            print("Некорректная цена!")


cat1 = Category("Чай", "Черный", [{
    "name": "Майский",
    "description": "Нормальный пацанский чай",
    "price": 300.0,
    "quantity": 7
}])

add_data = {"name": "Чай", "description": "Черный", "products": [{
    "name": "Майский",
    "description": "Нормальный пацанский чай",
    "price": 300.0,
    "quantity": 7
}]}

add_data1 = {"name": "Кофе", "description": "Черный гранулированный", "products": [{
    "name": "Nescafe",
    "description": "Нормальный пацанский кофе",
    "price": 300.0,
    "quantity": 7
}, {
    "name": "365 дней",
    "description": "Ну такой себе кофеек, но не помрёшь",
    "price": 100.0,
    "quantity": 3
}]
             }
add_product = Product("Nescafe",
                      "Нормальный пацанский кофе",
                      300.0, 7)

# print(cat1.len_products)

# Проверка работы (раскомментить нужное) 13.2:
# Задача 1:
# cat1.add_product(add_product)
# Задача 2:
# print(cat1.products, end="\n")
# Задача 3:
# prod1 = Product.create_product(
#     name="Кофе",
#     description="Черный гранулированный",
#     price=300.0,
#     quantity=7
# )
# # print(prod1.name, prod1.description, prod1.price, prod1.quantity, sep='\n')
# prod2 = Product.create_product(
#     name="Кофе",
#     description="Черный гранулированный",
#     price=100.0,
#     quantity=7
# )
# print(prod2.quantity)
