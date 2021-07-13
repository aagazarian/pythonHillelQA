import re

name = ["FirstItem", "FriendsList", "MyTuple"]
name_new = []
for element in name:
    element = re.sub(r'(?<!^)(?=[A-Z])', '_', element).lower()
    name_new.append(element)
print(name_new)  # camel_case_name
