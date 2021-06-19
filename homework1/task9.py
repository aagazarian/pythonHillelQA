from homework1 import task6
from homework1.task7 import coordinates_john, coordinates_marta

peter = {"full_name": "Peter Ivanov", "age": 20, "salary": 200, "gender": True, "friends": task6.names, "coordinates": coordinates_john}  # Good but friends of peter also could be dicts
simon = {"full_name": "Simon Ivanov", "age": 20, "salary": 200, "gender": True, "friends": task6.names, "coordinates": coordinates_john}  # Good but friends of simon also could be dicts
alex = {"full_name": "Alex Ivanov", "age": 20, "salary": 200, "gender": True, "friends": task6.names, "coordinates": coordinates_marta}  # Good but friends of alex also could be dicts
grek = {"full_name": "Grek Ivanov", "age": 20, "salary": 200, "gender": True, "friends": task6.names, "coordinates": coordinates_marta}  # Good but friends of grek also could be dicts

john = {"full_name": "Jouh Ivanov", "age": 20, "salary": 200, "gender": True, "friends": [peter, simon], "coordinates": coordinates_john}
marta = {"full_name": "Marta Ivanova", "age": 20, "salary": 200, "gender": True, "friends": [alex, grek], "coordinates": coordinates_marta}

print ("john: %s" % john)  # Good but there should not be whitespace before '('
print ("marta: %s" % marta)  # Good but there should not be whitespace before '('

# Good but it could be described and printed in console in more elegant way:
# john = {
#     "first_name": "John",
#     "last_name": "Smith",
#     "age": 25,
#     "gender": "male",
#     "parents": ["John Smith Junio", "Marta Smith"]
# }
#  Look on how dict is described. It is more preferable view on real projects.
# print(john)
#
#
# for key, value in john.items():
#     # print(key, value, sep=" => ")
#     print(f"{key} => {value}")