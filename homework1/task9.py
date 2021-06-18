from homework1 import task6
from homework1.task7 import coordinates_john, coordinates_marta

peter = {"full_name": "Peter Ivanov", "age": 20, "salary": 200, "gender": True, "friends": task6.names, "coordinates": coordinates_john}
simon = {"full_name": "Simon Ivanov", "age": 20, "salary": 200, "gender": True, "friends": task6.names, "coordinates": coordinates_john}
alex = {"full_name": "Alex Ivanov", "age": 20, "salary": 200, "gender": True, "friends": task6.names, "coordinates": coordinates_marta}
grek = {"full_name": "Grek Ivanov", "age": 20, "salary": 200, "gender": True, "friends": task6.names, "coordinates": coordinates_marta}

john = {"full_name": "Jouh Ivanov", "age": 20, "salary": 200, "gender": True, "friends": [peter, simon], "coordinates": coordinates_john}
marta = {"full_name": "Marta Ivanova", "age": 20, "salary": 200, "gender": True, "friends": [alex, grek], "coordinates": coordinates_marta}

print ("john: %s" % john)
print ("marta: %s" % marta)