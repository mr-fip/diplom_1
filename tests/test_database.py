import allure
from unittest.mock import Mock, patch
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@allure.suite("Тесты для класса Database")
class TestDatabase:
    @allure.title("Проверка инициализации базы данных")
    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_database_initialization(self, mock_ingredient, mock_bun):
        with allure.step("Создаем экземпляр базы данных"):
            db = Database()
        
        with allure.step("Проверяем количество доступных булочек"):
            assert len(db.available_buns()) == 3
        
        with allure.step("Проверяем количество доступных ингредиентов"):
            assert len(db.available_ingredients()) == 6
        
        with allure.step("Проверяем вызовы моков"):
            mock_bun.assert_called()
            mock_ingredient.assert_called()