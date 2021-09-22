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
client_name = input("Please enter your name: ")

# TODO: Write code to ask the client his savings and save it to another variable.
client_savings = input("Please enter the amount of your savings: ")

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
# the above instruction is confusing to me given the code is/was already written. Commented it out. Rewrote it below. 
# stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
client_stock_interest = input("Which stock would you like to purchase? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. ")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stored in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
# added code below after noting not sure how to separate just calculations from prints for customers... the code below is me trying to separate the two

client_stock_calc = float(client_savings) / (amazon)
if float(client_savings) and 'amzn':
    print(f'Can purchase {client_stock_calc} shares of Amazon stock at the current price of ${amazon})')

elif float(client_savings) and 'aapl':
    print(f'Can purchase {client_stock_calc} shares of Apple stock at the current price of ${apple})')

elif float(client_savings) and 'fb':
    print(f'Can purchase {client_stock_calc} shares of Facebook stock at the current price of ${fb})')

elif float(client_savings) and 'goog':
    print(f'Can purchase {client_stock_calc} shares of Google stock at the current price of ${google})')

elif float(client_savings) and 'msft':
   print(f'Can purchase {client_stock_calc} shares of Microsoft stock at the current price of ${msft})')

else:
    print(f'Can not purchase shares of stock with {client_savings}.')
print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
print()

# please note - and my apologies if this is incorrect - I seemed to combine the last two parts of this exercise which is the reason I have the calculations and prints below ... if possible please show me how I would separate them

if float(client_savings) and 'amzn':
    print(f'{client_name} has ${client_savings} in savings, which puts {client_name} in a financial position to purchase {client_stock_calc} shares of Amazon stock at the current price of ${amazon})')

elif float(client_savings) and 'aapl':
    print(f'{client_name} has ${client_savings} in savings, which puts {client_name} in a financial position to purchase {client_stock_calc} shares of Apple stock at the current price of ${apple})')

elif float(client_savings) and 'fb':
    print(f'{client_name} has ${client_savings} in savings, which puts {client_name} in a financial position to purchase {client_stock_calc} shares of Facebook stock at the current price of ${fb})')

elif float(client_savings) and 'goog':
    print(f'{client_name} has ${client_savings} in savings, which puts {client_name} in a financial position to purchase {client_stock_calc} shares of Google stock at the current price of ${google})')

elif float(client_savings) and 'msft':
   print(f'{client_name} has ${client_savings} in savings, which puts {client_name} in a financial position to purchase {client_stock_calc} shares of Microsoft stock at the current price of ${msft})')

else:
    print(f'Your savings of ${client_savings} is not enough to purchase stock at this time.')
print()



# code below from trying to code int and float separately. .. ultimately used float per search results showing division always results in float
# apple_stock_calc_int = (int(client_savings) / apple)
# apple_stock_calc_flt = (float(client_savings) / apple)

# fb_stock_calc_int = (int(client_savings) / fb)
# fb_stock_calc_flt = (float(client_savings) / fb)

# google_stock_calc_int = (int(client_savings) / google)
# google_stock_calc_flt = (float(client_savings) / google)

# msft_stock_calc_int = (int(client_savings) / msft)
# msft_stock_calc_flt = (float(client_savings) / msft)
