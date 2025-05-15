import allure
from unittest.mock import patch
from praktikum.database import Database

@allure.suite("Тесты для класса Database")
class TestDatabase:
    @allure.title("Проверка инициализации базы данных")
    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_database_initialization(self, mock_ingredient, mock_bun):
        db = Database()
        
        assert len(db.available_buns()) == 3
        assert len(db.available_ingredients()) == 6
        mock_bun.assert_called()
        mock_ingredient.assert_called()