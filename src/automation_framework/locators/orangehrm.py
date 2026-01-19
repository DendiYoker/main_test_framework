from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class Orangehrm:
    class AuthorizationPage:
        url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        ЛОГИН = [By.XPATH, "//input[@name='username']"]
        ПАРОЛЬ = [By.XPATH, "//input[@name='password']"]
        КНОПКА_LOGIN = [By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main "
                                  "orangehrm-login-button']"]
