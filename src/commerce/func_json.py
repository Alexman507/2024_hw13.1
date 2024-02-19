import json
from src.commerce import obj



def json_loads(json_config):
    """
            Выгружает данные в состоянии "как есть"
            :return: List of dictionaries
            :rtype: list"""

    with open(json_config, 'r', encoding='utf-8') as json_file:
        category_list: list = json.load(json_file)
        category_output = []
        products_input = []
        products_output = []
        for category in category_list:
            product = category.get('products')
            products_input.append(product)

            category_output.append(obj.Category(
                name=category.get('name'),
                description=category.get('description'),
                products=category.get('products'),
            ))
        for product in products_input:
            # print(product)
            if type(product) != list:
                products_output.append(obj.Product(
                    name=product.get('name'),
                    description=product.get('description'),
                    price=product.get('price'),
                    quantity=product.get('quantity'),
                ))
                continue

            for item in product:
                products_output.append(obj.Product(
                    name=item.get('name'),
                    description=item.get('description'),
                    price=item.get('price'),
                    quantity=item.get('quantity'),
                ))

        # print(category_output)
        return category_output, products_output

