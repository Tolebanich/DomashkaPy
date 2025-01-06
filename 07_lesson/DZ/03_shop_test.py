from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.swag_labs.LogPage import LoginPage
from pages.swag_labs.ShopPage import ShopPage


def test_form():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    log_page = LoginPage(browser)
    shop_page = ShopPage(browser)
    # Залогиниться
    log_page.authorise_pass("standard_user", "secret_sauce")
    # Выбрать товары
    shop_page.add_goods()
    # перейти в корзину
    shop_page.checkout()
    # ввести данные
    shop_page.fill_fields("Anatoly", "Fedchenko", "830001")
    # проверить стоимость
    shop_page.check_price()
    assert "Total: $58.29" == shop_page.check_price()
    browser.quit()
