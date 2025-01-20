from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.swag_labs.LogPage import LoginPage
from pages.swag_labs.ShopPage import ShopPage
import allure


@allure.title("Тест магазина Swag Labs")
@allure.description("Проверка работы каталога на добавление товара и покупке в корзине")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Тестирование магазина")
def test_form():
    with allure.step("Открыть браузер и перейти на страницу магазина"):
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        log_page = LoginPage(browser)
        shop_page = ShopPage(browser)
    log_page.authorise_pass("standard_user", "secret_sauce")
    shop_page.add_goods()
    shop_page.checkout()
    shop_page.fill_fields("Anatoly", "Fedchenko", "830001")
    shop_page.check_price()
    with allure.step("Проверить ожидаемую цену в корзине и фактическую"):
        assert "Total: $58.29" == shop_page.check_price()
    with allure.step("Закрыть браузер"):
        browser.quit()
