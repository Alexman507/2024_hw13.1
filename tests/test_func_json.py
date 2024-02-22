from src.commerce import func_json


def test_json_loads():
    data_category = func_json.json_loads('../tests/test_data/test_products.json')
    assert len(data_category) > 0
    assert len(data_category) == 2
    assert type(data_category) == list
    assert data_category is not None
