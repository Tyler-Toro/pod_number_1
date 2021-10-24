def say_hello():
    print('Hello Python Code World!')

# For this remember to invoke the function by calling it ... i.e. do not assume the print statement is for printing in functions ... instead add the function to invoke it i.e. at the end of the code add say_hello()
say_hello()

if 3 > 7:
    say_hello()
else:
    print('not true')

def say_hello_tyler():
    print('Hello Tyler')
    print('Good day to you, ')
    print('and goodnight.')

say_hello_tyler()

# Function using other functions
# Couldn't get bottom to work - keep practicing 
def say_hello_alanna():
    print("Hello Alanna")
    print("and I hope the day treats you well.")

say_hello_alanna
say_hello_tyler

# Add parameter(s)
def say_hello(name):
    print(f'Hello {name}')
    print('Good day')
    print('and good evening.')

say_hello('Alanna')
say_hello('Deshawn')

# Functions w/operations
def times_two(num):
    print(num * 2)

times_two(88)
times_two(9320987528435)

# List passed into function
number = [3, 0, 0, 7, 9, 2]
def first_num(nums):
    print(nums[0])
first_num(number)  

def greeting(first_name, middle_name, last_name):
    print(first_name, middle_name, last_name)
    print(f'Hi folks, my name is {first_name} and I hail from the land of wanting a better life.')
greeting('La\'Tonia Mertica', 'Middle Name', 'Sheppard Walker')

# Using default value (i.e. arguements) instead of parameters (i.e. added inside the function)
def times_seven(q = 7, r = 13):
    print(q*r)
times_seven()