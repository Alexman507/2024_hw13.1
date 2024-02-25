class Category:
    """Класс для вывода списка товаров"""
    # Количество категорий
    len_category: int = 0
    # Количество продуктов
    len_products: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description

        self.__products = products
        if Category.len_products != 0:
            # print("init", len(self.__products))
            Category.len_products += len(self.__products)
        else:
            Category.len_products = len(self.__products)
        Category.len_category += 1

    # def if_repeat_category(self, name):
    #     """Проверяет, есть ли такая категория в списке"""
    #     if name in self.__products:
    #         return True
    #     return False

    def add_product(self, product):
        """Добавляет товар в существующую категорию после инициализации"""
        name = product.name
        description = product.description
        price = product.price
        quantity = product.quantity
        obj = Product(name, description, price, quantity)
        self.__products.append(obj)

    @property
    def products(self):
        """Выводит информацию об имеющихся продуктах
        :return: Список продуктов, стоимость и остаток
        """
        list_products = []
        for category in self.__products:
            list_products.append(f'{category.get('name')}, '
                                 f'{category.get('price')} руб. '
                                 f'Остаток: {category.get('quantity')} шт.')
        return list_products


class Product:
    """Класс для вывода информации о товаре"""
    # Список существующих названий продуктов для проверки
    list_products: list = []
    prev_price = None

    def __init__(self, name, description, price, quantity):
        self.description = description
        self.price = price
        self.quantity = quantity
        self.name = name
        Product.list_products.append({
            "name": name,
            "description": description,
            "price": price,
            "quantity": quantity
        })

    @classmethod
    def create_product(cls, _dict: dict):
        """Создает товар, если уже есть такой товар - обновляет количество и цену"""
        name = _dict["name"]
        description = _dict["description"]
        price = _dict["price"]
        quantity = _dict["quantity"]
        if name in cls.list_products:
            print("Такой продукт уже есть.")
            for product in cls.list_products:
                if name == product["name"]:
                    quantity += product["quantity"]
                    product["quantity"] = quantity
                    if product["price"] != price:
                        product["price"] = max(price, product["price"])
                print("Данные по цене и количеству обновлены!")
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
add_product = Product("Lipton",
                      "Ну такой себе",
                      300.0, 7)

# print("cat1", cat1.len_products)

# Проверка работы (раскомментить нужное) 13.2:
# Задача 1:
# new_cat1 = cat1.add_product(add_product)
# print("ncat", new_cat1.len_products)
# Задача 2:
# print(new_cat1.products, end="\n")
# Задача 3:
prod1 = Product.create_product({
    "name": "Кофе",
    "description": "Черный гранулированный",
    "price": 300.0,
    "quantity": 7
}
)
# print(prod1.name, prod1.description, prod1.price, prod1.quantity, sep='\n')
# prod2 = Product.create_product(
#     name="Кофе",
#     description="Черный гранулированный",
#     price=100.0,
#     quantity=7
# )
# print(prod2.quantity)
