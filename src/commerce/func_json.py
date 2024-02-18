import json
import obj


def json_loads():
    """
            Выгружает данные в состоянии "как есть"
            :return: List of dictionaries
            :rtype: list"""
    json_config = '../../data/products.json'
    with open(json_config, 'r', encoding='utf-8') as json_file:
        category_list: list = json.load(json_file)
        category_output = []
        products_output = []
        for category in category_list:
            category_output.append(obj.Category(
                name=category.get('name'),
                description=category.get('description'),
                products=category.get('products'),
            ))
            #for product in category:
                #obj.Product(
                    #name=product.get('name'),
                    #description=product.get('description'),
                    #price=product.get('price'),
                    #quantity=product.get('quantity'),
                #)
        return category_output

result = json_loads()
#json_loads()
print(result.name, result.description, result.products)
