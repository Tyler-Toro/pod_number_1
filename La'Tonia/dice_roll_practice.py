'''
practice project courtesy favtutor:
https://favtutor.com/blog-details/7-Python-Projects-For-Beginners
'''

# adds functionality of randomly generated numbers
import random
# assigns x value of string y aka letter y
x = "y"
# while loop for x being equal to string y/letter y
# then prints five results each for numbers 1 to 6 as set as the parameters inclusive of 1 and 6 using the random keyword and random integer method
while x == "y":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")

# accepts input by user of strings only (i.e. y or n)
# user can roll dice as long as they want
    x = input("Press y to roll dice again. Press n to stop: ")
# line break inside of otherwise empty print statement to add padding between outputs
    print("\n")
