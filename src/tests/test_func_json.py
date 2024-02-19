from src.commerce import func_json


def test_json_loads():
    data_category, data_product = func_json.json_loads('../../data/products.json')
    assert len(data_category) > 0
    assert len(data_product) > 0
    assert len(data_category) == 2
    assert len(data_product) == 4
    assert type(data_category) == list
    assert type(data_product) == list
    assert data_category is not None
    assert data_product is not None
