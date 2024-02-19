from src.commerce.func_json import json_loads

cat_out, prod_out = json_loads('../data/products.json')

for cat in cat_out:
    print(cat.name)

for prod in prod_out:
    print(prod.name)