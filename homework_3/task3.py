friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for name in friends:
    if name != 'James':
        if name not in enemies:
            print(f"{name} we are the best friends")
        else:
            print(f"{name} we are not the friends anymore")

# Good. You are first who solved this task in such style.
