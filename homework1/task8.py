from homework1.task6 import names
from homework1.task7 import coordinates_john, coordinates_marta

john = {"full_name": "Jouh Ivanov", "age": 20, "salary": 200, "gender": True, "friends": names, "coordinates": coordinates_john}
marta = {"full_name": "Marta Ivanova", "age": 20, "salary": 200, "gender": True, "friends": names, "coordinates": coordinates_marta}

for key, value in john.items():
        print("%s => %s" % (key, value))

for key, value in marta.items():
        print("%s => %s" % (key, value))
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

# # line 8 and 11 over indented 8 spaces instead of 4
