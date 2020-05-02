import names


def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        names.sessionStorage[user_id] = {
            'suggests': [
                "Разбор",
                "Рассписание",
                "Отстань!",
            ]
        }
        res['response']['text'] = 'Привет! Я помогу тебе с учёбой! Что ты хочешь? Узнать рассписание или разбор'
        res['response']['buttons'] = get_suggests(user_id)
        return
    if 'рассписание' in req['request']['original_utterance'].lower() \
            and ('школ' in req['request']['original_utterance'].lower() or
                 'гимнази' in req['request']['original_utterance'].lower() or
                 'лице' in req['request']['original_utterance'].lower()):
        res['response']['text'] = 'Вот рассписание'
        return
    elif'рассписание' in req['request']['original_utterance'].lower():
        res['response']['text'] = 'Какой именно школы?'
        names.rasspisanie = True
        return
    elif names.rasspisanie:
        res['response']['text'] = 'Вот рассписание'
        names.rasspisanie = False
        return

    if 'cпасибо' in req['request']['original_utterance'].lower() \
            or "Благодар" in req['request']['original_utterance'].lower():
        res['response']['text'] = "Всегда пожалуйста. Ещё что то?"
        return

    if names.morf:
        names.morf = False
        res['response']['text'] = "Вот разбор"
        return
    if names.zvbuk:
        names.zvbuk = False
        res['response']['text'] = "Вот разбор"
        return
    if names.fonet:
        names.fonet = False
        res['response']['text'] = "Вот разбор"
        return
    if names.poSost:
        names.poSost = False
        res['response']['text'] = "Вот разбор"
        return
    if names.morfemn:
        names.morfemn = False
        res['response']['text'] = "Вот разбор"
        return
    if names.cacChast:
        names.cacChast = False
        res['response']['text'] = "Вот разбор"
        return

    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'морфологический' in req['request']['original_utterance'].lower() \
            and len(req['request']['original_utterance'].lower().split()) >= 3:
        res['response']['text'] = "Вот разбор"
        names.morf = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'как части речи' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 3:
        res['response']['text'] = "Вот разбор"
        names.cacChast = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'морфемный' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 3:
        res['response']['text'] = "Вот разбор"
        names.morfemn = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'по составу' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 3:
        res['response']['text'] = "Вот разбор"
        names.poSost = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'фонетический' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 3:
        res['response']['text'] = "Вот разбор"
        names.fonet = False
        names.rasbor = False
        return
    if 'разбор' in req['request']['original_utterance'].lower() \
            and 'звуко-буквенный' in req['request']['original_utterance'].lower()\
            and len(req['request']['original_utterance'].lower().split()) >= 3:
        res['response']['text'] = "Вот разбор"
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
