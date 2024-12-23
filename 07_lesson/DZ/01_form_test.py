from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.FormPage import FormPage


def test_form():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    form_page = FormPage(browser)

    # Заполнение форм

    form_page.input_first_name("Иван")
    form_page.input_last_name("Петров")
    form_page.input_address("Ленина, 55-3")
    form_page.input_email("test@skypro.com")
    form_page.input_phone("+7985899998787")
    form_page.input_zip("")
    form_page.input_city("Москва")
    form_page.input_country("Россия")
    form_page.input_job("QA")
    form_page.input_company("SkyPro")
    form_page.click_subm()

    # Проверка

    assert "danger" in form_page.zip_check()
    assert "success" in form_page.firstn_check()
    assert "success" in form_page.last_name_check()
    assert "success" in form_page.address_check()
    assert "success" in form_page.email_check()
    assert "success" in form_page.phone_check()
    assert "success" in form_page.city_check()
    assert "success" in form_page.country_check()
    assert "success" in form_page.job_check()
    assert "success" in form_page.company_check()

    # закрыть,к чертям.

    browser.quit()
