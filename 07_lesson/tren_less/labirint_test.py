from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    "name": "cookie_policy",
    "value": "1"
}
browser = None

def open_labyrint():
    # Перейти на сайт лабиринта
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(15)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    # найти все книги по слову питон
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

def add_books():
    # добавить все книги в корзину и посчитать,сколько их
    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, ("a._btn.btn-tocart.buy-link"))
    
    counter=0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    print(counter)
    return counter

def go_to_cart():
    #Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # проверить счётчик товаров. Должен быть равен числу нажатий
    #Получить текущее значение
    txt = browser.find_element(By.CSS_SELECTOR, '#basket-default-prod-count2').text
    return int(txt)

def close_driver():
    browser.quit()

def test_cart_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    open_labyrint()
    search("python")    
    
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    
    
    #Сравнить с counter
    assert added == cart_counter
    close_driver()
