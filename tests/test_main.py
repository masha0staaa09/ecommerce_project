import pytest
from main import Product, Category


def test_product():
    product = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    assert "_Product__price" in vars(product)


def test_new_product():
    data = {
        "name": "Samsung",
        "description": "Смартфон",
        "price": 180000.0,
        "quantity": 5
    }

    product = Product.new_product(data)

    assert product.name == "Samsung"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter():
    product = Product("Samsung", "Смартфон", 1000, 5)

    product.price = 2000

    assert product.price == 2000


@pytest.mark.parametrize("price", [0, -100])
def test_invalid_price(price, capsys):
    product = Product("Samsung", "Смартфон", 1000, 5)
    product.price = price

    assert product.price == 1000
    assert ("Цена не должна быть нулевая или "
            "отрицательная") in capsys.readouterr().out


def test_category():
    product1 = Product("Samsung", "Смартфон", 180000, 5)
    product2 = Product("iPhone", "Смартфон", 210000, 8)
    category = Category(
        "Смартфоны",
        "Категория смартфонов",
        [product1, product2]
    )

    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"
    assert "Samsung, 180000 руб." in category.products
    assert "iPhone, 210000 руб." in category.products
    assert "_Category__products" in vars(category)


def test_category_counters():
    product1 = Product("Samsung", "Смартфон", 180000, 5)
    product2 = Product("iPhone", "Смартфон", 210000, 8)

    old_category_count = Category.category_count
    old_product_count = Category.product_count

    Category("Смартфоны", "Описание", [product1, product2])

    assert Category.category_count == old_category_count + 1
    assert Category.product_count == old_product_count + 2


def test_empty_category():
    category = Category("Пустая категория", "Описание", [])

    assert category.name == "Пустая категория"
    assert category.products == ""


def test_add_product():
    category = Category("Смартфоны", "Описание", [])
    product = Product("Samsung", "Смартфон", 180000, 5)

    old_product_count = Category.product_count
    category.add_product(product)

    assert "Samsung" in category.products
    assert Category.product_count == old_product_count + 1


def test_product_str():
    product = Product("Samsung", "Смартфон", 100000, 5)
    assert str(product) == (
        "Samsung, 100000 руб. Остаток: 5 шт."
    )


def test_category_str():
    product1 = Product("Samsung", "Смартфон", 100000, 5)
    product2 = Product("iPhone", "Смартфон", 200000, 8)
    category = Category(
        "Смартфоны",
        "Категория смартфонов",
        [product1, product2]
    )

    assert str(category) == (
        "Смартфоны, количество продуктов: 13 шт."
    )


def test_product_add():
    product1 = Product("Samsung", "Смартфон", 100, 10)
    product2 = Product("iPhone", "Смартфон", 200, 2)

    assert product1 + product2 == 1400
