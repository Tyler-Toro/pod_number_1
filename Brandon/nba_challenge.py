# Q2.1
Jamal_M=46
Fred_VV=43
James_H=37
# assigned variables for the various players
# 3-point shots made for the players

# Q2.2
print(f'Jamal Murry {Jamal_M} \nFred VanVleet {Fred_VV} \nJames Harden {James_H}')
# a bit long, but as I learn it will be better
# used 'f' string to run function

# Q2.3
Jamal_M_2=93
Fred_VV_2=110
James_H_2=109
# assigned variables for the various players
# 3-point shots attempted for the players


# Q2.4
print(f'Jamal Murry {Jamal_M},{Jamal_M_2} \nFred VanVleet {Fred_VV},{Fred_VV_2} \nJames Harden {James_H},{James_H_2}')
# made and 'f' string to list the variables
# read the directions carefully this time and realized 
# you may have wanted multipule print statements
# need to know if this is ok?

# Q2.5
print(f'Jamal Murry {Jamal_M/Jamal_M_2} \nFred VanVleet {Fred_VV/Fred_VV_2} \nJames Harden {James_H/James_H_2}')
# altered previous 'f' string to reflect the players  shooting percentage
# ran function and got floats

# Q3.1
print('The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.')
# added line breaks to the paragraph as per the question
# didn't know if you wanted the '*' at the begining and end so I just ommited them

# Q3.2
print('This is a HUGE chunk of text. \nCan you add **escape characters** to print out this text from a python script to the command line so that only one sentence is on each line?'.upper())
# was a tad confused here know not if the period's seperated the lines 
# or if you wanted me to add period's so I just left as is
# added line breaks after the periods and the upper command to complete the question

# Q3.3
lakers_are_best=True
print(f'The Lakers are the best basketball team in the NBA \n{lakers_are_best}')
# assigned boolean variable
# I would like to see how the rest of the trades go, but decent answer for now

# Q3.4
lakers_are_best= int(True)
print(lakers_are_best)
# did a type conversion to convert boolean variable
'''It takes this value because True has a value of 1 and false has a value of 0'''
lakers_are_best= float(True)
print(lakers_are_best)
# did a type conversion to convert the boolean variable

# Q3.5
print(str(Jamal_M/Jamal_M_2))
print(str(Fred_VV/Fred_VV_2))
print(str(James_H/James_H_2))
'''I noticed that nothing has changed'''
# converted previous variables into strings

print(int(Jamal_M/Jamal_M_2))
print(int(Fred_VV/Fred_VV_2))
print(int(James_H/James_H_2))
'''Everthing has been zero'd out'''
# converted previous variables into intergers

