from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()


for i in range(0, 5):
    driver.find_element(By.XPATH, ("//button[text()='Add Element']") ).click()

delButton = driver.find_elements(By.XPATH, ("//button[text()='Delete']") )
print(len(delButton))

