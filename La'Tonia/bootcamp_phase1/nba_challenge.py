'''
ranked #1 Jamal Murray = 46 successful three-pointers
ranked #2 Fred VanVleet = 43 successful three-pointers
ranked #3 James Harden = 37 successful three-pointers
'''

print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable below for number of 3 pt shots made by Fred VanVleet
fred_vanvleet_3pts_made = 43
# TODO: Create variable below for number of 3 pt shots made by James Harden
james_harden_3pts_made = 37
# below print statement inserts a newline/break
# I was using '\n' for a newline/break but without success
print()

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} three-point shots.\n")
# TODO: Create print statement below for Fred VanVleet
print(f"Fred VanVleet dunked a major upset in the 2020 NBA playoffs\nwhen he seemed to re-materialize in a fury of basketball masterfulness\nand add to the records an entry under his name for {fred_vanvleet_3pts_made} three-point shots.\n")
# TODO: Create print statement below for James Harden
print(f"The 2020 NBA Playoffs offered a triple 3-point-shots treat. And\npolishing off the tremendous talent from the rear was James Harden\n- with {james_harden_3pts_made} three-point shots.\n")
print()

'''
ranked #1 Jamal Murray = three-pointers made 46 v. attempted 93
ranked #2 Fred VanVleet = three-pointers made 43 v. attempted 110
ranked #3 James Harden = three-pointers made 37 v. attempted 109
'''
print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable below for number of 3 pt shot attempts by Jamal Murray
jamal_murray_3pts_attempted = 93
# TODO: Create variable below for number of 3 pt shot attempts by Fred VanVleet
fred_vanvleet_3pts_attempted = 110
# TODO: Create variable below for number of 3 pt shot attempts by James Harden
james_harden_3pts_attempted = 109
# Do I Need This print() function which was already in the code?
print()

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."

print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} three-point shots of the {jamal_murray_3pts_attempted} three-point shots he tried to make.\n")
# TODO: Create print statement below for Fred VanVleet
print(f"Fred VanVleet dunked a major upset in the 2020 NBA playoffs\nwhen he seemed to re-materialize in a fury of basketball masterfulness\nand add to the records an entry under his name for {fred_vanvleet_3pts_made} three-point shots.\nIn total, VanVleet tried to slam {fred_vanvleet_3pts_attempted} three-point shots.\n")
# TODO: Create print statement below for James Harden
print(f"The 2020 NBA Playoffs offered a triple 3-point shots treat. And\npolishing off the tremendous talent from the rear was James Harden\n- with {james_harden_3pts_made} three-point shots. Harden actually played to try to get\na total of {james_harden_3pts_made} three-pointers.\n")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# 3 POINT SHOTS PERCENTAGE == made divided by attempted == made/attempted
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
print("Jamal Murray 3-Point-Shot Percentage:")
print(jamal_murray_3pts_made / jamal_murray_3pts_attempted)
print()

# TODO: Calculate and print the 3 point percentage for Fred VanVleet
print("Fred VanVleet 3-Point-Shot Percentage:")
print(fred_vanvleet_3pts_made / fred_vanvleet_3pts_attempted)
print()

# TODO: Calculate and print the 3 point percentage for James Harden
print("James Harden 3-Point-Shot Percentage:")
print(james_harden_3pts_made / james_harden_3pts_attempted)
print()

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\nThose three have made good developments with the Pelicans, especially Brandon Ingram.\nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\nThe Lakers ended the season atop the Western Conference with a record of 49-14.\nThey were narrowly behind the Bucks for the best record in the league.\nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.\n")

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, print out the paragraph with only 1 sentence per line, and all in upper case
var_paragraph = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\nThose three have made good developments with the Pelicans, especially Brandon Ingram.\nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\nThe Lakers ended the season atop the Western Conference with a record of 49-14.\nThey were narrowly behind the Bucks for the best record in the league.\nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
print(var_paragraph.upper())
print()

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers
lakers_are_best = True
print(f'In my opinion, it is {lakers_are_best} the Lakers are the best\nbasketball team. I grew up with a sense of community pride centered around\nthe Lakers. Still, in general, I am not a sports fan.\n')

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out.
lakers_are_best = int(lakers_are_best)
print(lakers_are_best)
print()
# the above code results in a numeric value of 1 because the assignment to the variable is truthy - truthy values have a value of 1

# TODO: Convert your `lakers_are best` variable to a float, and print it out
lakers_are_best = float(lakers_are_best)
print(lakers_are_best)
print()
# the above code results in a numeric value of 1.0 because the assignment to the variable is truthy (truthy == value of 1) AND a float - floats always include a decimal and in this case the decimal zero is added to denote the value is a float

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
# what I notice about the three conversions to type string below is that each percentage still looks like a numeric value - in other words, I notice that there is no indication that they are string types

print("Jamal Murray 3-Point-Shot Percentage:")
print(str(jamal_murray_3pts_made / jamal_murray_3pts_attempted))
print(type(str(jamal_murray_3pts_made / jamal_murray_3pts_attempted)))
print()

# TODO: Calculate and print the 3 point percentage for Fred VanVleet
print("Fred VanVleet 3-Point-Shot Percentage:")
print(str(fred_vanvleet_3pts_made / fred_vanvleet_3pts_attempted))
print(type(str(fred_vanvleet_3pts_made / fred_vanvleet_3pts_attempted)))
print()

# TODO: Calculate and print the 3 point percentage for James Harden
print("James Harden 3-Point-Shot Percentage:")
print(str(james_harden_3pts_made / james_harden_3pts_attempted))
print(type(str(james_harden_3pts_made / james_harden_3pts_attempted)))
print()

# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
# what I notice about the three conversions to type integer below is that each percentage is represented as number zero - all numeric value after the decimal is lost and the conversion does not factor in rounding the actual percentage which has value despite being less than zero 
print("Jamal Murray 3-Point-Shot Percentage:")
print(int(jamal_murray_3pts_made / jamal_murray_3pts_attempted))
print(type(int(jamal_murray_3pts_made / jamal_murray_3pts_attempted)))
print()

# TODO: Calculate and print the 3 point percentage for Fred VanVleet
print("Fred VanVleet 3-Point-Shot Percentage:")
print(int(fred_vanvleet_3pts_made / fred_vanvleet_3pts_attempted))
print(type(int(fred_vanvleet_3pts_made / fred_vanvleet_3pts_attempted)))
print()

# TODO: Calculate and print the 3 point percentage for James Harden
print("James Harden 3-Point-Shot Percentage:")
print(int(james_harden_3pts_made / james_harden_3pts_attempted))
print(type(int(james_harden_3pts_made / james_harden_3pts_attempted)))
print()

# below code is a bonus for myself to practice rounding
# TODO: Calculate and print the 3 point percentage for James Harden
james_harden_3pts_made_rnd = round(james_harden_3pts_made / james_harden_3pts_attempted, 3)
print("James Harden 3-Point-Shot Percentage:")
print(james_harden_3pts_made_rnd)


