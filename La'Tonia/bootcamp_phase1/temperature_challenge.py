# Fahrenheit to Celsius subtract 32 THEN multiply by 5/9
# 5/9 == 0.5555555
# (100 - 32) * 5/9

celsius_100 = (100 - 32) * 5/9
print(celsius_100)
# challenge part 1
# resulting temperature is 37.7778 degrees celsius, which
# is a float (not an integer) because it has a decimal aka
# the result is not a whole number
# this was converted from 100 degrees fahrenheit

celsius_0 = (0 - 32) * 5/9
print(celsius_0)
# challenge part 2
# resulting temperature is -17.7778 degrees celsius
# this was converted from 0 degrees fahrenheit

print((34.2 - 32) * 5/9)
# challenge part 3
# resulting temperature is 1.2222222 degrees celsius
# this was converted from 34.2 degrees fahrenheit

# SWITCHING TO CELSIUS TO FAHRENHEIT
# Celsius to Fahrenheit multiply by 9/5 THEN add 32
# 9/5 == 1.8
# (5 * 9/5) + 32

fahrenheit_5 = (5 * 9/5) + 32
print(fahrenheit_5)
# challenge part 4
# resulting temperature is 41 degrees fahrenheit
# this was converted from 5 degrees celsius

# challenge part 5
# converted 30.2 degrees celsius to fahrenheit equivalent
# celsius = 30.2 == (30.2 * 9/5) + 32 == 86.36 degrees fahrenheit
celsius = (30.2 * 9/5) + 32
print(celsius)

# converted 85.1 degrees fahrenheit to celsius equivalent
# fahrenheit = 85.1 (can see here solution is 30.2 celsius is hotter)
# fahrenheit = 85.1 == (85.1 - 32) * 5/9 == 29.49 degrees celsius
fahrenheit = (85.1 - 32) * 5/9
print(fahrenheit)

# combined parts of challenge part 5 to see comparison
# below code returns true
print(celsius > fahrenheit)

my_f_string = f'In this example, the celsius value of {celsius} is greater than the fahrenheit value of {fahrenheit}'
print(my_f_string)



