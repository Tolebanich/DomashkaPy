from sqlalchemy import create_engine, text


db = create_engine("postgresql://postgres:Neo1neo2neo3@localhost:5432/QADZ")


def test_insert():
    insert_sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (153, 'Nature_test')")
    select_sql = text("SELECT * FROM subject WHERE subject_id = 153")
    delete_sql = text("DELETE FROM subject WHERE subject_id = 153")

    with db.connect() as connection:
        connection.execute(insert_sql)
        result = connection.execute(select_sql).fetchone()
        assert result is not None
        assert result['subject_id'] == 153
        assert result['subject_title'] == 'Nature_test'
        connection.execute(delete_sql)

def test_update():
    insert_sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (154, 'Nature_test')")
    update_sql = text("UPDATE subject SET subject_title = 'Nature_test_update' WHERE subject_id = 154")
    select_sql = text("SELECT * FROM subject WHERE subject_id = 154")
    delete_sql = text("DELETE FROM subject WHERE subject_id = 154")

    with db.connect() as connection:
        connection.execute(insert_sql)
        connection.execute(update_sql)
        result = connection.execute(select_sql).fetchone()
        assert result is not None
        assert result['subject_id'] == 154
        assert result['subject_title'] == 'Nature_test_update'
        connection.execute(delete_sql)

def test_delete():
    insert_sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (155, 'Nature_test')")
    delete_sql = text("DELETE FROM subject WHERE subject_id = 155")
    select_sql = text("SELECT * FROM subject WHERE subject_id = 155")

    with db.connect() as connection:
        connection.execute(insert_sql)
        connection.execute(delete_sql)
        result = connection.execute(select_sql).fetchone()
        assert result is None