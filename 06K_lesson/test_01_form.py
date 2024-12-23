from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(
    By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
last_name = driver.find_element(
    By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
address = driver.find_element(
    By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
email = driver.find_element(
    By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
pnumber = driver.find_element(
    By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
zcode = driver.find_element(
    By.CSS_SELECTOR, "input[name='zip-code']")
city = driver.find_element(
    By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
country = driver.find_element(
    By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
job = driver.find_element(
    By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
company = driver.find_element(
    By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


def test_01():
    assert "alert-danger" in driver.find_element(
        By.XPATH, "//div[@id='zip-code']").get_attribute("class")


def test_02():
    assert "alert-success" in driver.find_element(
        By.XPATH, "//div[@id='first-name']").get_attribute("class")


def test_03():
    assert "alert-success" in driver.find_element(
        By.XPATH, "//div[@id='last-name']").get_attribute("class")


def test_04():
    assert "alert-success" in driver.find_element(
        By.XPATH, "//div[@id='address']").get_attribute("class")


def test_05():
    assert "alert-success" in driver.find_element(
        By.XPATH, "//div[@id='e-mail']").get_attribute("class")


def test_06():
    assert "alert-success" in driver.find_element(
        By.XPATH, "//div[@id='phone']").get_attribute("class")


def test_07():
    assert "alert-success" in driver.find_element(
        By.XPATH, "//div[@id='city']").get_attribute("class")


def test_08():
    assert "alert-success" in driver.find_element(
        By.XPATH, "//div[@id='country']").get_attribute("class")


def test_09():
    assert "alert-success" in driver.find_element(
        By.XPATH, "//div[@id='job-position']").get_attribute("class")


def test_10():
    assert "alert-success" in driver.find_element(
        By.XPATH, "//div[@id='company']").get_attribute("class")
