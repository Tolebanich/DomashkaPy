from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()

blue_button = "button.btn.btn-primary"
driver.find_element(By.CSS_SELECTOR, blue_button ).click()
