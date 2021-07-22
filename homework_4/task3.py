string_query = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro              "
null_list = string_query.strip(' ')
print(null_list)
first = null_list.split('&&')
print(first)

final_list = []

for element in first:
    second = element.split('&')
    print(second)
    for el in second:
        final = el.split('=', maxsplit=1)
        final_list.append(final)
        # dict([final])

print(dict(final_list))

# Good. But take a look how it could be solved easier
# result = dict()
#
# for pair in some_string.strip().split('&'):
#     if pair:
#         key, value = pair.split('=', maxsplit=1)
#         result[key] = value
#
# print(result)
