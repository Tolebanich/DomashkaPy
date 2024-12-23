from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
field = driver.find_element(By.CSS_SELECTOR, "#delay")
field.clear()
field.send_keys("45")
driver.find_element(
    By.XPATH, "//span[@class='btn btn-outline-primary'][1]"
    ).click()
driver.find_element(
    By.XPATH, "//span[@class='operator btn btn-outline-success'][1]"
    ).click()
driver.find_element(
    By.XPATH, "//span[@class='btn btn-outline-primary'][2]"
    ).click()
driver.find_element(
    By.XPATH, "//span[@class='btn btn-outline-warning']"
    ).click()

waiter = WebDriverWait(driver, 50)
waiter.until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//div[@class='top']/div[@class='screen']"), "15"
        )
)


def test_res():
    assert "15" in driver.find_element(
        By.XPATH, "//div[@class='top']/div[@class='screen']"
        ).text
