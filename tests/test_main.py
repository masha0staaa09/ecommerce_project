from main import Product, Category


def test_product():
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_category():
    product1 = Product(
        "Samsung",
        "Смартфон",
        180000.0,
        5
    )
    product2 = Product("iPhone", "Смартфон", 210000.0, 8)
    category1 = Category(
        "Смартфоны",
        "Категория смартфонов",
        [product1, product2]
    )

    assert category1.name == "Смартфоны"
    assert category1.description == "Категория смартфонов"
    assert category1.products == [product1, product2]
    assert len(category1.products) == 2


def test_category_counters():
    product1 = Product(
        "Samsung",
        "Смартфон",
        180000.0,
        5
    )
    product2 = Product("iPhone", "Смартфон", 210000.0, 8)
    old_category_count = Category.category_count
    old_product_count = Category.product_count

    Category("Смартфоны", "Категория смартфонов", [product1, product2])

    assert Category.category_count == old_category_count + 1
    assert Category.product_count == old_product_count + 2


def test_empty_category():
    category = Category(
        "Пустая категория",
        "Описание",
        []
    )
    assert category.name == "Пустая категория"
    assert category.products == []
    assert len(category.products) == 0
