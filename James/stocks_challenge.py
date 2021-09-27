print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

tsla = 500
gm=750
dowjones = 300

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
Question_One = input('What is your name?')
print(Question_One)
# TODO: Write code to ask the client his savings and save it to another variable.
savings = int(input("what is your amount of savings, {question_one} ?"))
print(savings)
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()
stock_two = str(input("which stock are you interested in? type 'tsla', 'gm' for general motors, 'dow jones' for dow jones industrial"))
print()
print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
# "Your code should look like this:"

# "if stock == amzn:
  
# elif ...
# else ...

convert = int(float(savings / tsla))
convert_two = int(float(savings/ gm))
convert_three = int(float(savings / dowjones))

if stock_two == "tsla":
   print(f"  you are able to purchase ${savings / tsla} of stock")
elif stock_two == "gm":
   print(f"{Question_One} you are able to purchase {savings / gm} of stock.")
elif stock_two == "dow jones":
    print(f"{Question_One} you are able to purchase {savings / dowjones} of stock.")
else:
   print("incorrect syntax, please try again")

#print()

#("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:



# print(f"{question_one} has {savings} and he/she can buy 50 shares of {stock_two} at the price of {savings / tsla}")
# print(f"{question_one} has {savings} and he/she can buy 50 shares of {stock_two} at the price of {savings / gm}")
# print(f"{question_one} has {savings} and he/she can buy 50 shares of {stock_two} at the price of {savings / dow jones}")
# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
#if Stock_two == "tsla":
   # print(f"{Question_One} has {Savings} and is able to purchase {convert} of Tesla stock shares at the price of {tsla}. ")
#elif Stock_two == "gm":
    #print(f"{Question_One} has {Savings} and is able to purchase {convert_two} of General Motors stock shares at the price of {gm}.")
#elif Stock_two == "dowjones":
    #print(f"{Question_One} and is able to purchase {convert_three} of Dow Jones Industrial stock shares at the price of {dowjones}.")
# else: