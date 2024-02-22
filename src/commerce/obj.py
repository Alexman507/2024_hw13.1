class Category:
    """Класс для вывода списка товаров"""
    # Название категории
    name: str
    # Описание категории
    description: str
    # Количество категорий
    len_category: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.len_category = len(self.name)
        self.len_products = len(self.__products)

    @classmethod
    def add_product(cls, self, *list_category: list):
        """Добавляет категорию с проверкой, если уже есть такая категория - выдаёт сообщение"""
        obj = []
        print(list_category)
        for category in list_category:
            item = cls(category)
            # print(category.get('name'))
            if item.get('name') == self.name:
                # print(cls.__products)
                print(f"Извините, категория '{category.get('name')}' уже присутствует в списке!")
                continue
            else:
                obj.append(item)
                # print(item.__products)
                return obj

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
    # Название продукта
    name: str
    # Стоимость продукта
    price: float
    # Количество продукта в наличии
    quantity: int

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

add_data = [{"name": "Чай", "description": "Черный", "products": [{
    "name": "Майский",
    "description": "Нормальный пацанский чай",
    "price": 300.0,
    "quantity": 7
}]}]

add_data1 = [{"name": "Кофе", "description": "Черный гранулированный", "products": [{
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
              }]

# print(cat1.len_products)

# Проверка работы (раскомментить нужное) 13.2:
# Задача 1:
cat1.add_product(add_data)
# Задача 2:
# print(cat1.products, end="\n")
