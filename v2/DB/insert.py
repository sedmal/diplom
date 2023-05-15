from DB.select import select_nalichie_users_DB


# СДЕЛАНО добавление множества либо одного пользователя
def add_users(connection,dict):
    for key in dict.keys():
        data = select_nalichie_users_DB(connection,key)
        if data == []:
            value = f'''insert into users('''
            columns = ''''''
            values = f""""""
            for key2 in dict[key].keys():
                if type(dict[key][key2]) == str:
                    if "'" in dict[key][key2]:
                        dict[key][key2] = dict[key][key2].replace("'",'"')
                columns += f'''"{key2}",'''
                values += f"""'{dict[key][key2]}',"""
            columns = columns[:len(columns)-1]
            values = values[:len(values)-1]
            value = value + columns + ') values (' + values + ');'
            connection.execute(value)
            print('пользователь добавлен в БД')
        else:
            print('пользователь есть в БД')

