# Созданы юнит-тесты, покрывающие класс Bun
# Используй моки и параметризацию там, где нужно.

import pytest
from praktikum.bun import Bun

class TestBun:
    def test_get_name(self):
        bun = Bun("Пшеничная", 3.0)
        assert bun.get_name() == "Пшеничная"

    def test_get_price(self):
        bun = Bun("Пшеничная", 3.0)
        assert bun.get_price() == 3.0