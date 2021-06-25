gruppa = ["Elena Duo", "Elena Duo", "Tim Pike", "Kim Test", "Elena Duo"]
for i in gruppa:
    while gruppa.count(i) > 1:
        gruppa.remove(i)
print(gruppa)
# Good. Interesting solution but it could be done with dicts
# print(list({}.fromkeys(gruppa).keys()))
