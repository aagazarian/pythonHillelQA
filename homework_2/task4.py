gruppa_vegetarians = ["Ivan Ivanov", "Anna Kim"]
gruppa_all = ["Anna Tim", "Marta Hell"]
gruppa_vegetarians.extend(gruppa_all)
print(gruppa_vegetarians)
# Good it is also will work but lets look on solution.
# vegetarians group was extended by all group so in gact your vegeterians were extended
# you should return external list of names and you should not touch existing 2 groups
# so will be better somthing like this:
# print(gruppa_vegetarians + gruppa_all)
