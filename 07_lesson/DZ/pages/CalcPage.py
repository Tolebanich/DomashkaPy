from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(15)
        self._driver.maximize_window()

    def timer_set(self):
        field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        field.clear()
        field.send_keys("45")

    def push_butn_07(self):
        self._driver.find_element(
            By.XPATH, "//span[@class='btn btn-outline-primary'][1]"
            ).click()

    def push_butn_plus(self):
        self._driver.find_element(
            By.XPATH, "//span[@class='operator btn btn-outline-success'][1]"
        ).click()

    def push_butn_08(self):
        self._driver.find_element(
            By.XPATH, "//span[@class='btn btn-outline-primary'][2]"
            ).click()

    def push_butn_eq(self):
        self._driver.find_element(
            By.XPATH, "//span[@class='btn btn-outline-warning']"
        ).click()

    def waiter(self):
        waiter = WebDriverWait(self._driver, 50)
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@class='top']/div[@class='screen']"), "15"
            ))

    def result(self):
        res = self._driver.find_element(
            By.XPATH, "//div[@class='top']/div[@class='screen']"
        ).text
        return res
