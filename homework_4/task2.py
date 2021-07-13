friends = ["John", "Marta", "James", "Amanda", "Marianna"]
print(f'Names'.center(40, '*'))
for names in friends:
    print(f"{names.rjust(20,' ')}\n")
