
def show_capital(x):
    a=input("Ведите название страны, столицу которой хотите узнать:   ")
    if a in x:
        print("Столица страны " + a + ': ' + x[a])
    else:
        print("В базе нет страны c названием " + a)
    return

def add_new(x):
    a=input("Введите название страны, которую хотите добавить:   ")
    b=input("Введите название столицы данной страны:   ")
    x[a]=b
    print(x)
    return

def correct(x):
    a=input("Введите название страны, которую хотите исправить:   ")
    del x[a]
    b=input("Введите новое название страны:   ")
    c=input("Введите название ее столицы:   ")
    x[b]=c
    print(x)
    return

def randoms(x):
    import random
    country, capital = random.choice(list(x.items()))
    a=input("Введите столицу для страны: " + country + "\n")
    if x.get(country)==a:
        print("Все верно!")
    else:
        print("Неверный ответ!")
    return
