from module1 import *
import random
countries={"Austria": "Vena","Estonia": "Tallinn","Russia": "Moscow"}
r=int(input("1 - узнать столицу введенной страны\n2 - добавить в базу данных страну и ее столицу\n3 - исправить ошибку в базе данных\n4 - проверить себя\n5 - закончить работу\nвыберите действие:   "))

if r==1:
    show_capital(countries)
elif r==2:
    add_new(countries)
elif r==3:
    correct(countries)
elif r==4:
    randoms(countries)
elif r==5:
    exit()
