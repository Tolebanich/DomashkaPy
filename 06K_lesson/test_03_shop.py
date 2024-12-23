from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://www.saucedemo.com/")
driver.implicitly_wait(15)
driver.find_element(
    By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(
    By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(
    By.CSS_SELECTOR, "#login-button").click()
driver.implicitly_wait(15)
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
driver.find_element(
    By.XPATH, "//a[@class='shopping_cart_link']").click()
driver.find_element(
    By.CSS_SELECTOR, "#checkout").click()
driver.find_element(
    By.XPATH, "//input[@id='first-name']").send_keys("Anatoly")
driver.find_element(
    By.XPATH, "//input[@id='last-name']").send_keys("Fedchenko")
driver.find_element(
    By.XPATH, "//input[@id='postal-code']").send_keys("830001")
driver.find_element(
    By.CSS_SELECTOR, "#continue").click()
total = driver.find_element(
    By.XPATH, "//div[@class='summary_total_label']"
    ).text
print(total)
driver.close()


def test_01():
    assert "Total: $58.29" == total
