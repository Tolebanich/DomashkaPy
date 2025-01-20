import allure
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable

api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

@allure.id("SKYPRO-1")
@allure.story("Получение списка компаний")
@allure.epic("Компании")
@allure.feature("READ")
@allure.title("Получение полного списка организаций")
@allure.severity("blocker")
def test_get_companies():
    api_result = api.get_company_list()
    with allure.step("получить список компаний из БД"):
        db_result = db.get_companies()

    with allure.step("Проверить, что списки равны"):
        assert len(api_result) == len(db_result)

@allure.id("SKYPRO-2")
@allure.story("Получение списка активных компаний")
@allure.epic("Компании")
@allure.feature("READ")
@allure.title("Получение списка активных организаций")
@allure.description("Запрос организаций с пар-м active=true")
def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={"is_active": "true"})
    db_list = db.get_active_companies()
    assert len(filtered_list) == len(db_list)

@allure.id("SKYPRO-3")
@allure.story("ДОбавление новых компаний")
@allure.epic("Компании")
@allure.feature("READ")
@allure.title("Создание организации")
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)
    with allure.step("Создать организацию"):
        with allure.step("Сгенерить название"):
            name = "Autotest"
            descr = "Descr"
        with allure.step("Вызвать API-метод для создания"):
            result = api.create_company(name, descr)
            new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1
    for company in body:
            if company["id"] == new_id:
                assert company["name"] == name
                assert company["description"] == descr
                assert company["id"] == new_id
