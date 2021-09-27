''' 
## Setup
In your personal folder inside your pod git repo, make a script called `temperature.py` and
 run it using `python temperature.py` to verify you get the expected output.

### The formula for converting between fahrenheit and celsius is to first subtract 32, then
#  multiply by 5/9. Can you do the following in python?

1. Convert a temperature of 100 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_100`, and use `print()` to print out the
     value
    * Is the resulting temperature you get an integer or float? How do you know?
2. Convert a temperature of 0 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_0`, and use `print()` to print out the 
    value
3. Convert a temperature of 34.2 degrees fahrenheit to celsius
    * Do this one all in one print statement **without** saving any variables


### Now, can you convert back?

4. Convert a temperature of 5 degrees celsius to fahrenheit?
5. What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1
 degrees fahrenheit?


### Make sure everything is documented!

6. If you haven't already, go through your script and add a comment for questions 1-5
 explaining what your code is doing.

### Awesome job! Now, add, commit, and push your completed script to your pod Github repo
#  on your branch, then submit a pull request   

**Note: make sure you push to your POD repo where the base version is maintained by your 
TA, not the general JTC repo where the base version is maintained by the `Justice Through
 Code` organization**

Remember, you'll do this from the command line. First add:
```console
$ git add temperature.py
```

Then commit to take a 'snapshot':
```console
$ git commit -m 'adding temperature.py challenge'
```

Then push to the remote online on your branch!

```console
$ git push origin [your_branch_name]
```

Now, go to your pod github repository and make sure the changes have been pushed 
correctly to your branch, then submit a pull request! 

**Congrats! You finished the python bootcamp day1 challenge!!**
'''
# Q1
F = 100
celsius_100 = ((F-32)*5/9)
print(celsius_100)
# Printed out a float because it is a decimal.
# L61 is assigning a value to variable F
# L62 is assigning a formula to varible celsius_100
# L63 prints our answer


# Q2
F = 0
celsius_0 = ((F-32)*5/9)
print(celsius_0)
# Float because there is a decimal
# L71 assigning a value to variable F
# L72 A formula is assigned to the variable

# Q3
print((34.2-32)*5/9)
# Outcome is again a float

# Q4
C=5
Ferenheit_1 =((C*9/5)+32)
print(Ferenheit_1)
# Solution is an Int

# Q5
C=30.2
F=85.1
print((C*9/5)+32)
print(F)
# Celsius is hotter than Ferenheit 86.36>85.1

# Q6