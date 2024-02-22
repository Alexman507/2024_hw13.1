class Category:
    """Класс для вывода списка товаров"""
    # Название категории для проверки
    name: str = None
    # Количество категорий
    len_category: int = 0
    # Количество продуктов
    len_products: int = 0
    # Список продуктов, собираемый в категорию
    list_products: list = []

    def __str__(self):
        """Выводит информацию для ввода в список"""
        to_dict = {"name": self.name, "description": self.description, "products": self.__products}
        return to_dict

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.name = self.name
        self.len_products = len(Category.list_products)
        # Пополнение списка категорий при первой инициализации
        if Category.len_category == 0:
            Category.list_products.append(Category.__str__(self))
            Category.len_category = Category.len_category + 1

    @staticmethod
    def if_repeat_category(name):
        """Проверяет, есть ли такая категория в списке"""
        if Category.name == name:
            return True
        return False

    @classmethod
    def add_product(cls, *list_category: list):
        """Добавляет категорию с проверкой, если уже есть такая категория - выдаёт сообщение"""
        # print(list_category)
        for category in list_category:
            if_repeat_name = category.get('name')
            if cls.if_repeat_category(if_repeat_name):
                # print(cls.__products)
                print(f"Извините, категория '{category.get('name')}' уже присутствует в списке!")
                continue
            else:
                cls.list_products.append(category)
                cls.len_category = cls.len_category + 1
                print(cls.list_products, f"\nВсего категорий: {cls.len_category}")

    @property
    def products(self):
        """Выводит информацию об имеющихся продуктах
        :return: Список продуктов, стоимость и остаток
        """
        for category in self.__products:
            print(category)
            return f'{category.get('name')}, {category.get('price')} руб. Остаток: {category.get('quantity')} шт.'


class Product(Category):
    """Класс для вывода информации о товаре"""

    def __init__(self, name, description, __products):
        # super(Category, self)
        super().__init__(name, description, __products)
        self.name = __products.name
        self.description = __products.description
        self.price = __products.price
        self.quantity = __products.quantity


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
