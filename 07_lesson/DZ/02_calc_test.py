from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage


def test_form():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    calc_page = CalcPage(browser)
    # выставить дилэй
    calc_page.timer_set()
    # нажать на кнопки
    calc_page.push_butn_07()
    calc_page.push_butn_plus()
    calc_page.push_butn_08()
    calc_page.push_butn_eq()
    # проверка результата
    calc_page.waiter()
    assert "15" in calc_page.result()
    # выход
    browser.quit()
