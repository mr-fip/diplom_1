import pytest
import allure
from praktikum.bun import Bun
from data import *

@allure.suite("Тесты для класса Bun")
class TestBun:
    @allure.title("Проверка создания булочки с разными параметрами")
    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("белая булка", 200),
            ("bun123", 150),
            ("#!@bun%^", 300),
        ],
    )
    def test_bun_creation(self, name, price):
        with allure.step(f"Создаем булочку с именем '{name}' и ценой {price}"):
            bun = Bun(name, price)
        
        with allure.step("Проверяем корректность имени булочки"):
            assert bun.get_name() == name
        
        with allure.step("Проверяем корректность цены булочки"):
            assert bun.get_price() == price