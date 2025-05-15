import pytest
import allure
from praktikum.burger import Burger

@allure.suite("Тесты для класса Burger")
class TestBurger:
    @allure.title("Проверка расчета цены бургера")
    def test_get_price(self, burger, mock_bun, mock_ingredients):
        with allure.step("Устанавливаем булочку и ингредиенты"):
            burger.set_buns(mock_bun)
            burger.ingredients = mock_ingredients
        
        expected_price = (mock_bun.get_price() * 2 + sum(ingredient.get_price() for ingredient in mock_ingredients))
        
        with allure.step("Проверяем общую цену бургера"):
            assert burger.get_price() == expected_price