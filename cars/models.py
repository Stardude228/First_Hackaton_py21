import json

class Cars:
    def __init__(self, brand, model, year, volume, color, body, mileage, price):
        # Changing IDs for cars
        with open("db.json") as db:
            temp = db.read()
            temp = json.loads(temp)
            temp['id'] += 1
            print(temp)
    
        db1 = open("db.json", 'w')
        res = json.dumps(temp)
        db1.write(res)
        db1.close()
        # Changing IDs for cars

        # Creation of cars
        self.id_ = temp['id']
        self.brand = brand
        self.model = model
        self.year = year
        self.volume = volume
        self.color = color
        self.body = body
        self.mileage = mileage
        self.price = price

        car = {
            "brand": str(brand),
            "model": str(model),
            "year": str(year),
            "volume": str(volume),
            "color": str(color),
            "body": str(body),
            "mileage": str(mileage),
            "price": str(price),
            "ID": str(self.id_)
        }
        # Creation of cars

        # Changing and sending to database
        with open("db.json") as db:
            temp = db.read()
            temp = json.loads(temp)
            temp['cars'].append(car)
            print(temp)
        
        db1 = open("db.json", 'w')
        res = json.dumps(temp)
        db1.write(res)
        db1.close()
        # Changing and sending to database


    def __str__(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "volume": self.volume,
            "color": self.color,
            "body": self.body,
            "mileage": self.mileage,
            "price": self.price
        }
