import requests
import names


def russki(pravilo):
    for i in range(1, 10):
        k = requests.get("https://interneturok.ru/subject/russian/class/{}".format(i)).text.lower()
        f = k.find(pravilo.lower())
        if f != -1:
            break
        elif f == -1 and i == 9:
            return "Извините, я не нашла правило."
    h = k[:f:]
    g = h.rfind("<a href=")
    t = h[g::]
    l = t.find('"')
    r = t.find('"', l + 1)
    t = t[l + 1:r:]
    lin = "https://interneturok.ru" + t
    k = requests.get(lin).text
    h = k.find("Смотреть в видеоуроке")
    k = k[h::]
    h = k.find(">")
    k = k[h + 1::]
    h = k.find("Список литературы")
    k = k[:h:]
    ki = ""
    for i in range(len(k)):
        if k[i] in names.dic:
            ki += k[i]
    f = ki.find("Смотреть в видеоуроке")
    while f != -1:
        l = ki.find("2 -  -")
        r = ki.find(" -__")
        ki = ki[:l:] + ki[r + 4::]
        f = ki.find("Смотреть в видеоуроке")
    return ki


def fizik(prav):
    k = requests.get("https://educon.by/index.php/formuly/formfiz").text
    l = k.find("Средняя скорость при равноускоренном движении")
    r = k.find("/></p>", l)
    k = k[l:r:]
    l = k.find("img src=")
    r = k.find("alt=")
    k = k[l:r:]
    l = k.find('"')
    r = k.find('"', l + 1)
    k = k[l + 1:r:]
    link = "https://educon.by" + k
    return link
