import names
import rasbor


def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        names.sessionStorage[user_id] = {
            'suggests': [
                "Разбор",
                "Расписание",
                "Отстань!",
            ]
        }
        res['response']['text'] = 'Привет! Я помогу тебе с учёбой.'
        res['response']['buttons'] = get_suggests(user_id)
        return
    if prov_g(req) and 'расписание' in req['request']['original_utterance'].lower() \
            and ('школ' in req['request']['original_utterance'].lower() or
                 'гимнази' in req['request']['original_utterance'].lower() or
                 'лице' in req['request']['original_utterance'].lower()):
        res['response']['text'] = 'Какого класса?!'
        names.rasspisanie = False
        names.raspisanie2 = True
        return
    elif 'расписание' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Какой города?'
        names.city = True
        return
    elif names.city:
        res['response']['text'] = 'Какой именно школы?'
        names.city = False
        names.rasspisanie = True
        return
    elif names.rasspisanie:
        res['response']['text'] = 'Какого класса?!'
        names.rasspisanie = False
        names.raspisanie2 = True
        return
    elif names.raspisanie2:
        res['response']['text'] = "На какой день?!"
        names.raspisanie2 = False
        names.rasspisanie3 = True
        return
    elif names.rasspisanie3:
        res['response']['text'] = "Вот расписание"
        names.rasspisanie3 = False
        return
    elif prov_r_s_c(req) and prov_g(req):
        res['response']['text'] = "На какой день?!"
        names.raspisanie2 = False
        names.rasspisanie3 = True
        return
    elif prov_r_s_c_d(req) and prov_g(req):
        res['response']['text'] = "Вот расписание"
        names.rasspisanie3 = False
        return

    if 'cпасибо' in req['request']['original_utterance'].lower() \
            or "Благодар" in req['request']['original_utterance'].lower():
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

    #res['response']['buttons'] = get_suggests(user_id)
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

    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": "https://market.yandex.ru/search?text=слон",
            "hide": True
        })

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


def prov_g(req):
    #тут должна быть проверка города
    if True:
                return True
    return False
