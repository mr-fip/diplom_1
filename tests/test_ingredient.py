import allure
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@allure.suite("Тесты для класса Ingredient")
class TestIngredient:
    @allure.title("Проверка создания ингредиента")
    def test_ingredient_creation(self):
        with allure.step("Создаем ингредиент типа SAUCE"):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        
        with allure.step("Проверяем тип ингредиента"):
            assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        
        with allure.step("Проверяем имя ингредиента"):
            assert ingredient.get_name() == "hot sauce"
        
        with allure.step("Проверяем цену ингредиента"):
            assert ingredient.get_price() == 100