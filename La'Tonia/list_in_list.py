taste_test_list = [
    ['raspberries in cream', 'vodka soaked peaches', 'caramel spiked honey lamb'], 
    [44, 3, -99, 87, -1, 0], 
    [True, False]
    ]

print(taste_test_list)
print()

# Print just the second list in the main list
print(taste_test_list[1])
print()

# Add item to a list in the main list and to the main list 
# Interesting that this created a new list inside of the list - tried to add just the items into the existing list not a list in the list
taste_test_list[2].append(['Optional', 'Maybe'])
print(taste_test_list)
print()

taste_test_list.append(['Create a To-Do List', 'Go Get Groceries w/Fun Stuff'])
print(taste_test_list)
print()

# Remove something using two delete methods
taste_test_list[0].remove('caramel spiked honey lamb')
print(taste_test_list)
print()

taste_test_list[1].clear()
print(taste_test_list)
print()

# Pop seems to be popping/removing the oppostive - i.e. keeping the item I input into the pop method/function to be deleted and deleting the other only option in that list ... Why?
taste_test_list[2].pop(False)
print(taste_test_list)
print()