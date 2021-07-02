lists = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
not_even = []
for element in lists:
    tpl = (lists.index(element), element)
    if lists.index(element) % 2 == 0:
        even.append(tpl)
    else:
        not_even.append(tpl)
print(even)
print(not_even)
