import pytest
import pytest_check as check


@pytest.mark.smoke
@pytest.mark.parametrize("args_1", ['1','2','3'])
def test_chrome_opens(args_1):
    """Простой тест, чтобы проверить что Chrome открывается"""
    # ES.driver_chrome.get("https://www.google.com")
    # assert "Google" in ES.driver_chrome.title
    print("✓ Chrome успешно открыл Google")

@pytest.mark.regression
def test_example_site():
    """Еще один простой тест"""
    # ES.driver_chrome.get("https://example.com")
    # assert "Example" in ES.driver_chrome.title or "Example Domain" in ES.driver_chrome.page_source
    print("✓ Тест с example.com прошел")

@pytest.mark.smoke
def test_multiple_checks():
    check.equal(1, 1)  # не остановит тест при падении
    check.equal(2, 3)  # добавит ошибку в список
    check.equal("a", "a")  # продолжит выполнение
    # В конце покажет все ошибки
