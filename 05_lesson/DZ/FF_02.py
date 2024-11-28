from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/inputs')

search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
search_input.send_keys('1000')
search_input.clear()
search_input.send_keys('999')

driver.close()

