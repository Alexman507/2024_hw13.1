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
            category_output.append(obj.Category(
                name=category.get('name'),
                description=category.get('description'),
                products=category.get('products'),
            ))

        print(category_output)
        return category_output
