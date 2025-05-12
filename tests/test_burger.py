import pytest
import allure
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@allure.suite("Тесты для класса Burger")
class TestBurger:
    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def mock_bun(self):
        bun = Mock()
        bun.get_price.return_value = 100
        bun.get_name.return_value = "black bun"
        return bun
    
    @pytest.fixture
    def mock_ingredients(self):
        sauce = Mock()
        sauce.get_price.return_value = 50
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "hot sauce"
        
        filling = Mock()
        filling.get_price.return_value = 100
        filling.get_type.return_value = "FILLING"
        filling.get_name.return_value = "cutlet"
        
        return [sauce, filling]

    @allure.title("Проверка установки булочек в бургер")
    def test_set_buns(self, burger, mock_bun):
        with allure.step("Устанавливаем булочку в бургер"):
            burger.set_buns(mock_bun)
        
        with allure.step("Проверяем, что булочка установлена корректно"):
            assert burger.bun == mock_bun
        
    @allure.title("Проверка добавления ингредиента в бургер")
    def test_add_ingredient(self, burger, mock_ingredients):
        with allure.step("Добавляем ингредиент в бургер"):
            burger.add_ingredient(mock_ingredients[0])
        
        with allure.step("Проверяем, что ингредиент добавлен"):
            assert len(burger.ingredients) == 1

    @allure.title("Проверка удаления ингредиента из бургера")
    def test_remove_ingredient(self, burger, mock_ingredients):
        with allure.step("Добавляем ингредиенты в бургер"):
            burger.ingredients = mock_ingredients.copy()
        
        with allure.step("Удаляем один ингредиент"):
            burger.remove_ingredient(0)
        
        with allure.step("Проверяем, что ингредиент удален"):
            assert len(burger.ingredients) == 1

    @allure.title("Проверка перемещения ингредиента в бургере")
    def test_move_ingredient(self, burger, mock_ingredients):
        with allure.step("Добавляем ингредиенты в бургер"):
            burger.ingredients = mock_ingredients.copy()
        
        with allure.step("Перемещаем ингредиент"):
            burger.move_ingredient(0, 1)
        
        with allure.step("Проверяем новую позицию ингредиента"):
            assert burger.ingredients[1] == mock_ingredients[0]

    @allure.title("Проверка расчета цены бургера")
    def test_get_price(self, burger, mock_bun, mock_ingredients):
        with allure.step("Устанавливаем булочку и ингредиенты"):
            burger.set_buns(mock_bun)
            burger.ingredients = mock_ingredients
        
        with allure.step("Проверяем общую цену бургера"):
            assert burger.get_price() == (100*2 + 50 + 100)
        
    @allure.title("Проверка формирования чека")
    def test_get_receipt(self, burger, mock_bun, mock_ingredients):
        with allure.step("Устанавливаем булочку и ингредиенты"):
            burger.set_buns(mock_bun)
            burger.ingredients = mock_ingredients
        
        with allure.step("Получаем чек"):
            receipt = burger.get_receipt()
        
        with allure.step("Проверяем содержание чека"):
            assert "(==== black bun ====)" in receipt
            assert "= sauce hot sauce =" in receipt
            assert "= filling cutlet =" in receipt
            assert "Price: 350" in receipt