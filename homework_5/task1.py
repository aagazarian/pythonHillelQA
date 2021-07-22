import os
import random

# dir_list = os.listdir()
# if "test" not in dir_list:
#     print("File doesn't exist")
#     os.makedirs("test/data")
#
# tuple_list = []
# operation = [1, 2, 3]
#
# for element in range(100):
#     tuple_list.append((random.randint(0, 1000), random.randint(1, 1000), random.randint(1, 3)))
#
# print(tuple_list)
#
# final_string = ""
# with open("test/data/tuple.txt", "w") as file:
#     for tuple_element in tuple_list:
#         for element in tuple_element:
#             if tuple_element.index(element) != 2:
#                 final_string = f"{final_string}{str(element)} "
#             else:
#                 final_string = f"{final_string}{str(element)}\n"
#
#     file.write(final_string)
#     file.close()

# Good but take a look how it could be solved in more clear way
import pickle
import os

from random import randint


os.makedirs("test/data")
operations = []

for _ in range(100):
    operations.append((randint(1, 100), randint(1, 100), randint(1, 3)))

with open("test/data/text.txt", "wb") as file:
    pickle.dump(operations, file)
