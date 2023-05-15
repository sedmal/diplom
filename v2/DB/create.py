from DB.connect import connection

def create_table_users(connection):
    value = """CREATE TABLE IF NOT EXISTS users (
                                 bd_id serial PRIMARY KEY,
                                 id INTEGER NULL,
                                 first_name varchar(30) NOT NULL,
                                 last_name varchar(30) NOT NULL
                                 );
                                 """
    connection.execute(value)

def creat_all_tables(connection):
    create_table_users(connection)
