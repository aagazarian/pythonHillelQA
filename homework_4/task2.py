friends = ["John", "Marta", "James", "Amanda", "Marianna"]
print(f'Names'.center(40, '*'))
for names in friends:
    print(f"{names.rjust(20,' ')}\n")

# Good but solved only using str methods. Take a look how to align text right
# or in center using fstring operators
# -2 points
