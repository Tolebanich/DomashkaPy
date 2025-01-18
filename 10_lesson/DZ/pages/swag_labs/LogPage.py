from selenium.webdriver.common.by import By
import allure

class LoginPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(15)
        self._driver.maximize_window()

    @allure.step("Авторизация на сайте c логином '{login}' и паролем '{passw}'")
    def authorise_pass(self, login: str, passw: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(login)
        self._driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(passw)
        self._driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
