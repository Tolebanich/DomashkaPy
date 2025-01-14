from data.projects_api import projects_api
import requests

api = projects_api("https://ru.yougile.com/api-v2")

def test_get_proj_list():
    proj_id = api.get_proj_list()
    assert len(proj_id) > 0
    
def test_create_proj():
    body = api.get_proj_list() # Получаем список проэктов
    before = len(body["content"]) # сохраняем длину
    new_proj = api.create_proj("Kadia") #Возвращается айди.
    id_new = new_proj["id"] # Сохраняем новый айди
    body = api.get_proj_list() # Получаем новый список проектов
    after = len(body["content"]) # Сохраняем новую длину
    assert id_new > str(0)
    assert before < after
    assert body['content'][-1]['title'] == "Kadia"
    
# def test_find_by_id():
#     new_proj = api.create_proj("Kadia_id_test") # Создаём новый проект
#     need_id = new_proj['id'] # Сохраняем айди нового проекта
#     comp_by_id = api.search_by_id(need_id) # Ищем по новому айди создался ли проект
#     assert comp_by_id["title"] == "Kadia_id_test"
    
def test_edit():
    new_proj = api.create_proj("Kadia_edit_test") # Создаём новый проект
    change_id = new_proj['id'] # Сохраняем айди нового проекта
    api.change_proj(change_id, "No more Kadia")
    changed = api.search_by_id(change_id)["title"]
    assert changed == "No more Kadia"


def test_get_list_neg():
    proj_id = api.get_proj_list_neg() # Проверка на запрос при отсутствии токена авторизации
    assert len(proj_id) > 0
    
def test_create_proj_neg_no_title():
    response = api.create_proj("")  # Пустой заголовок
    assert response["error"], "Ожидалась ошибка при создании проекта без названия"

def test_create_proj_neg():
    body = api.get_proj_list() # Получаем список проектов
    before = len(body["content"]) # сохраняем длину
    api.create_proj_neg_tok("Kadia") #Создать проект без токена
    body = api.get_proj_list() # Получаем новый список проектов
    after = len(body["content"]) # Сохраняем новую длину
    assert before == after # Проверяем что ничего не создалось

def test_find_by_id_neg():
    api.search_by_id_neg("id") # Ищем по пустому айди
    
def test_change_neg():
    api.change_proj_neg(123, "No more Kadia") # Посылаем запрос на поиск по айди,по неправильному айди