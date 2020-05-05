import names
import rasbor
from MethodsOfDb import table, id_of_class, id_of_school, name_of_schools, classes, add_school, add_class


sessionStorage = {}
import pravila


def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        names.sessionStorage[user_id] = {
            'suggests': [
                "Разбор",
                "Добавление школы",
                "Добавление класса",
                "Расписание",
                "Правило",
                "Отстань!",
            ]
        }

        names.sessionStorage1[user_id] = {
                'table': {
                    'city': None,
                    'school': None,
                    'class': None
                }
        }

        res['response']['text'] = 'Привет! Я помогу тебе с учёбой.'
        res['response']['buttons'] = get_suggests(user_id)
        return
    if 'не стоит' in req['request']['original_utterance'].lower() or 'хватит' in req['request']['original_utterance'].lower():
        res['response']['text'] = "Ну ладно. Может ещё чем нибудь помочь?"
        names.city = False
        names.rasbor = False
        names.morf = False
        names.poSost = False
        names.zvbuk = False
        names.fonet = False
        names.cacChast = False
        names.morfemn = False
        names.rasspisanie = False
        names.raspisanie2 = False
        names.rasspisanie3 = False
        names.addschool = False
        names.addclass = False
        return
    if 'добавление класса' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Введите город, школу и класс, который хотите добавит через ";"'
        names.addclass = True
        return
    if 'добавление школы' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Введите город, адрес и название школы через ";"'
        names.addschool = True
        return
    if names.addclass:
        text = req['request']['original_utterance'].lower().split(';')
        if len(text) == 3:
            id = id_of_school(text[0], text[1])
            print(text[0], text[1])
            if id is None:
                res['response']['text'] = 'Похоже, вы пытаетесь добавить класс к несуществующей школе или данные введены неверно'
                return
            add_class(id, text[2], 0)
            res['response']['text'] = 'Класс добавлен, но до проверки на достоверность, отображаться он не будет'
            names.addclass = False
            return
        res['response']['text'] = 'Данные введены некорректно'
        return
    if names.addschool:
        text = req['request']['original_utterance'].lower().split(';')
        if len(text) == 3:
            add_school(text[2], text[0], text[1], 0)
            res['response']['text'] = 'Школа добавлена, но до проверки на достоверность, отображаться она не будет'
            names.addschool = False
            return
        res['response']['text'] = 'Данные введены некорректно'
        return

    if 'расписание' in req['request']['original_utterance'].lower() and names.rasspisanie is False:
        names.rasspisanie = True
        res['response']['text'] = 'Какой город?'
        return
    if names.rasspisanie is True and not names.raspisanie2 and not names.rasspisanie3\
            and names.sessionStorage1[user_id]['table']['city'] is not None\
            and req['request']['original_utterance'] not in [i[0] for i in name_of_schools(names.sessionStorage1[user_id]['table']['city'])]:
        res['response']['text'] = 'Какая-какая школа? Повтори ещё разок!'
        return
    if names.rasspisanie is True and not names.raspisanie2 and not names.rasspisanie3\
            and names.sessionStorage1[user_id]['table']['city'] is not None\
            and req['request']['original_utterance'] in [i[0] for i in name_of_schools(names.sessionStorage1[user_id]['table']['city'])]:
        names.raspisanie2 = True
        names.sessionStorage1[user_id]['table']['school'] = req['request']['original_utterance']
        res['response']['text'] = 'Какой класс?'
        return

    if names.raspisanie2 is True and names.sessionStorage1[user_id]['table']['school'] is not None and not names.rasspisanie3\
            and req['request']['original_utterance'] not in [i[0] for i in classes(id_of_school(names.sessionStorage1[user_id]['table']['city'], names.sessionStorage1[user_id]['table']['school'])[0])]:
        res['response']['text'] = 'Какой-какой класс? Повтори ещё разок!'
        return
    if names.raspisanie2 is True and names.sessionStorage1[user_id]['table']['school'] is not None and not names.rasspisanie3\
            and req['request']['original_utterance'] in [i[0] for i in classes(id_of_school(names.sessionStorage1[user_id]['table']['city'], names.sessionStorage1[user_id]['table']['school'])[0])]:
        names.rasspisanie3 = True

        schools_id = id_of_school(names.sessionStorage1[user_id]['table']['city'], names.sessionStorage1[user_id]['table']['school'])[0]
        names.sessionStorage1[user_id]['table']['class'] = req['request']['original_utterance']
        clas_id = id_of_class(schools_id, names.sessionStorage1[user_id]['table']['class'])[0]
        res['response']['text'] = str(table(clas_id))
        names.sessionStorage1[user_id]['table']['class'] = req['request']['original_utterance']
        city = names.sessionStorage1[user_id]['table']['city']
        sch = names.sessionStorage1[user_id]['table']['school']
        clas = names.sessionStorage1[user_id]['table']['class']
        names.rasspisanie = False
        names.raspisanie2 = False
        names.rasspisanie3 = False
        names.sessionStorage1[user_id]['table']['school'] = None
        names.sessionStorage1[user_id]['table']['class'] = None
        names.sessionStorage1[user_id]['table']['city'] = None

        return
    if names.rasspisanie is True and names.sessionStorage1[user_id]['table']['city'] is None\
            and not names.raspisanie2 and not names.rasspisanie3:
        print(1)
        city = get_city(req)
        print(2)
        if city is None:
            res['response']['text'] = 'Первый раз слышу об этом городе. Попробуй еще разок!'
            return
        names.sessionStorage1[user_id]['table']['city'] = city
        res['response']['text'] = 'Какая школа?'
        return

    if 'cпасибо' in req['request']['original_utterance'].lower() \
            or "благодар" in req['request']['original_utterance'].lower():
        res['response']['text'] = "Всегда пожалуйста. Ещё что то?"
        return

    if names.morf or names.cacChast:
        names.morf = False
        names.cacChast = False
        res['response']['text'] = rasbor.morfolog(req['request']['original_utterance'].
                                                  lower().replace("слова", "").split()[0])
        return
    if names.zvbuk or names.fonet:
        names.zvbuk = False
        names.fonet = False
        res['response']['text'] = rasbor.fonet(req['request']['original_utterance'].
                                               lower().replace("слова", "").split()[0])
        return
    if names.poSost or names.morfemn:
        names.poSost = False
        names.morfemn = False
        res['response']['text'] = rasbor.morfemn(req['request']['original_utterance'].
                                                 lower().replace("слова", "").split()[0])
        return

    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'морфологический' in req['request']['original_utterance'].lower() \
            and len(req['request']['original_utterance'].lower().split()) >= 4:
        res['response']['text'] = rasbor.morfolog(req['request']['original_utterance'].
                                                  lower().replace("слова", "").replace("разбор", "").
                                                  replace("морфологический", "").split()[0])
        names.morf = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'как части речи' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 4:
        res['response']['text'] = rasbor.morfolog(req['request']['original_utterance'].
                                                  lower().replace("слова", "").replace("разбор", "").
                                                  replace("как части речи", "").split()[0])
        names.cacChast = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'морфемный' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 4:
        res['response']['text'] = rasbor.morfemn(req['request']['original_utterance'].
                                                 lower().replace("слова", "").replace("разбор", "").
                                                 replace("морфемный", "").split()[0])
        names.morfemn = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'по составу' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 4:
        res['response']['text'] = rasbor.morfemn(req['request']['original_utterance'].
                                                 lower().replace("слова", "").replace("разбор", "").
                                                 replace("по составу", "").split()[0])
        names.poSost = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'фонетический' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 4:
        res['response']['text'] = rasbor.fonet(req['request']['original_utterance']
                                               .lower().replace("слова", "").
                                               replace("разбор", "").replace("фонетический", "").split()[0])
        names.fonet = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'звуко-буквенный' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 4:
        res['response']['text'] = rasbor.fonet(req['request']['original_utterance']
                                               .lower().replace("слова", "").
                                               replace("разбор", "").replace("звуко-буквенный", "").split()[0])
        names.zvbuk = False
        names.rasbor = False
        return

    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'морфологический' in req['request']['original_utterance'].lower():
        res['response']['text'] = "Какого слова?!"
        names.morf = True
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'как части речи' in req['request']['original_utterance'].lower():
        res['response']['text'] = "Какого слова?!"
        names.cacChast = True
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'морфемный' in req['request']['original_utterance'].lower():
        res['response']['text'] = "Какого слова?!"
        names.morfemn = True
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'по составу' in req['request']['original_utterance'].lower():
        res['response']['text'] = "Какого слова?!"
        names.poSost = True
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'фонетический' in req['request']['original_utterance'].lower():
        res['response']['text'] = "Какого слова?!"
        names.fonet = True
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'звуко-буквенный' in req['request']['original_utterance'].lower():
        res['response']['text'] = "Какого слова?!"
        names.zvbuk = True
        names.rasbor = False
        return

    if names.rasbor:
        if 'морфологический' in req['request']['original_utterance'].lower():
            res['response']['text'] = "Какого слова?!"
            names.morf = True
            names.rasbor = False
            return
        if 'как части речи' in req['request']['original_utterance'].lower():
            res['response']['text'] = "Какого слова?!"
            names.cacChast = True
            names.rasbor = False
            return
        if 'морфемный' in req['request']['original_utterance'].lower():
            res['response']['text'] = "Какого слова?!"
            names.morfemn = True
            names.rasbor = False
            return
        if 'по составу' in req['request']['original_utterance'].lower():
            res['response']['text'] = "Какого слова?!"
            names.poSost = True
            names.rasbor = False
            return
        if 'фонетический' in req['request']['original_utterance'].lower():
            res['response']['text'] = "Какого слова?!"
            names.fonet = True
            names.rasbor = False
            return
        if 'звуко-буквенный' in req['request']['original_utterance'].lower():
            res['response']['text'] = "Какого слова?!"
            names.zvbuk = True
            names.rasbor = False
            return
    if 'разбор' in req['request']['original_utterance'].lower():
        res['response']['text'] = "Какой разбор?"
        names.rasbor = True
        return

    if 'правил' in req['request']['original_utterance'].lower()\
            and "русс" in req['request']['original_utterance'].lower() \
            or "правописан" in req['request']['original_utterance'].lower():
        res['response']['text'] = "Извините, но этот функционал пока не готов."
        return

    res['response']['buttons'] = get_suggests(user_id)
    res['response']['text'] = "Извините, но я не поняла."
    return


def get_suggests(user_id):
    session = names.sessionStorage[user_id]

    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:2]
    ]

    session['suggests'] = session['suggests'][1:]
    names.sessionStorage[user_id] = session

    return suggests


def prov_r_s_c(req):
    if 'расписание' in req['request']['original_utterance'].lower() \
            and ('школ' in req['request']['original_utterance'].lower() or
                 'гимнази' in req['request']['original_utterance'].lower() or
                 'лице' in req['request']['original_utterance'].lower()):
        if 'класс' in req['request']['original_utterance'].lower():
            return True
    return False


def prov_r_s_c_d(req):
    if 'расписание' in req['request']['original_utterance'].lower() \
            and ('школ' in req['request']['original_utterance'].lower() or
                 'гимнази' in req['request']['original_utterance'].lower() or
                 'лице' in req['request']['original_utterance'].lower()):
        if 'класс' in req['request']['original_utterance'].lower():
            if 'понедельник' in req['request']['original_utterance'].lower() \
                    or 'вторник' in req['request']['original_utterance'].lower()\
                    or 'среда' in req['request']['original_utterance'].lower() \
                    or 'четверг' in req['request']['original_utterance'].lower() \
                    or 'пятница' in req['request']['original_utterance'].lower() \
                    or 'суббота' in req['request']['original_utterance'].lower():
                return True
    return False


def get_class(req):
    # перебираем сущности
    for entity in req['request']['nlu']['entities']:
        # находим сущность с типом 'YANDEX.FIO'
        if entity['type'] == 'YANDEX.FIO':
            # Если есть сущность с ключом 'first_name',
            # то возвращаем ее значение.
            # Во всех остальных случаях возвращаем None.
            return entity['value'].get('first_name', None)
    return sessionStorage['nlu']['tokens']


def get_city(req):
    # перебираем именованные сущности
    for entity in req['request']['nlu']['entities']:
        # если тип YANDEX.GEO то пытаемся получить город(city),
        # если нет, то возвращаем None
        if entity['type'] == 'YANDEX.GEO':
            # возвращаем None, если не нашли сущности с типом YANDEX.GEO
            return entity['value'].get('city', None)



def prov_g(req):
    #тут должна быть проверка города
    if True:
                return True
    return False
