'''
binary search project to look for certain number in a string

project courtesy https://towardsdatascience.com/10-python-mini-projects-that-everyone-should-build-with-code-769c6f1af0c4
'''

# code designed to look in middle then the front and then the end of string
# this exercise introduced me to the double forward slash, which according to article at https://betterprogramming.pub/lesser-known-arithmetic-operators-in-python-a34670087b3a is "known as the integer division operator. Essentially, it will divide the left by the right, and only keep the whole number component." ... n!ce
# interesting number seven only returns for one position and at location seven when clearly indexed farther along in the list
lst7 = [1, 3, 0, 2, 44, 5, 6, 67, 9, 8, 37, 99, 10, 64, 13, 88, 7, 56, 7, 21, 70, 91]
lst7.sort()
first = 0
last = len(lst7) - 1
mid = (first + last) // 2
item = int(input("Enter Searchable Number: "))
found = False
while( first <= last and not found):
    mid = (first + last) // 2
    if lst7[mid] == item :
        print(f"found at location {mid}")
        found = True 
    else:
        if item < lst7[mid]:
            last = mid - 1
        else:
                first = mid + 1

if found == False:
    print("Number Not Found")
