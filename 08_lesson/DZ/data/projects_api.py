import requests


class projects_api:
    def __init__(self, url) -> None:
        self.url = url

    # Получить список проектов
    def get_proj_list(self):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "
        }
        project_l = requests.get(self.url + "/projects", headers=my_headers)
        response = requests.get(self.url + "/projects", headers=my_headers)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        return project_l.json()

    def create_proj(self, title):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "
        }
        my_json = {
            "title": title,
            "users": {"bf1b3cd7-3ea0-4ba0-8930-0a0bd8cf69e0": "admin"}
        }
        project_l = requests.post(self.url + "/projects", json=my_json, headers=my_headers)
        response = requests.get(self.url + "/projects", headers=my_headers)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        return project_l.json()

    def search_by_id(self, id_proj):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "
        }
        search_by = requests.get(f"{self.url}/projects/{id_proj}", headers=my_headers)
        response = requests.get(self.url + "/projects", headers=my_headers)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        return search_by.json()

    def change_proj(self, id_proj, new_name):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "
        }
        body = {
            "title": new_name
        }
        edit = requests.put(f"{self.url}/projects/{id_proj}", json=body, headers=my_headers)
        response = requests.get(self.url + "/projects", headers=my_headers)
        assert response.status_code == 200, f"Ошибка: {response.status_code}"
        return edit.json()

    def get_proj_list_neg(self):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer"
        }
        project_l = requests.get(self.url + "/projects", headers=my_headers)
        response = requests.get(self.url + "/projects", headers=my_headers)
        assert response.status_code == 401, f"Ошибка: {response.status_code}"
        return project_l.json()

    def create_proj_neg_tok(self, title):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer"
        }
        my_json = {
            "title": title,
            "users": {"bf1b3cd7-3ea0-4ba0-8930-0a0bd8cf69e0": "admin"}
        }
        project_l = requests.post(self.url + "/projects", json=my_json, headers=my_headers)
        response = requests.get(self.url + "/projects", headers=my_headers)
        assert response.status_code == 401, f"Ошибка: {response.status_code}"
        return project_l.json()

    def search_by_id_neg(self, id_proj):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "
        }
        search_by = requests.get(
            f"{self.url}/projects/{id_proj}", headers=my_headers
            )
        response = requests.get(self.url + f"/projects/{id_proj}", headers=my_headers)
        assert response.status_code == 404, f"Ошибка: {response.status_code}"
        return search_by.json()

    def change_proj_neg(self, id_proj, new_name):
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "
        }
        body = {
            "title": new_name
        }
        edit = requests.put(
            f"{self.url}/projects/{id_proj}", json=body, headers=my_headers
            )
        response = requests.get(self.url + f"/projects/{id_proj}", headers=my_headers)
        assert response.status_code == 404, f"Ошибка: {response.status_code}"
        return edit.json()
