import sqlite3


con = sqlite3.connect('BaseOfSchools.db')
cur = con.cursor()


def name_of_schools(city):  # Все школы
    con = sqlite3.connect('BaseOfSchools.db')
    cur = con.cursor()
    a = cur.execute('SELECT nameofschool FROM schools WHERE city = "{id}" AND checked = 1'.format(id=city)).fetchall()
    if a:
        return a
    return cur.execute('SELECT nameofschool FROM schools WHERE city = "{id}"'.format(id=city)).fetchall()


def name_of_school(id):
    con = sqlite3.connect('BaseOfSchools.db')
    cur = con.cursor()
    a = cur.execute('SELECT nameofschool FROM schools WHERE id = {id} AND checked = 1'.format(id=id)).fetchone()
    if a:
        return a
    return cur.execute('SELECT nameofschool FROM schools WHERE id = {id}'.format(id=id)).fetchone()


def id_of_school(city, name):  # ID школы, вводится город, название школы
    con = sqlite3.connect('BaseOfSchools.db')
    cur = con.cursor()
    a = cur.execute('SELECT id FROM schools WHERE city = "{city}" AND nameofschool = "{name}" AND checked = 1'.format(
        name=name, city=city)).fetchone()
    if a:
        return a
    return cur.execute('SELECT id FROM schools WHERE city = "{city}" AND nameofschool = "{name}"'.format(
        name=name, city=city)).fetchone()


def id_of_class(school_id, clas):  # ID класса, в school вводится ID школы, в clas - название класса
    con = sqlite3.connect('BaseOfSchools.db')
    cur = con.cursor()
    a = cur.execute('SELECT id FROM classes WHERE school = {school} AND class = "{clas}" AND checked = 1'.format(
        school=school_id, clas=clas)).fetchone()
    if a:
        return a
    return cur.execute('SELECT id FROM classes WHERE school = {school} AND class = "{clas}"'.format(
        school=school_id, clas=clas)).fetchone()


def pupils(school_id, clas):  # Ученики класса, в school_id водится id школы, в clas - название класса
    con = sqlite3.connect('BaseOfSchools.db')
    cur = con.cursor()
    a = cur.execute('SELECT pupils FROM classes WHERE school = {id} AND class = "{clas}" AND checked = 1'.format(
        clas=clas, id=school_id)).fetchone()
    if a:
        return a
    return cur.execute('SELECT pupils FROM classes WHERE class = "{clas}"'.format(
        clas=clas)).fetchone()


def table(clas_id, day=''):  # Расписание, в clas вводится id класса
    con = sqlite3.connect('BaseOfSchools.db')
    cur = con.cursor()
    #  В day - день недели, если не ввести день недели, то вернёт полное расписание
    if day == '':
        a = cur.execute(
            'SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM tables WHERE class = {id}'
            ' AND checked = 1'.format(id=clas_id)).fetchone()
        if a:
            return a
        return cur.execute(
            'SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM tables'
            ' WHERE class = {id}'.format(id=clas_id)).fetchone()
    a = cur.execute('SELECT {day} FROM tables WHERE class = {id} AND checked = 1'.format(id=clas_id, day=day)).fetchone()
    if a is not False:
        return a
    return cur.execute('SELECT {day} FROM tables WHERE class = {id}'.format(id=clas_id, day=day)).fetchone()


def classes(school_id):
    con = sqlite3.connect('BaseOfSchools.db')
    cur = con.cursor()
    a = cur.execute('SELECT class FROM classes WHERE school = {id} and checked = 1'.format(id=school_id)).fetchall()
    if a:
        return a
    return cur.execute('SELECT class FROM classes WHERE school = {id}'.format(id=school_id)).fetchall()


def add_school(name, city, address, checked):
    con = sqlite3.connect('BaseOfSchools.db')
    cur = con.cursor()
    cur.execute('INSERT INTO schools (nameofschool, city, address, checked)'
                ' VALUES("{name}", "{city}", "{address}", {checked})'.format(
        name=name, city=city, address=address, checked=checked))
    con.commit()


def add_class(school, clas, checked, *pupils):
    con = sqlite3.connect('BaseOfSchools.db')
    cur = con.cursor()
    cur.execute('INSERT INTO classes (school, class, pupils, checked)'
                ' VALUES("{school}", "{clas}", "{pupils}", "{checked}")'.format(
        school=school, clas=clas, pupils=pupils, checked=checked))
    con.commit()
