print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input("What is your name?")

# TODO: Write code to ask the client his savings and save it to another variable.
saving = input("How much is in your savings?")

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations, Challenge 3.2.3: Output for the user the result")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.


if stock == "amzn":
    number_stocks = int(saving) / amazon 
    if number_stocks >=1:
        print(f"{name} has ${saving} and can purchase {number_stocks} shares at the current price of ${amazon} ")
    else:
        print('You are too broke to purchase with this company!')

elif stock == "aapl":
    number_stocks = int(saving) / apple
    if number_stocks >=1:
        print(f"{name} has ${saving} and can purchase {number_stocks} shares at the current price of ${apple} ")
    else:
        print('You are too broke to purchase with this company!')

elif stock == "fb":
    number_stocks = int(saving) / fb
    if number_stocks >=1:
        print(f"{name} has ${saving} and can purchase {number_stocks} shares at the current price of ${fb} ")
    else:
        print('You are too broke to purchase with this company!')

elif stock == "goog":
    number_stocks = int(saving) / google  
    if number_stocks >=1:
        print(f"{name} has ${saving} and can purchase {number_stocks} shares at the current price of ${google} ")
    else:
        print('You are too broke to purchase with this company!')

elif stock == "msft":
    number_stocks = int(saving) / msft  
    if number_stocks >=1:
        print(f"{name} has ${saving} and can purchase {number_stocks} shares at the current price of ${msft} ")
    else:
        print('You are too broke to purchase with this company!')
     


