"""
Тестовый файл для демонстрации ВСЕХ возможностей Allure
"""
import allure
import pytest
import logging
import time
from datetime import datetime
import json
import csv
from io import StringIO
import os
# Для демонстрации создаем "скриншот" программно
from PIL import Image, ImageDraw
import io

# ======================= 1. БАЗОВЫЕ ТЕСТЫ =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Базовые возможности")
class TestAllureBasics:

    @allure.story("Успешный тест")
    @allure.title("Тест с простым assert")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("smoke", "regression")
    def test_simple_assert(self):
        """Простой тест с assert"""
        with allure.step("Шаг 1: Подготовка данных"):
            expected = 10
            actual = 5 + 5

        with allure.step("Шаг 2: Проверка результата"):
            assert actual == expected, f"Ожидалось {expected}, получено {actual}"

        with allure.step("Шаг 3: Логирование результата"):
            allure.dynamic.description(f"Тест завершен в {datetime.now()}")

    @allure.story("Падающий тест")
    @allure.title("Тест с AssertionError")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_failing_assert(self):
        """Тест с преднамеренным падением"""
        with allure.step("Выполняем некорректную операцию"):
            result = 10 / 0  # ZeroDivisionError

        assert result == 10

    @allure.story("Пропущенный тест")
    @allure.title("Тест с пропуском")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.skip(reason="Фича еще в разработке")
    def test_skipped(self):
        """Пропущенный тест"""
        assert 1 == 2

    @allure.story("Сломанный тест")
    @allure.title("Тест с исключением")
    @allure.severity(allure.severity_level.NORMAL)
    def test_broken(self):
        """Тест с непредвиденным исключением"""
        raise ConnectionError("Сервер недоступен")


# ======================= 2. SOFT ASSERTIONS =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Soft Assertions")
class TestSoftAssertions:

    @allure.story("Множественные проверки")
    @allure.title("Тест с несколькими soft assertions")
    def test_multiple_soft_asserts(self):
        """Демонстрация soft assertions - все проверки выполняются"""
        errors = []

        with allure.step("Проверка 1: Математика"):
            try:
                assert 1 + 1 == 3, "Математика сломалась"
                allure.attach("✅ Проверка 1 пройдена", name="Результат", attachment_type=allure.attachment_type.TEXT)
            except AssertionError as e:
                errors.append(str(e))
                allure.attach(f"❌ {e}", name="Ошибка", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Проверка 2: Строки"):
            try:
                assert "hello".upper() == "HELLO", "Строки не совпадают"
                allure.attach("✅ Проверка 2 пройдена", name="Результат", attachment_type=allure.attachment_type.TEXT)
            except AssertionError as e:
                errors.append(str(e))

        with allure.step("Проверка 3: Список"):
            try:
                assert len([1, 2, 3, 4]) == 3, "Неверная длина списка"
                allure.attach("✅ Проверка 3 пройдена", name="Результат", attachment_type=allure.attachment_type.TEXT)
            except AssertionError as e:
                errors.append(str(e))

        with allure.step("Итоговая проверка"):
            if errors:
                error_message = "\n".join(errors)
                allure.attach(error_message, name="Все ошибки", attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"Найдены ошибки:\n{error_message}")


# ======================= 3. ВЛОЖЕННЫЕ ШАГИ И СЕКЦИИ =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Вложенные шаги")
class TestNestedSteps:

    @allure.story("Сложный процесс")
    @allure.title("Тест с вложенными шагами")
    def test_nested_steps(self):
        """Демонстрация вложенных шагов"""

        @allure.step("Внешний шаг: {step_name}")
        def outer_step(step_name):
            with allure.step(f"Внутренний шаг 1 в {step_name}"):
                time.sleep(0.1)

            with allure.step(f"Внутренний шаг 2 в {step_name}"):
                time.sleep(0.1)

        with allure.step("Начало сложного процесса"):
            outer_step("первая часть")
            outer_step("вторая часть")

            with allure.step("Секция с подшагами"):
                for i in range(3):
                    with allure.step(f"Итерация {i + 1}"):
                        time.sleep(0.05)


# ======================= 4. АТТАЧМЕНТЫ (ВЛОЖЕНИЯ) =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Аттачменты")
class TestAttachments:

    @allure.story("Разные типы вложений")
    @allure.title("Тест с файлами аттачментами")
    def test_attachments(self):
        """Демонстрация всех типов аттачментов"""

        # 1. Текстовый файл
        text_content = "Это текстовый файл\nСодержащий несколько строк\nДля демонстрации"
        allure.attach(text_content, name="text_file.txt", attachment_type=allure.attachment_type.TEXT)

        # 2. JSON файл
        json_data = {
            "test": "данные",
            "version": 1.0,
            "items": ["item1", "item2", "item3"]
        }
        allure.attach(json.dumps(json_data, indent=2), name="config.json", attachment_type=allure.attachment_type.JSON)

        # 3. CSV файл
        csv_data = "id,name,value\n1,Item1,100\n2,Item2,200\n3,Item3,300"
        allure.attach(csv_data, name="data.csv", attachment_type=allure.attachment_type.CSV)

        # 4. HTML файл
        html_content = """
        <html>
            <body>
                <h1>HTML Report</h1>
                <p>This is <b>HTML</b> content</p>
                <table border="1">
                    <tr><th>ID</th><th>Name</th></tr>
                    <tr><td>1</td><td>Test</td></tr>
                </table>
            </body>
        </html>
        """
        allure.attach(html_content, name="report.html", attachment_type=allure.attachment_type.HTML)

        # 5. XML файл
        xml_content = '<?xml version="1.0"?><root><item id="1">Test</item></root>'
        allure.attach(xml_content, name="data.xml", attachment_type=allure.attachment_type.XML)

        # 6. URI (сслыка)
        allure.attach("https://allurereport.org", name="Allure Website",
                      attachment_type=allure.attachment_type.URI_LIST)


# ======================= 5. ПАРАМЕТРИЗАЦИЯ И ДАННЫЕ =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Параметризация")
class TestParameterization:

    @pytest.mark.parametrize("username,password,expected", [
        ("admin", "admin123", True),
        ("user", "user123", True),
        ("guest", "wrong", False),
        ("", "", False)
    ])
    @allure.story("Параметризованные тесты")
    @allure.title("Авторизация пользователя {username}")
    def test_login_parameters(self, username, password, expected):
        """Параметризованный тест с разными данными"""
        allure.dynamic.description(f"Проверка логина для пользователя: {username}")

        # Добавляем параметры в отчет
        allure.attach(f"Username: {username}\nPassword: {password}\nExpected: {expected}",
                      name="Test Data", attachment_type=allure.attachment_type.TEXT)

        # Симуляция логики авторизации
        is_valid = len(username) > 0 and len(password) > 0 and "123" in password

        assert is_valid == expected, f"Для {username} ожидалось {expected}, получено {is_valid}"


# ======================= 6. ЛИНКИ И ССЫЛКИ =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Ссылки и интеграции")
class TestLinks:

    @allure.story("Ссылки на внешние системы")
    @allure.title("Тест с интеграциями")
    @allure.link("https://github.com/allure-framework/allure-python", name="Allure Python")
    @allure.issue("BUG-123", "https://jira.example.com/browse/BUG-123")
    @allure.testcase("TC-456", "https://testrail.example.com/index.php?/cases/view/456")
    def test_with_links(self):
        """Тест со ссылками на внешние системы"""
        allure.link("https://pytest.org", name="Pytest Documentation")

        # Динамическое добавление ссылок
        if False:  # В реальном тесте условие
            allure.issue("BUG-999", "Новая найденная ошибка")

        assert True


# ======================= 7. КАТЕГОРИИ И МЕТКИ =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Категории и теги")
class TestCategories:

    @allure.story("Разные категории тестов")
    @allure.title("Продуктовый тест")
    @allure.tag("product", "e2e")
    def test_product_category(self):
        """Тест с продуктовыми тегами"""
        assert True

    @allure.story("Технические тесты")
    @allure.title("Технический тест")
    @allure.tag("technical", "integration")
    def test_technical_category(self):
        """Тест с техническими тегами"""
        assert True


# ======================= 8. КАСТОМНЫЕ ДАННЫЕ И МЕТАИНФОРМАЦИЯ =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Кастомные данные")
class TestCustomData:

    @allure.story("Пользовательские данные")
    @allure.title("Тест с кастомной информацией")
    def test_custom_data(self):
        """Добавление кастомных данных в отчет"""

        # Добавляем кастомные поля
        allure.dynamic.title(f"Тест выполнен в {datetime.now().strftime('%H:%M:%S')}")

        # Можем динамически менять описание
        allure.dynamic.description("""
        ## Кастомное описание теста

        Это тест с:
        - Кастомным описанием
        - Динамическими данными
        - Markdown разметкой

        **Результат:** ожидается успех
        """)

        # Добавляем свои метки
        allure.dynamic.tag("custom", "demo", "dynamic")

        # Добавляем свои ссылки
        allure.dynamic.link("https://example.com", name="Example")

        assert True


# ======================= 9. ТЕСТ С ОЖИДАНИЕМ И ТАЙМАУТОМ =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Тайминги")
class TestTimings:

    @allure.story("Долгий тест")
    @allure.title("Тест с ожиданием")
    def test_with_wait(self):
        """Тест с имитацией долгой операции"""
        with allure.step("Долгая операция 1"):
            time.sleep(1.5)
            allure.attach("Операция 1 завершена", name="Статус", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Долгая операция 2"):
            time.sleep(0.8)
            allure.attach("Операция 2 завершена", name="Статус", attachment_type=allure.attachment_type.TEXT)

        assert True


# ======================= 10. ТЕСТ С ЛОГИРОВАНИЕМ =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Логирование")
class TestLogging:

    @allure.story("Логи")
    @allure.title("Тест с логами")
    def test_with_logs(self):
        """Тест с добавлением логов в отчет"""

        # Создаем логгер
        logger = logging.getLogger(__name__)

        with allure.step("Логирование разных уровней"):
            # Эмулируем логи
            allure.attach("DEBUG: Начало выполнения теста", name="log", attachment_type=allure.attachment_type.TEXT)
            allure.attach("INFO: Открываем браузер", name="log", attachment_type=allure.attachment_type.TEXT)
            allure.attach("WARNING: Медленный ответ от сервера", name="log",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach("ERROR: Элемент не найден", name="log", attachment_type=allure.attachment_type.TEXT)

            # Можно прикрепить логи как файл
            logs = """2024-01-15 10:30:15 INFO - Starting test
            2024-01-15 10:30:16 DEBUG - Opening browser
            2024-01-15 10:30:17 INFO - Navigating to URL
            2024-01-15 10:30:20 WARNING - Slow response detected
            2024-01-15 10:30:22 INFO - Test completed"""

            allure.attach(logs, name="test.log", attachment_type=allure.attachment_type.TEXT)

            assert True


# ======================= 11. СКРИНШОТЫ И ВИЗУАЛЬНЫЕ ДАННЫЕ =======================
@allure.epic("Демонстрация Allure")
@allure.feature("Скриншоты и графика")
class TestScreenshots:

    @allure.story("Скриншоты")
    @allure.title("Тест со скриншотами (симуляция)")
    def test_with_screenshots(self):
        """Демонстрация скриншотов (в реальном тесте с Selenium)"""

        # В реальном Selenium тесте:
        # driver.save_screenshot("screenshot.png")
        # with open("screenshot.png", "rb") as f:
        #     allure.attach(f.read(), name="Скриншот", attachment_type=allure.attachment_type.PNG)

        # Создаем тестовое изображение
        img = Image.new('RGB', (800, 600), color='white')
        d = ImageDraw.Draw(img)
        d.text((50, 50), "Allure Screenshot Demo", fill='black')
        d.rectangle([100, 100, 700, 500], outline='red', width=5)

        # Сохраняем в байты
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')

        # Прикрепляем к отчету
        allure.attach(img_bytes.getvalue(), name="Пример скриншота", attachment_type=allure.attachment_type.PNG)

        # Также можно прикрепить несколько скриншотов
        img2 = Image.new('RGB', (400, 300), color='lightblue')
        d2 = ImageDraw.Draw(img2)
        d2.text((50, 50), "Дополнительный скриншот", fill='black')

        img2_bytes = io.BytesIO()
        img2.save(img2_bytes, format='PNG')
        allure.attach(img2_bytes.getvalue(), name="Дополнительный скриншот", attachment_type=allure.attachment_type.PNG)
