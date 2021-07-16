first = 0
second = 0
operator = 0
count = 1

with open("test/data/tuple.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        string = "{}".format(line.strip())
        list = string.split()

        for element in list:
            if list.index(element) == 0:
                first = int(element)
            elif list.index(element) == 1:
                second = int(element)
            else:
                operator = int(element)

        if operator == 1:
            result = first + second
        elif operator == 2:
            result = first - second
        else:
            result = first / second

        print(f"Line {count}: {result}")
        count += 1

# Not bad but it could be solved in more elegant way
# import pickle
#
# with open('test/data/text.txt', "rb") as file:
#     operations = pickle.load(file)
#
#     for operation in operations:
#         left, right, operator = operation
#         if operator == 1:
#             print(f"{left} + {right} = {left + right}")
#         elif operator == 2:
#             print(f"{left} * {right} = {left * right}")
#         else:
#             print(f"{left} / {right} = {left / right}")
