from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(15)
        self._driver.maximize_window()

    def input_first_name(self, fname):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='first-name']").send_keys(fname)

    def input_last_name(self, lname):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='last-name']").send_keys(lname)

    def input_address(self, address):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='address']").send_keys(address)

    def input_email(self, mail):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='e-mail']").send_keys(mail)

    def input_phone(self, phone):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='phone']").send_keys(phone)

    def input_zip(self, zip):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='zip-code']").send_keys(zip)

    def input_city(self, city):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='city']").send_keys(city)

    def input_country(self, country):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='country']").send_keys(country)

    def input_job(self, job):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='job-position']").send_keys(job)

    def input_company(self, company):
        self._driver.find_element(
            By.CSS_SELECTOR, "input[name='company']").send_keys(company)

    def click_subm(self):
        self._driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
            ).click()

    def zip_check(self):
        zip = self._driver.find_element(
            By.XPATH, "//div[@id='zip-code']").get_attribute("class")
        return zip

    def firstn_check(self):
        fname = self._driver.find_element(
            By.XPATH, "//div[@id='first-name']").get_attribute("class")
        return fname

    def last_name_check(self):
        lname = self._driver.find_element(
            By.XPATH, "//div[@id='last-name']").get_attribute("class")
        return lname

    def address_check(self):
        address = self._driver.find_element(
            By.XPATH, "//div[@id='address']").get_attribute("class")
        return address

    def email_check(self):
        email = self._driver.find_element(
            By.XPATH, "//div[@id='e-mail']").get_attribute("class")
        return email

    def phone_check(self):
        phone = self._driver.find_element(
            By.XPATH, "//div[@id='phone']").get_attribute("class")
        return phone

    def city_check(self):
        city = self._driver.find_element(
            By.XPATH, "//div[@id='city']").get_attribute("class")
        return city

    def country_check(self):
        country = self._driver.find_element(
            By.XPATH, "//div[@id='country']").get_attribute("class")
        return country

    def job_check(self):
        job = self._driver.find_element(
            By.XPATH, "//div[@id='job-position']").get_attribute("class")
        return job

    def company_check(self):
        company = self._driver.find_element(
            By.XPATH, "//div[@id='company']").get_attribute("class")
        return company
