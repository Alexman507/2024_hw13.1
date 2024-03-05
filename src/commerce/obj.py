from abc import ABC, abstractmethod


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

    def add_product(self, product: object):
        """Добавляет товар в существующую категорию после инициализации"""
        if not isinstance(product, Product):
            raise TypeError(f'Cannot add {type(product)} to {type(self)}')
        else:
            self.__products.append(product)

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

    def average_price(self):
        """Возвращает среднюю цену продуктов в категории"""
        sum_price = 0
        for product in self.__products:
            sum_price += product['price']
        try:
            result = int(sum_price / len(self.__products))
        except ZeroDivisionError as e:
            print(e)
        else:
            return result


class ProductABS(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def price(self):
        pass


class MixinRepr:
    """Миксин для вывода информации о товаре"""

    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v}, '
        return f"создан объект со свойствами: ({object_attributes[0:-2]})"


class Product(MixinRepr, ProductABS):
    """Класс для вывода информации о товаре"""
    # Список существующих названий продуктов для проверки
    list_products: list = []
    prev_price = None

    def __init__(self, name, description, price, quantity):
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        self.name = name
        super().__init__()
        if not Product.list_products:
            Product.list_products.append(self)

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Возвращает сумму цен и количества"""
        if isinstance(other, type(self)):
            result = int(self.price * self.quantity) + (other.price * other.quantity)
            return result
        else:
            raise TypeError

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
                if quantity == 0:
                    raise ValueError("Товар с нулевым количеством не может быть добавлен")
            print("Данные по цене и количеству обновлены!")
        return cls(name, description, price, quantity)


class Smartphone(Product, MixinRepr):
    """Класс для вывода информации о товаре Смартфон"""

    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product, MixinRepr):
    """Класс для вывода информации о товаре Трава газонная"""

    def __init__(self, name, description, price, quantity, manufacturer_country, germination_period, color):
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)


prod1 = Product("Test", "Test", 1, 12)
lawn1 = LawnGrass("Lawn", "Test", 150, 100, "RF", "2 years", "Green")
smart1 = Smartphone("Smartphone", "Test", 12_000, 100, "6.8/10", "l1", "128gb", "Blue")

print(LawnGrass.__mro__)
print(Smartphone.__mro__)
print(Product.__mro__)
