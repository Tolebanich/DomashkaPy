from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, browser):
        self._driver = browser

    def add_goods(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def checkout(self):
        self._driver.find_element(
            By.XPATH, "//a[@class='shopping_cart_link']").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()

    def fill_fields(self, fname, lname, zip):
        self._driver.find_element(
            By.XPATH, "//input[@id='first-name']").send_keys(fname)
        self._driver.find_element(
            By.XPATH, "//input[@id='last-name']").send_keys(lname)
        self._driver.find_element(
            By.XPATH, "//input[@id='postal-code']").send_keys(zip)
        self._driver.find_element(
            By.CSS_SELECTOR, "#continue").click()

    def check_price(self):
        total = self._driver.find_element(
            By.XPATH, "//div[@class='summary_total_label']"
            ).text
        return total
