from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self._driver = browser

    def get(self):
        self._driver.get("https://www.labirint.ru/cart/")

    def get_counter(self):
        txt = self.driver.find_element(By.CSS_SELECTOR, '#basket-default-prod-count2').text
        return int(txt)