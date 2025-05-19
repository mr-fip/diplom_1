import allure
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import *

@allure.suite("Тесты для класса Ingredient")
class TestIngredient:
    @allure.title("Проверка создания ингредиента с разными параметрами")
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE_2),
            (INGREDIENT_TYPE_FILLING, ALTERNATIVE_NAME, ALTERNATIVE_PRICE),
            (INGREDIENT_TYPE_SAUCE, "sauce#!", 150),
        ],
    )
    def test_ingredient_creation(self, ingredient_type, name, price):
        with allure.step(f"Создаем ингредиент типа {ingredient_type} с именем '{name}' и ценой {price}"):
            ingredient = Ingredient(ingredient_type, name, price)
        
        with allure.step("Проверяем тип ингредиента через метод get_type()"):
            assert ingredient.get_type() == ingredient_type
        
        with allure.step("Проверяем имя ингредиента через метод get_name()"):
            assert ingredient.get_name() == name
        
        with allure.step("Проверяем цену ингредиента через метод get_price()"):
            assert ingredient.get_price() == price

    @allure.title("Проверка граничных значений цены ингредиента")
    @pytest.mark.parametrize(
        "price",
        [
            0,
            1,
            9999,
        ],
    )
    def test_ingredient_price_boundaries(self, price):
        with allure.step(f"Создаем ингредиент с ценой {price}"):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, price)
        
        with allure.step("Проверяем корректность цены через метод get_price()"):
            assert ingredient.get_price() == price