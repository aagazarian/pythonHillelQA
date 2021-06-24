from homework1.task6 import names
from homework1.task7 import coordinates_john, coordinates_marta

john = {
    "full_name": "Jouh Ivanov",
    "age": 20, "salary": 200,
    "gender": True,
    "friends": names,
    "coordinates": coordinates_john
}

marta = {
    "full_name": "Marta Ivanova",
    "age": 20, "salary": 200,
    "gender": True,
    "friends": names,
    "coordinates": coordinates_marta
}

for key, value in john.items():
    print("%s => %s" % (key, value))

for key, value in marta.items():
    print("%s => %s" % (key, value))
