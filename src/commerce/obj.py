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
        self.__products = products

    def add_product(self, list_category: list):
        """Добавляет категорию с проверкой, если уже есть такая категория - выдаёт сообщение"""
        # print(self.name)
        for category in list_category:
            # print(category.get('name'))
            if category.get('name') == self.name:
                # print(self.__products)
                print(f"Извините, категория '{category.get('name')}' уже присутствует в списке!")
                pass
            else:
                self.__products.append(list_category)
            # print(self.__products)


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


cat1 = Category("Чай", "Черный", [{
    "name": "Майский",
    "description": "Нормальный пацанский чай",
    "price": 300.0,
    "quantity": 7
}])

add_data = [{"name": "Чай", "description": "Черный", "products": {
    "name": "Майский",
    "description": "Нормальный пацанский чай",
    "price": 300.0,
    "quantity": 7
}}]

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


cat1.add_product(add_data)

# for products in list_category:
#     if products.name == self.name:
#         self.__products['quantity'] += products['quantity']
#         self.__products.append(products)
