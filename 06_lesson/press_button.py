from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
driver.implicitly_wait(40)
ajax = driver.find_element(By.CSS_SELECTOR, "p[class='bg-success']")
print(ajax.text)

driver.quit()
