print("Challenge 3.1: Debug code snippets")
#Debug each snippet in order
print()



print("Code Snippet 1:")
u = 5
v = 2
#changed single equal sign, which denotes assignment, into double equal sign to denote equal to for the goal of printing the first/True statement and not to print the else statement
if u * v == 10:
    print(f"The product of u ({u}) and v ({v}) is 10")
else:
    print(f"The product of u ({u}) and v ({v}) is not 10")
print()



print("Code Snippet 2:")
x = 15
y = 25
z = 30
if z < x:
    print("z is less than x")
# added colon after y in statement below
elif z > x and z < y:
    print("z is between x and y")
# added colon after else in statement below
else:
    print("z is greater than y")
print()



print("Code Snippet 3:")
#modify the comparison operator below so the assert statement passes
#update the print statement to reflect changes to the code
a = 1
b = 1
# changed greater than operator between a and b to equal operator between a and b
c = (a == b)
# changed following print statement to active print statement that follows this comment print(f"The value of c ({c}) is True since a ({a}) is greater than b ({b}).")
print(f"The value of c ({c}) is True since a ({a}) and b ({b}) each contain the same value.")
assert(c == True) #Do not change this line
print()



print("Code Snippet 4:")
#modify exactly one boolean operator in the assignment of d, so that d evaluates to False
# To solve, both sides need to be False. Another option is to replace the or operator with the and operator. Note when the value is False the statement does not print. To illustrate the value, I added a print statement for variable d to print the value.
d = (5 < 7) and not (8 < 20)
#TO DO: Explain how d is set to False in a print statement
# d is set to False because assert obligates what the value can be. In this exercise, using the double equals sign forces the only acceptable option for the value of d to be False. 
assert(d == False) #Do not change this line
print(d)
print()



print("Code Snippet 5:")
#modify the comparison operator so o evalutes to true
#update the print statement to reflect the changes
m = "GOAT"
n = "goat"
# changed the below code from == to != to reverse the returned result from False to True (different letter case == unequal values)
o = (m != n)
print (f"The value of o ({o}) is True since the not operator has been added to reverse the outcome value, which was initially False because Python is case-sensitive.")
assert(o == True) #Do not change this line
print()
print("CHALLENGE COMPLETE!")
