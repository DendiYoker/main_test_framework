import allure
from Tools.tools import story

@story('001')
@allure.description('Описание первого теста')
def test_001():
    with allure.step("шаг 1"):
        allure.attach(name='тестируем приклад', body='какое нибудь тело', attachment_type=allure.attachment_type.TEXT)
    print(f"Запущен тест № 1")

@story('002')
@allure.description('Описание второго теста')
def test_002():
    print(f"Запущен тест № 2")

