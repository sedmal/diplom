# выборка одного аккаунта для просмотра
def select_one_user_for_view(connection,bd_id):
    table = 'users'
    column1 = 'bd_id'
    value = f"""SELECT * FROM {table} WHERE {column1}={bd_id};"""
    data = connection.execute(value).fetchall()[0]
    return {'bd_id' : data[0],
            'id' : data[1],
            'first_name' : data[2],
            'last_name' : data[3]
            }
