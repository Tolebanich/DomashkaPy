from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage
import allure


@allure.title("Тест калькулятора")
@allure.description("Проверка работы калькулятора с ожиданием таймера в 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Тестирование калькулятора")
def test_form():
    with allure.step("Открыть браузер и перейти на страницу калькулятора"):
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        calc_page = CalcPage(browser)
    with allure.step("Поставить таймер на 45 секунд"):
        calc_page.timer_set()
    with allure.step("Ввести данные и получить результат"):
        calc_page.push_butn_07()
        calc_page.push_butn_plus()
        calc_page.push_butn_08()
        calc_page.push_butn_eq()
    with allure.step("Подождать 50 секунд и проверить результат"):
        calc_page.waiter(50)
        assert "15" in calc_page.result()
    with allure.step("Закрыть браузер"):
        browser.quit()
