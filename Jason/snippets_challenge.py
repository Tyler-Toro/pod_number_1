print("Challenge 3.1: Debug code snippets")
#Debug each snippet in order

print()

print("Code Snippet 1:") 

u = 5
v = 2

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

elif (z > x and z < y):
    print("z is between x and y")

else:
    print("z is greater than y")


print()

print("Code Snippet 3:")

#modify the comparison operator below so the assert statement passes
#update the print statement to reflect changes to the code

a = 1
b = 1
c = (a >= b)

print(f"The value of c ({c}) is True since a ({a}) is greater than or equal to b ({b}).")
assert(c == True) #Do not change this line

print()

print("Code Snippet 4:")

#modify exactly one boolean operator in the assignment of d, so that d evaluates to False

d = (5 > 7) or not (8 < 20)
# TO DO: Explain how d is set to False in a print statement
print(f"The value of d ({d}) is False since 5 is not greater than 7 and 8 is not 'not' less than 20")
assert(d == False) #Do not change this line

print()


print("Code Snippet 5:")

#modify the comparison operator so o evalutes to true
#update the print statement to reflect the changes

m = "GOAT"
n = "goat"

print(ord('g'))
print(ord('G'))

o = (m < n)


print (f"The value of o ({o}) is True since Python uses unicode to define letters as numerical values.")
assert(o == True) #Do not change this line

print()
print("CHALLENGE COMPLETE!")