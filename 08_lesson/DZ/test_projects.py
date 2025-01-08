from data.projects_api import projects_api

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
    
def test_find_by_id():
    new_proj = api.create_proj("Kadia_id_test") # Создаём новый проект
    need_id = new_proj['id'] # Сохраняем айди нового проекта
    comp_by_id = api.search_by_id(need_id) # Ищем по новому айди создался ли проект
    assert comp_by_id["title"] == "Kadia_id_test"
    
def test_edit():
    new_proj = api.create_proj("Kadia_edit_test") # Создаём новый проект
    change_id = new_proj['id'] # Сохраняем айди нового проекта
    api.change_proj(change_id, "No more Kadia")
    changed = api.search_by_id(change_id)["title"]
    assert changed == "No more Kadia"