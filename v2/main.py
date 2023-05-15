from app.photo import photos_getMessagesUploadServer
from app.main_app import (search_people_and_photos,
                          cur_user)

from DB.create import creat_all_tables
from DB.insert import (add_users)
from DB.select import (select_one_user_for_view)


from functions import (event_listen,
                       write_msg,
                       prepare_photo)

from pprint import pprint


from DB.connect import connection


creat_all_tables(connection)

favorites = 1
black_list = 1

while True:
    message, user_id = event_listen()
    sex, city, dict_cur_user = cur_user(user_id)
    add_users(connection,dict_cur_user)
    age_at = 30
    age_to = 40
    status = 6


    if message == "начать":
        name = dict_cur_user[user_id]['first_name']
        write_msg(user_id=user_id, message=f"""Привет, {name}! Введите 'поиск' для начала поиска анкет'""")


    elif message == "поиск":
        dict_all_persons = search_people_and_photos(sex, age_at, age_to, city, status)
        add_users_and_search_params(connection,dict_all_persons,sex,age_at,age_to,city,status)
        name = dict_cur_user[user_id]['first_name']
        write_msg(user_id, f"{name}, для просмотра анкет введите 'смотреть'")


    elif message == "смотреть":
        dict_for_view = select_search_params(connection,sex,age_at,age_to,city,status)#

        if dict_for_view == {}:
            write_msg(user_id, f"Записей для просмотра больше нет. Для повторного описка введите 'Поиск'")
        else:
            dict_one_persons = select_one_user_for_view(connection,dict_for_view[1])
            text, photo = prepare_photo(dict_one_persons)
            write_msg(user_id, text, photo)
            write_msg(user_id, "Для добавления в избранное введите 'добавить в избранное', для добавления в черный список введите 'добавить в черный список'")
            id_in_list = dict_one_persons['id']



    elif message == "пока":
        write_msg(user_id, "Пока((")


    else:
        write_msg(user_id, "Не поняла вашего ответа...")