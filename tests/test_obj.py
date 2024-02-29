import src.commerce.obj
import pytest


@pytest.fixture
def category():
    return src.commerce.obj.Category(
        name='Чай',
        description='Черный',
        products=[{
            "name": "Майский",
            "description": "Вкусный",
            "price": 120.0,
            "quantity": 5
        }]
    )


def test_init(category):
    assert category.name == 'Чай'
    assert category.description == 'Черный'
    assert category.products[0] == "Майский, 120 руб. Остаток: 5 шт."


def test_str(category):
    assert str(category) == "Чай, количество продуктов 5 шт."


def test_len(category):
    assert len(category) == 5


def test_add_product(category):
    test_cat = src.commerce.obj.Product(
        name='Майский',
        price=120.00,
        description='Вкусный',
        quantity=5
    )
    category.add_product(test_cat)
    assert str(test_cat) == "Майский, 120.0 руб. Остаток: 5 шт."


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


def test_string(product):
    assert str(product) == "Майский, 120.0 руб. Остаток: 5 шт."


def test_add(product):
    test_product1 = src.commerce.obj.Product("Lipton",
                                             "Ну такой себе",
                                             300.0, 7)

    test_product2 = src.commerce.obj.Product("Nestea",
                                             "Сладенький",
                                             300.0, 7)

    assert test_product1 + test_product2 == 4200.0

    with pytest.raises(TypeError):
        class_smart = src.commerce.obj.Smartphone("Xiaomi", "low coast", 10_000, 15,
                                                  "6/10", "MI8", "256 GB", "Blue")
        class_grass = src.commerce.obj.LawnGrass("Grass", "овёс", 100, 2,
                                                 "RF", "2 weeks", "Green")
        class_smart + class_grass


def test_create(product):
    prod1 = src.commerce.obj.Product.create_product({
        "name": "Кофе",
        "description": "Черный гранулированный",
        "price": 300.0,
        "quantity": 7
    })

    assert str(prod1) == "Кофе, 300.0 руб. Остаток: 7 шт."


def test_update():
    prod2 = src.commerce.obj.Product("Lipton",
                                     "Ну такой себе",
                                     300.0, 7)
    prod2_new = {"name": "Lipton",
                 "description": "Ну такой себе",
                 "price": 120.0,
                 "quantity": 5
                 }
    res = prod2.create_product(prod2_new)

    assert res.price == 300
    assert res.quantity == 12


def test_get_price(product):
    prod1 = src.commerce.obj.Product("Кофе",
                                     "Черный гранулированный",
                                     300.0,
                                     7
                                     )
    prod1.price = 4000
    assert prod1.price == 4000.00

    with pytest.raises(ValueError):
        prod1.price = -400
