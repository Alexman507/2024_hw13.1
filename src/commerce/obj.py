class Category:
    """Класс для вывода списка товаров"""
    # Количество категорий
    len_category: int = 0
    # Количество продуктов
    len_products: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        if len(products):
            Category.len_products += len(self.products)
        Category.len_category += 1

    @staticmethod
    def if_repeat_category(name):
        """Проверяет, есть ли такая категория в списке"""
        pass
        # if Category.name == name:
        #     return True
        # return False

    @classmethod
    def add_product(cls, *list_category: list):
        """Добавляет категорию с проверкой, если уже есть такая категория - выдаёт сообщение"""
        pass
        # print(list_category)
        # for category in list_category:
        #     if_repeat_name = category.get('name')
            # if cls.if_repeat_category(if_repeat_name):
            #     # print(cls.__products)
            #     print(f"Извините, категория '{category.get('name')}' уже присутствует в списке!")
            #     continue
            # else:
            #     cls.list_products.append(category)
            #     cls.len_category = cls.len_category + 1
            #     print(cls.list_products, f"\nВсего категорий: {cls.len_category}")

    # @property
    # def products(self):
    #     """Выводит информацию об имеющихся продуктах
    #     :return: Список продуктов, стоимость и остаток
    #     """
    #     pass
        # for category in self.__products:
        #     print(category)
        #     return f'{category.get('name')}, {category.get('price')} руб. Остаток: {category.get('quantity')} шт.'


class Product:
    """Класс для вывода информации о товаре"""

    def __init__(self, price, quantity, name, description):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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

# print(cat1.len_products)

# Проверка работы (раскомментить нужное) 13.2:
# Задача 1:
cat1.add_product(add_data1)
# Задача 2:
# print(cat1.products, end="\n")
