# What is a list?
# # Lists are commonly used to store related data

shopping_list = ["bread", "chocolate", "avocados", "milk"]
# print(shopping_list)

# print(shopping_list[0])

# shopping_list[0] = "orange"
# shopping_list.append("apple juice")

# shopping_list.pop(0)
# print(shopping_list)

mixed_list = [1, 2, 3, "one", "two", "three"]
# print(mixed_list)

# weekdays_de = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag")
# # weekdays_de[0] = "Monday" # causes an error
# print(weekdays_de)

# # This works, but probably isn't very useful as is
# odd_items = [shopping_list, mixed_list, weekdays_de]
# print(odd_items)

# prompted by a question

tuple_of_lists = (shopping_list, mixed_list)
print(tuple_of_lists)
tuple_of_lists[0][1] = "M 'n Ms"
print(tuple_of_lists)