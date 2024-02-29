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
            Category.len_products += len(self.__products)
        else:
            Category.len_products = len(self.__products)
        Category.len_category += 1

    def __str__(self):
        """Выводит информацию о экземпляре
        :return: Список продуктов, стоимость и остаток
        """
        sum_len = len(self)
        name = self.name

        return f'{name}, количество продуктов {sum_len} шт.'

    def __len__(self):
        """Возвращает количество продуктов в категории"""
        sum_quantity = 0
        for product in self.__products:
            sum_quantity += product['quantity']
        return int(sum_quantity)

    def add_product(self, product):
        """Добавляет товар в существующую категорию после инициализации"""
        name = product.name
        description = product.description
        price = int(product.price)
        quantity = product.quantity
        obj = Product(name, description, price, quantity)
        self.__products.append(obj)

    @property
    def products(self):
        """Выводит информацию об имеющихся продуктах (для теста)
        :return: Список продуктов, стоимость и остаток
        """
        list_products = []
        for category in self.__products:
            list_products.append(f'{category.get("name")}, '
                                 f'{int(category.get("price"))} руб. '
                                 f'Остаток: {category.get("quantity")} шт.')

        return list_products


class Product:
    """Класс для вывода информации о товаре"""
    # Список существующих названий продуктов для проверки
    list_products: list = []
    prev_price = None

    def __init__(self, name, description, price, quantity):
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.name = name
        if not Product.list_products:
            Product.list_products.append(self)

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Возвращает сумму цен и количества"""
        if not isinstance(other, type(other)):
            result = int(self.price * self.quantity) + (other.price * other.quantity)
            return result

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError

    @classmethod
    def create_product(cls, _dict: dict):
        """Создает товар, если уже есть такой товар - обновляет количество и цену"""
        name = _dict["name"]
        description = _dict["description"]
        price = _dict["price"]
        quantity = _dict["quantity"]
        # print(cls.list_products)
        for product in cls.list_products:
            if name == product.name:
                print("Такой продукт уже есть.")
                quantity += product.quantity
                product.quantity = quantity
            # if product.price != price:
                if price < product.price:
                    price = product.price
            print("Данные по цене и количеству обновлены!")
        return cls(name, description, price, quantity)


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, manufacturer_country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color


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

product1 = Product("Lipton",
                   "Ну такой себе",
                   300.0, 7)

product1_new = {"name": "Lipton",
                "description": "Ну такой себе",
                "price": 120.0,
                "quantity": 5
                }

product2 = Product("Nestea",
                   "Сладенький",
                   300.0, 7)

# print("cat1", cat1)
# res1 = product1.create_product(product1_new)
# print(res1.price, res1.quantity)
# Проверка работы (раскомментить нужное) 13.3:
# Задача 1:
# print(product1)
# Задача 2:
# print(f'Стоимость двух товаров в наличии на складе:', product1 + product2, "руб.")
# Задача 3:
