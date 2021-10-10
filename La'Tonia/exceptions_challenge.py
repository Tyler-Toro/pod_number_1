print('Question 1')
# TODO: Fix error(s) so that the if/else blocks runs without issues
# followed basic proper structure to fix ... ensured colons, tabs/indents ...
a = 1
b = 2

if a < b:
    print(f'{a} is less than {b}')

else:
    print(f'{a} is greater than {b}')

print('')
print()


print('Question 2')
# TODO: Fix error(s) so that a list of sandwiches with unique combinations of meats and cheeses is printed at line 22
# changed meet to variable meats in f-string

meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

sandwiches = []

for meat in meats:
    for cheese in cheeses:
        sandwiches.append(f'{meats} & {cheese}')

print(sandwiches)

print('')
print()


print('Question 3')
# TODO: Fix error(s) in the the print statements to repeat a string
# exercise states to repeat a string, before I fixed line 48 was not a string - the first argument was a set of curly braces ... I wrapped the curly braces in single quotes to create a string


def repeat(str, times):
    return str * times


print(repeat('python', 3))
print(repeat('[]', 3))
print(repeat('//', 3))
print(repeat('{}', 5))
print(repeat('{[', 3))

print('')
print()


print('Question 4')
# TODO: Fix error(s) in the print statements to look up all 5 fruits by their index
# list indices begin with zero
# re-numbered index for each fruit from starting at 1 to starting at 0 and going in succession down the line to line up proper index to each fruit in the list
fruits = ['apples', 'oranges', 'bananas', 'tomatoes', 'cherries']

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])


print('')
print()


print('Question 5')

num = input("Enter a number to compute it's square value: ")

# Line 65 currently errors if you provide an input like a dictionary instead of a number
# TODO: Rewrite line 65 with try/except blocks to handle all exceptions. If an exception exists, print 'Something Went Wrong!'
# TODO: Bonus: Add a finally block to print 'The End'
# commented out line 81 and replaced with try/except ... line 81 on its own throws error and clogs rest of code from running
# added finally per basic proper try/except/finally structure
# print(int(num) * int(num))

try:
    print(int(num) * int(num))
except:
    print('Somethings Wrong')
finally:
    print('The End')
    print()


print('Question 6')

# TODO: Change the code here so that the 'NameError' exception block runs.
# commented out 'Yusuf' on line 96 so name is non existent 
# name = 'Yusuf'
# re-trying this exercise with a misspelling ... works/also results in print of NameError
name = 'Yusuf'

try:
    print(naame.capitalize())
except NameError:
    print('You got to run this exception block! Your challenge is completed!')
except:
    print('You should not be seeing this print statement. Try a different solution!')
