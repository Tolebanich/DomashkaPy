import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class CompanyTable:
    __scripts = {
        "select": "select * from company where deleted_at is null",
        "select only active": "select * from company where \"is_active\" = true  and deleted_at is null",
        "delete by id": text("delete from company where id =:id_to_delete")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    @allure.step("БД. Запросить список организаций")
    def get_companies(self):
        query = self.db.execute(self.__scripts["select"])
        sql = str(query.context.cursor.query)
        return query.fetchall()

    @allure.step("БД. Запросить список активных организаций")
    def get_active_companies(self):
        return self.__db.execute(self.__scripts["select only active"]).fetchall()

    @allure.step("БД. Удалить организацию по {id}")
    def delete(self, id):
        params = {'id_to_delete' : id}
        query = self.__db.execute(self.__scripts["delete by id"], parameters = params)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)