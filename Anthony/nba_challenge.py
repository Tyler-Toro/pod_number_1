print("Challenge 2.1:")
jamal_murray_3pts_made = 46


# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
Fred_VanVleet_3pts_made = 10  #AC: created a variable Fred_VanVleet_3pts_made and defined it as 10

# TODO: Create variable here for number of 3 pt shots made by James Harden
Harden_3pts = 20 #AC: created a variable Harden_3pts and defined it as 20

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots, Fred VanVleet made {Fred_VanVleet_3pts_made}, and James Harden made {Harden_3pts}.")
#AC: I used the f-function to create this print statement, which pulls the shots made based on how I declared the variables. 


# TODO: Create print statement here for Fred VanVleet
print(Fred_VanVleet_3pts_made)
print()

# TODO: Create print statement here for James Harden
print(Harden_3pts)
print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
jamal_attempts = 50

# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
fred_attempts = 25

# TODO: Create variable here for number of 3 pt shot attempts by James Harden
harden_attempts = 10
print()

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f'In the 2020 NBA playoffs, Jamal Murray made {jamal_attempts} 3 point shot attempts, Fred VanFleet made {fred_attempts}, and James Harden made {harden_attempts}.')
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray



jamal_percent = jamal_murray_3pts_made / fred_attempts
print(jamal_percent)
print(type(jamal_attempts))


# TODO: Calculate and print the 3 point percentage for Fred VanVleet
fred_percent = Fred_VanVleet_3pts_made / fred_attempts
print(fred_percent)
print(type(fred_attempts))



# TODO: Calculate and print the 3 point percentage for James Harden
harden_percent = Harden_3pts / harden_attempts
print(harden_percent)
print(type(harden_percent))



print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
print()

# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print(f'In the 2020 NBA playoffs,\n Jamal Murray made {jamal_attempts} 3 point shot attempts,\n Fred VanFleet made {fred_attempts},\n and James Harden made {harden_attempts}.')
print()

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
print()

# TODO: As above, print out the paragraph with only 1 sentence per line, and all in upper case
print(f'In the 2020 NBA playoffs, Jamal Murray made {jamal_attempts} 3 point shot attempts,\n Fred VanFleet made {fred_attempts},\n and James Harden made {harden_attempts}'.upper())

print()

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')

# TODO: make a variable called `lakers_are_best` to indicate this
lakers_are_best = {False}

print(lakers_are_best)
print()

    #AC: Note to Tyler - I am not sure what to do here. This is my best guess. Google gave some complex results. 

# TODO: print out the variable in an f-string to convey your opinion on the lakers
print(f'It is {lakers_are_best} that the Lakers are the best team.')
print()

print('Challenge 3.4: Type Conversion')
print()

# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
print(int(50.00))

    #AC: Note to Tyler - I don't understand what the question 3.3 (line 85) is asking, but I am showing here that I know how to turn a variable or float into an integer. 

# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(float(50))

    #AC: Note to Tyler - I don't understand what the question 3.3 (line 85) is asking, but I am showing here that I know how to turn a variable or integer into an float. 

print()

print('Challenge 3.5: Type Conversion Part 2')

print()

# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.

print(type(str(harden_percent)))

print(type(str(fred_attempts)))

print(type(str(harden_percent)))

print()



# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(type(int(Fred_VanVleet_3pts_made)))
print(type(int(jamal_murray_3pts_made)))
print(type(int(Harden_3pts)))