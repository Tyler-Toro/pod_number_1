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
print("what is your name?")
name = input()
print("hello,"+ name)
# TODO: Write code to ask the client his savings and save it to another variable.
print("May I ask how much is your savings?")
savings = input()
print("Nice!")
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
print("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
stock = input()
print()
print(stock+",is a great choice")

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
# number_of_stocks
# number_of_stocks== (int(savings)/ amazon)
# number_of_stocks=1
# print(number_of_stocks==(int(savings)/amazon))
if stock == "amzn":
    print("excellent choice")
    number_of_stocks = (int(savings) / amazon)
    if number_of_stocks >1:
        print(f"{name} has $ {savings} therefore he can purchase {int(number_of_stocks)} of Amazon")
    elif number_of_stocks<1:
        print("Sorry, you dont have enough savings")
elif stock == "aapl":
    print("excellent choice")
    number_of_stocks = (int(savings) / apple)
    if number_of_stocks >1:
        print(f"{name} has $ {savings} therefore he can purchase {int(number_of_stocks)} of Apple")
    elif number_of_stocks<1:
        print("Sorry, you dont have enough savings")
elif stock == "fb":
    print("excellent choice")
    number_of_stocks = (int(savings) / fb)
    if number_of_stocks >1:
        print(f"{name} has $ {savings} therefore he can purchase {int(number_of_stocks)} of FaceBook")
    elif number_of_stocks<1:
        print("Sorry, you dont have enough savings")
elif stock == "goog":
    print("excellent choice")
    number_of_stocks = (int(savings) / google)
    if number_of_stocks >1:
        print(f"{name} has $ {savings} therefore he can purchase {int(number_of_stocks)} of Google")
    elif number_of_stocks<1:
        print("Sorry, you dont have enough savings")
elif stock == "msft":
    print("excellent choice")
    number_of_stocks = (int(savings) / msft)
    if number_of_stocks >1:
        print(f"{name} has $ {savings} therefore he can purchase {int(number_of_stocks)} of Microsoft")
    elif number_of_stocks<1:
        print("Sorry, you dont have enough savings")
else:
    print("Sorry, Those stocks are not available")

# number_of_stocks= 0
# if stock == "aapl":
#      print("excellent choice")
#     number_of_stocks = (savings / apple)
# elif number_of_stocks >1:
#     print(f"{name} has $ {savings} therefore you can purchase {number_of_stocks} of apple")
# else 
#     print(f"Sorry, don't have enough to buy stocks right now")


'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
if stock=="amzn":
    if number_of_stocks>1:
        print(f"{name} has ${savings} and they can buy {int(number_of_stocks)} of Amazon at the current price of $3000")
elif stock=="aapl":
    if number_of_stocks>1:
        print(f"{name} has ${savings} and they can buy {int(number_of_stocks)} of Apple at the current price of $100")
elif stock=="fb":
    if number_of_stocks>1:
        print(f"{name} has ${savings} and they can buy {int(number_of_stocks)} of FaceBook at the current price of $250")
elif stock=="goog":
    if number_of_stocks>1:
        print(f"{name} has ${savings} and they can buy {int(number_of_stocks)} of Google at the current price of $1400")
elif stock=="msft":
    if number_of_stocks>1:
        print(f"{name} has ${savings} and they can buy {int(number_of_stocks)} of Microsoft at the current price of $200")
print()

