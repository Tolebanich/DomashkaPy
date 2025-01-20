from selenium.webdriver.common.by import By
import allure


class FormPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(15)
        self._driver.maximize_window()

    @allure.step("Ввести имя {fname}")
    def input_first_name(self, fname: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='first-name']").send_keys(fname)

    @allure.step("Ввести фамилию {lname}")
    def input_last_name(self, lname: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='last-name']").send_keys(lname)

    @allure.step("Ввести адрес {address}")
    def input_address(self, address: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='address']").send_keys(address)

    @allure.step("Ввести почту {mail}")
    def input_email(self, mail: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='e-mail']").send_keys(mail)

    @allure.step("Ввести телефон {phone}")
    def input_phone(self, phone: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='phone']").send_keys(phone)

    @allure.step("Ввести индекс {zip}")
    def input_zip(self, zip: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='zip-code']").send_keys(zip)

    @allure.step("Ввести город {city}")
    def input_city(self, city: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='city']").send_keys(city)

    @allure.step("Ввести страну {country}")
    def input_country(self, country: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='country']").send_keys(country)

    @allure.step("Ввести должность {job}")
    def input_job(self, job: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='job-position']").send_keys(job)

    @allure.step("Ввести компанию {company}")
    def input_company(self, company: str):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='company']").send_keys(company)

    @allure.step("Нажать кнопку 'Submit'")
    def click_subm(self):
        self._driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
            ).click()

    @allure.step("Проверить поле 'ZIP'")
    def zip_check(self) -> str:
        zip = self._driver.find_element(
            By.XPATH, "//div[@id='zip-code']").get_attribute("class")
        return zip

    @allure.step("Проверить поле 'First Name'")
    def firstn_check(self) -> str:
        fname = self._driver.find_element(
            By.XPATH, "//div[@id='first-name']").get_attribute("class")
        return fname

    @allure.step("Проверить поле 'Last Name'")
    def last_name_check(self) -> str:
        lname = self._driver.find_element(
            By.XPATH, "//div[@id='last-name']").get_attribute("class")
        return lname

    @allure.step("Проверить поле 'Address'")
    def address_check(self) -> str:
        address = self._driver.find_element(
            By.XPATH, "//div[@id='address']").get_attribute("class")
        return address

    @allure.step("Проверить поле 'E-mail'")
    def email_check(self) -> str:
        email = self._driver.find_element(
            By.XPATH, "//div[@id='e-mail']").get_attribute("class")
        return email

    @allure.step("Проверить поле 'Phone'")
    def phone_check(self) -> str:
        phone = self._driver.find_element(
            By.XPATH, "//div[@id='phone']").get_attribute("class")
        return phone

    @allure.step("Проверить поле 'City'")
    def city_check(self) -> str:
        city = self._driver.find_element(
            By.XPATH, "//div[@id='city']").get_attribute("class")
        return city

    @allure.step("Проверить поле 'Country'")
    def country_check(self) -> str:
        country = self._driver.find_element(
            By.XPATH, "//div[@id='country']").get_attribute("class")
        return country

    @allure.step("Проверить поле 'Job'")
    def job_check(self) -> str:
        job = self._driver.find_element(
            By.XPATH, "//div[@id='job-position']").get_attribute("class")
        return job

    @allure.step("Проверить поле 'Company'")
    def company_check(self) -> str:
        company = self._driver.find_element(
            By.XPATH, "//div[@id='company']").get_attribute("class")
        return company
