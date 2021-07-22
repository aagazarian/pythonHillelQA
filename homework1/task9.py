from homework1 import task6
from homework1.task7 import coordinates_john, coordinates_marta

peter = {
    "full_name": "Peter Ivanov",
    "age": 20, "salary": 200,
    "gender": True,
    "friends": task6.name,
    "coordinates": coordinates_john
}
# Good but friends of peter also could be dicts

simon = {
    "full_name": "Simon Ivanov",
    "age": 20, "salary": 200,
    "gender": True,
    "friends": task6.name,
    "coordinates": coordinates_john
}
# Good but friends of simon also could be dicts

alex = {
    "full_name": "Alex Ivanov",
    "age": 20, "salary": 200,
    "gender": True,
    "friends": task6.name,
    "coordinates": coordinates_marta
}
# Good but friends of alex also could be dicts

grek = {
    "full_name": "Grek Ivanov",
    "age": 20,
    "salary": 200,
    "gender": True,
    "friends": task6.name,
    "coordinates": coordinates_marta
}
# Good but friends of grek also could be dicts

john = {
    "full_name": "Jouh Ivanov",
    "age": 20,
    "salary": 200,
    "gender": True,
    "friends": [peter, simon],
    "coordinates": coordinates_john
}

marta = {
    "full_name": "Marta Ivanova",
    "age": 20,
    "salary": 200,
    "gender": True,
    "friends": [alex, grek],
    "coordinates": coordinates_marta
}

print("John:")
for key, value in john.items():
    print(f"{key} => {value}")

print("Marta:")
for key, value in marta.items():
    print(f"{key} => {value}")
