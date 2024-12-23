from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/entry_ad')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ("/html[@class='no-js']/body/div[@class='row'][2]/div[@id='content']/div[@id='modal']/div[@class='modal']/div[@class='modal-footer']/p"),)))

driver.find_element(By.XPATH, ("/html[@class='no-js']/body/div[@class='row'][2]/div[@id='content']/div[@id='modal']/div[@class='modal']/div[@class='modal-footer']/p"),).click()

driver.close()
