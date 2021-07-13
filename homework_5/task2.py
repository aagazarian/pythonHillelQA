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