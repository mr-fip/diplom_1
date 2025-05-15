import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import *

@pytest.fixture
def burger():
    """Фикстура для создания экземпляра бургера."""
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = BUN_PRICE
    bun.get_name.return_value = BUN_NAME
    return bun

@pytest.fixture
def mock_ingredients():
    sauce = Mock()
    sauce.get_price.return_value = INGREDIENT_PRICE_1
    sauce.get_type.return_value = INGREDIENT_TYPE
    sauce.get_name.return_value = INGREDIENT_NAME
    
    filling = Mock()
    filling.get_price.return_value = 100
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "cutlet"
    
    return [sauce, filling]