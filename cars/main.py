from urls import urlpatterns
from pprint import pprint

while True:
    try:
        url = input('Type an address: ')
    except ValueError:
        print('You printed not valid url')
        continue
    
    found = False

    for uri, view in urlpatterns:
        if uri == url:
            found = True
            try:
                print(view())
            except Exception as e:
                print(e)
    if not found:
        print('404 url not found')