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

    def add_product(self, product):
        """Добавляет товар в существующую категорию после инициализации"""
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
        self.__products.append(to_dict)

    @property
    def products(self):
        """Выводит информацию об имеющихся продуктах
        :return: Список продуктов, стоимость и остаток
        """
        for category in self.__products:
            # print(category)
            yield f'{category.get('name')}, {category.get('price')} руб. Остаток: {category.get('quantity')} шт.'


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

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

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

product1 = Product("Lipton",
                   "Ну такой себе",
                   300.0, 7)

# print("cat1", cat1.len_products)

# Проверка работы (раскомментить нужное) 13.3:
# Задача 1:
# print(product1)
# Задача 2:
# Задача 3:
