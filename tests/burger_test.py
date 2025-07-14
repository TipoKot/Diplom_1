import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

def test_set_buns():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Пшеничная"
    burger.set_buns(mock_bun)
    assert burger.bun == mock_bun

def test_add_ingredient():
    burger = Burger()
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "Сыр"
    burger.add_ingredient(mock_ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == mock_ingredient

def test_remove_ingredient():
    burger = Burger()
    mock_ingredient = Mock()
    burger.add_ingredient(mock_ingredient)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0 

def test_move_ingredient():
    burger = Burger()
    mock_ingredient1 = Mock()
    mock_ingredient2 = Mock()
    burger.add_ingredient(mock_ingredient1)
    burger.add_ingredient(mock_ingredient2)
    burger.move_ingredient(0, 1)
    assert len(burger.ingredients) == 2
    assert burger.ingredients[0] == mock_ingredient2
    assert burger.ingredients[1] == mock_ingredient1

@pytest.mark.parametrize(
    "bun_price, ingredients_prices, expected_price",
    [
        (2.0, [], 4.0),                    # только булка
        (2.5, [1.0], 6.0),                # булка + 1 ингредиент
        (3.0, [1.5, 0.5], 8.0),           # булка + 2 ингредиента
        (1.0, [0.5, 0.5, 0.5], 3.5),      # булка + 3 ингредиента
    ]
)
def test_get_price(bun_price, ingredients_prices, expected_price):
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_price.return_value = bun_price
    burger.set_buns(mock_bun)

    for price in ingredients_prices:
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = price
        burger.add_ingredient(mock_ingredient)

    assert burger.get_price() == expected_price

def test_get_receipt():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Пшеничная"
    mock_bun.get_price.return_value = 2.5
    burger.set_buns(mock_bun)
    
    mock_ingredient1 = Mock()
    mock_ingredient1.get_name.return_value = "Сыр"
    mock_ingredient1.get_type.return_value = "начинка"
    mock_ingredient1.get_price.return_value = 1.0
    
    mock_ingredient2 = Mock()
    mock_ingredient2.get_name.return_value = "Кетчуп"
    mock_ingredient2.get_type.return_value = "соус"
    mock_ingredient2.get_price.return_value = 1.0
    
    burger.add_ingredient(mock_ingredient1)
    burger.add_ingredient(mock_ingredient2)
    
    expected_receipt = (
        "(==== Пшеничная ====)\n"
        "= начинка Сыр =\n"
        "= соус Кетчуп =\n"
        "(==== Пшеничная ====)\n\n"
        "Price: 7.0"
    )
    
    assert burger.get_receipt() == expected_receipt