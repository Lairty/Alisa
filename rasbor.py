import requests
import names


def morfolog(slovo):
    k = requests.get("http://morphologyonline.ru/{}".format(slovo)).text
    l = k.find("<ol>")
    r = k.find("</ol>")
    k = k[l:r:1]
    ki = "Извините, произошла какая-то ошибка"
    if "имя существительное" in k or "имя прилагательное" in k or "глагол" in k or "местоимение" in k:
        ki = ""
        for i in range(len(k)):
            if k[i] in names.dic:
                ki += k[i]
        ki = "1. " + ki[12::].replace("-Морфологические",
                                      "\n2. Морфологические").replace("признакиНачальная",
                                                                      "признаки:\nНачальная").replace("Постоянные",
                                                                                                      "\nПостоянные")
        ki = ki.replace("Непостоянные",
                        "\nНепостоянные").replace("-Синтаксическая",
                                                  "\n3. Синтаксическая").replace("рольМожет",
                                                                                 "роль: Может").replace("  ", " - ")
    elif "наречие" in ki:
        ki = ""
        for i in range(len(k)):
            if k[i] in names.dic:
                ki += k[i]
        r = ki.rfind("--")
        ki = "1. " + ki[12:r:].replace("-Морфологические",
                                       "\n2. Морфологические").replace("признаки",
                                                                       "признаки: ").replace("Постоянные",
                                                                                            "\nПостоянные")
        ki = ki.replace("Непостоянные",
                        "\nНепостоянные").replace("-Синтаксическая",
                                                  "\n3. Синтаксическая").replace("роль",
                                                                                 "роль - ").replace("  ", " - ")
    return ki


def fonet(slovo):
    k = requests.get("http://phoneticonline.ru/{}".format(slovo)).text
    l = k.rfind("Транскрипция")
    r = k.rfind("Цветовая")
    k = k[l:r:1]
    ki = "{}\n".format(slovo)
    for i in range(len(k)):
        if k[i] in names.dic:
            ki += k[i]
    ki = ki.replace("  ", " ").replace("ударный", "ударный\n").replace("(парный)", "(парный)\n") \
        .replace("(непарный, всегда произносится мягко)", "(непарный, всегда произносится мягко)\n").replace("  ", " ")
    f = ki.find("]") + 1
    ki = ki[:f:] + "\n" + ki[f::]
    return ki


def morfemn(slovo):
    k = requests.get("https://sostavslova.ru/{}/{}".format(slovo[0].upper(), slovo)).text
    l = k.find("Состав слова")
    r = k.find("Часть речи")
    k = k[l:r:1]
    ki = "{}{}\n".format(slovo[0].upper(), slovo[1::])
    for i in range(len(k)):
        if k[i] in names.dic:
            ki += k[i]
    ki = ki.replace("Состав слова:", "Состав слова:\n").replace(" ", "").replace("Составслова", "Состав слова") \
        .replace("корень", "корень - ").replace(",", ",\n").replace("суффикс", "суффикс - ") \
        .replace("окончание", "окончание - ").replace("основаслова", "основа слова - ")
    return ki
