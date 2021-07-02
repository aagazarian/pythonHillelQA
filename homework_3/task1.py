lists = [1, 2, 3, 1, 4, 5, 6, 2, 7, 8]  # Well. I suppose it is only one list with numbers so I suggest to name it like elements.
even = []  # Same thing. I suggest to name it like even_elements
not_even = []  # I suggest to name it like odd_elements
for element in lists:  # I suggest write expression like 'for element in elements'
    tpl = (lists.index(element), element) # this line could be placed inside append method
    if lists.index(element) % 2 == 0:
        even.append(tpl)
    else:
        not_even.append(tpl)
print(even)
print(not_even)

# Good. Task was solved correctly but what will be if I will add some more elements inside the list?
# Take a look on printed lists now.
