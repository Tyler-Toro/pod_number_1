'''
# Primitive Data Types Challenge 1: Converting temperatures

<img src="https://storage.googleapis.com/ltkcms.appspot.com/fs/yd/images/cover/thermometer-in-snow.base?v=1591222156" width="650">

## Setup
In your personal folder inside your pod git repo, make a script called `temperature.py` and run it using `python temperature.py` to verify you get the expected output. 

### The formula for converting between fahrenheit and celsius is to first subtract 32, then multiply by 5/9. Can you do the following in python?

1. Convert a temperature of 100 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_100`, and use `print()` to print out the value
    * Is the resulting temperature you get an integer or float? How do you know?
2. Convert a temperature of 0 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_0`, and use `print()` to print out the value
3. Convert a temperature of 34.2 degrees fahrenheit to celsius
    * Do this one all in one print statement **without** saving any variables


### Now, can you convert back?

4. Convert a temperature of 5 degrees celsius to fahrenheit?
5. What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?


### Make sure everything is documented!

6. If you haven't already, go through your script and add a comment for questions 1-5 explaining what your code is doing.

### Awesome job! Now, add, commit, and push your completed script to your pod Github repo on your branch, then submit a pull request



**Note: make sure you push to your POD repo where the base version is maintained by your TA, not the general JTC repo where the base version is maintained by the `Justice Through Code` organization**

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

Now, go to your pod github repository and make sure the changes have been pushed correctly to your branch, then submit a pull request!

**Congrats! You finished the python bootcamp day1 challenge!!**
'''
# 1 - Prints out a float 
f = 100
celsius_100 = ((f-32)*5/9)
print(celsius_100)
# Answer is 37.77777
# we are assinging 100 to variable f. Then we are assinging our formula to the variable celsius_100. We then print the results.



# 2 - 
f = 0
celsius_0 = ((f-32)*5/9)
print(celsius_0)
# Answer is -17.77777
# we are assinging 0 to variable c. Then we are assinging our formula to the variable celsius_0. We then print the results.

# 3
print((34.2-32)*5/9)
# Answer is 1.222222
# Here were are not assigning any variables. We are simply printing this formula, which calculates the integers and floats based on PEMDAS

# 4
print(5*9/5+32)
# Answer is 41
# Here were are not assigning any variables. We are simply printing this formula, which calculates the integers and floats based on PEMDAS


# 5
c = 30.2
f = 85.1
print((c*9/5)+32)
print(f)
# Celsius of 86.36 is hotter than Fahrenheit 85.1
# Here we assigned numbers from the question to variables c and f and a forumula to variables and printed both results to compare.

