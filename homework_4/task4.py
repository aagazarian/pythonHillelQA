import re

name = ["FirstItem", "FriendsList", "MyTuple"]
name_new = []
for element in name:
    element = re.sub(r'(?<!^)(?=[A-Z])', '_', element).lower()
    name_new.append(element)
print(name_new)  # camel_case_name

# Good. One ot the 2 possible solutions with regular expression
# some_list = ["FirstItem", "FriendsList", "MyTuple"]
# new_list = []

# for str_ in some_list:
#     new_list.append(re.sub('(?!^)([A-Z]+)', r'_\1', str_).lower())
