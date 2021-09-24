print("Challenge 2.1:")

# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
jamal_murray_3pts_made = 46

# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
fred_vanfleet_3pts_made = 43

# TODO: Create variable here for number of 3 pt shots made by James Harden
james_harden_3pts_made = 37


print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")

# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanfleet_3pts_made} 3 point shots")

# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")


print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")

# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
jamal_murray_3pts_attempts = 93


# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
fred_vanfleet_3pts_attempts = 110


# TODO: Create variable here for number of 3 pt shot attempts by James Harden
james_harden_3pts_attempts = 109


print()

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {jamal_murray_3pts_attempts} shot attempts")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanfleet_3pts_made} 3 point shots and {fred_vanfleet_3pts_attempts} shot attempts")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots and {james_harden_3pts_attempts} shot attempts")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`

# TODO: Calculate and print the 3 point percentage for Jamal Murray
murray_three_point_per = {jamal_murray_3pts_made / jamal_murray_3pts_attempts}
print(f"In the 2020 NBA playoffs, Jamal Murray had a 3 point percentage of {murray_three_point_per} ")

# TODO: Calculate and print the 3 point percentage for Fred VanVleet
fred_vanfleet_three_point_per = {fred_vanfleet_3pts_made / fred_vanfleet_3pts_attempts}
print(f"In the 2020 NBA playoffs, Fred VanVleet had a 3 point percentage of {fred_vanfleet_three_point_per}")

# TODO: Calculate and print the 3 point percentage for James Harden
james_harden_three_point_per = {james_harden_3pts_made / james_harden_3pts_attempts}
print(f"In the 2020 NBA playoffs, James Harden had a 3 point percentage of {james_harden_three_point_per} ")
print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line

murray_three_point_per = {jamal_murray_3pts_made / jamal_murray_3pts_attempts}
print(f"In the 2020 NBA playoffs, Jamal Murray had a 3 point percentage of {murray_three_point_per} ") \

fred_vanfleet_three_point_per = {fred_vanfleet_3pts_made / fred_vanfleet_3pts_attempts}
print(f"In the 2020 NBA playoffs, Fred VanVleet had a 3 point percentage of {fred_vanfleet_three_point_per} ")\

james_harden_three_point_per = {james_harden_3pts_made / james_harden_3pts_attempts}
print(f"In the 2020 NBA playoffs, James Harden had a 3 point percentage of {james_harden_three_point_per} ")\

print()

print('Challenge 3.2: Print out the paragraph in upper case')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case

murray_three_point_per = {jamal_murray_3pts_made / jamal_murray_3pts_attempts}
print(f"In the 2020 NBA playoffs, Jamal Murray had a 3 point percentage of {murray_three_point_per} ".upper()) \

fred_vanfleet_three_point_per = {fred_vanfleet_3pts_made / fred_vanfleet_3pts_attempts}
print(f"In the 2020 NBA playoffs, Fred VanVleet had a 3 point percentage of {fred_vanfleet_three_point_per} ".upper()) \

james_harden_three_point_per = {james_harden_3pts_made / james_harden_3pts_attempts}
print(f"In the 2020 NBA playoffs, James Harden had a 3 point percentage of {james_harden_three_point_per} ".upper()) \

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
lakers_are_best = False 

# TODO: print out the variable in an f-string to convey your opinion on the lakers
print(f"Do I believe the Lakers are the best team in the NBA? My answer: {lakers_are_best}")
print()

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
lakers_are_best = int(False) 
print(lakers_are_best)
print()

# TODO: Convert your `lakers_are best` variable to a float, and print it out
lakers_are_best = float(False) 
print(lakers_are_best)
print()

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.

my_string1 = str(murray_three_point_per)
murray_three_point_per = {jamal_murray_3pts_made / jamal_murray_3pts_attempts}
print(f"In the 2020 NBA playoffs, Jamal Murray had a 3 point percentage of {my_string1} ")


my_string2 = str(fred_vanfleet_three_point_per)
fred_vanfleet_three_point_per = {fred_vanfleet_3pts_made / fred_vanfleet_3pts_attempts}
print(f"In the 2020 NBA playoffs, Fred VanVleet had a 3 point percentage of {my_string2} ")

my_string3 = str(james_harden_three_point_per)
james_harden_three_point_per = {james_harden_3pts_made / james_harden_3pts_attempts}
print(f"In the 2020 NBA playoffs, James Harden had a 3 point percentage of {my_string3} ")
print()


#  TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.



print(int(jamal_murray_3pts_made / jamal_murray_3pts_attempts))
print(type(int(jamal_murray_3pts_made / jamal_murray_3pts_attempts)))


print(int(fred_vanfleet_3pts_made / fred_vanfleet_3pts_attempts))
print(type(int(fred_vanfleet_3pts_made / fred_vanfleet_3pts_attempts)))


print(int(james_harden_3pts_made / james_harden_3pts_attempts))
print(type(int(james_harden_3pts_made / james_harden_3pts_attempts)))
