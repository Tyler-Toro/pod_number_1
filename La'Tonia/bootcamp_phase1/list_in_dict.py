# Practice creating list in a dictionary
# flats, heels, boots are different kinds of shoes
# names of items in my boot closet list are named after women i.e. the debra ann heel
boot_closet = {
    'flats': ['cinderella', 'snow white', 'rahpunzle'],
    'heels': ['cindy lous', 'debra ann', 'janice pearl'],
    'boots': ['jacqueline', 'karens', 'greta'],
    'combined_worth': 44321.07
}


# Print whole boot closet dictionary
# Print datatype for boot closet dictionary
print(boot_closet)
print(type(boot_closet))
print()

# Print boots list from within boot closet dictionary but only the second-indexed list
# Print datatype of boots list from within boot closet dictionary but only the second-indexed item  
print(boot_closet['boots'][1])
print(type(boot_closet['boots'][1]))
print()

# Print how much the entire boot closet could sell for at this moment
print(boot_closet['combined_worth'])
# Code below returns syntax error and can't figure out reasons given the syntax seems correct ... 
# UPDATE: Ignore previous note because the code executed correctly after I closed terminal and started w/fresh terminal ... 
# Note to Self: Based on search, seems if has single quote in f-string then should use double quotes for the f-string ... 
# Files need .py extension and re-ran code == returned same syntax error ... 
# Final Answer: Was running code on wrong version of python (2 not 3) s/b all set now 
print(f"The entire boot closet. If sold to a feverish shoe fan. Can sell this very second for ${boot_closet['combined_worth']}.")
print()

# Confirm datatype of list inside dictionary
print(boot_closet['flats'])
print(type(boot_closet['flats']))

# Replace element in list nested in dictionary
boot_closet['boots'][2] = 'dez'
print(boot_closet)