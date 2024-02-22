from src.commerce.func_json import json_loads

cat_out = json_loads('../data/products.json')


for category in cat_out:
    print(category.name)



# for prod in prod_out:
#     print(prod.name)
