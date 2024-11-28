from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/login')

login = driver.find_element(By.CSS_SELECTOR, 'input#username')
login.send_keys('tomsmith')
password = driver.find_element(By.CSS_SELECTOR, 'input#password')
password.send_keys('SuperSecretPassword!')
driver.find_element(By.CSS_SELECTOR, "button[class='radius']").click()

driver.close()