import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient

def test_get_price():
    ingredient = Ingredient("начинка", "Сыр", 1.5)
    assert ingredient.get_price() == 1.5

def test_get_name():
    ingredient = Ingredient("соус", "Кетчуп", 0.5)
    assert ingredient.get_name() == "Кетчуп"

def test_get_type():
    ingredient = Ingredient("начинка", "Помидор", 0.8)
    assert ingredient.get_type() == "начинка"