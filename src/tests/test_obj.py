import src.commerce.obj
import pytest


@pytest.fixture
def category():
    return src.commerce.obj.Category(
        name='Чай',
        description='Черный',
        products=['Майский', 'Вкусный', 120.00, 5]
    )


def test_init(category):
    assert category.name == 'Чай'
    assert category.description == 'Черный'
    assert category.products == ['Майский', 'Вкусный', 120.00, 5]


@pytest.fixture
def product():
    return src.commerce.obj.Product(
        name='Майский',
        price=120.00,
        description='Вкусный',
        quantity=5
    )


def test_product(product):
    assert product.name == 'Майский'
    assert product.price == 120.00
    assert product.description == 'Вкусный'
    assert product.quantity == 5
