from pprint import pprint
from models import Cars
import json

def car_create():
    brand = input('Type a brand: ')
    model = input('Type a model: ')
    year = input('Type a year: ')
    volume = input('Type a volume: ')
    color = input('Type a color: ')
    body = input('Type a body: ')
    mileage = input('Type a mileage: ')
    price = input('Type a price: ')

    Cars(brand, model, year, volume, color, body, mileage, price)
    return 'Car has been created successfully!'

def car_listing():
    file = open('db.json')
    data = json.load(file)
    pprint(data['cars'])
    file.close()

def car_retrieve():
    user_choice = input('Type an ID of a car that you want to find \n(if you wish to look at the list of all cars try car_listing): ')
    # Opening a database
    file = open('db.json')
    data = json.load(file)
    data = data['cars']
    # Opening a database

    # Search of ID
    found = False
    for i in data:
        if user_choice in i['ID']:
            found = True
            pprint(i)
    if found == False:
        print('There is no such ID')
    file.close()
    # Search of ID

def car_update():
    user_choice = input('Type an ID of a car that you want to update \n(if you wish to look at the list of all cars try car_listing): ')
    user_change = input('Type a setting of a car that you wish to change: ')
    user_setting = input('Type a change: ')

    # Opening a database
    file = open('db.json')
    data = json.load(file)
    data = data['cars']
    file.close()
    # Opening a database

    # Search of ID and change of setting 
    found = False
    for i in data:
        if user_choice in i['ID']:
            found = True
            i[user_change] = user_setting
    if found == False:
        print('There is no such ID')
    # Search of ID and change of setting 

    # Sending a changed setting
    pprint(data)
    # db1 = open("db.json", 'w')
    # pprint(db1)
    # res = json.dumps(data)
    # db1.write(res)
    # db1.close()
    # file.close()
    # Sending a changed setting

# def car_delete():
#     user_choice = input('Type an ID of a car that you want to delete \n(if you wish to look at the list of all cars try car_listing): ')
#     # Opening a database
#     file = open('db.json')
#     data = json.load(file)
#     data = data['cars']
#     # Opening a database

#     # Search of ID
#     found = False
#     for i in data:
#         if user_choice in i['ID']:
#             found = True
#             pprint(data)
#             data.remove(i)
#             pprint(data)
#     if found == False:
#         print('There is no such ID')
#     file.close()
#     # Search of ID

# car_create()
# car_listing()
# car_retrieve()
car_update()
# car_delete()