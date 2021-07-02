global_logic = ['John', 'Marta', 'Leo']
toshiba = ['John', 'Marta', 'Alex', 'Nik']
toshiba.extend(global_logic)
print(toshiba)

# Good but employees of global logic still in global logic too.
# It could be resolved with next operations:
# 1.
# global_logic.clear()
# or
# 2.
# while global_logic:
#     toshiba.append(global_logic.pop())
# print(toshiba)
# print(global_logic)