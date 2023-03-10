

from main import func
import pytest

def test1():
	assert func("16.11.2021 06:30") == "До выхода курса осталось: 357 дней и 5 часов"

def test2():
	assert func("06.11.2022 12:00") == "До выхода курса осталось: 2 дня"

def test3():
	assert func("16.11.2021 06:30") == "До выхода курса осталось: 357 дней и 5 часов"