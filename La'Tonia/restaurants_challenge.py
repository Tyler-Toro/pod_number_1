print("Challenge: Favorite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. 

Go through the dictionary and print out the following 3 pieces of information about the restaurant: 
1. The latitude and longitude of Four Barrel Coffee 
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. 
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}
print()

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# In f-string, MUST put the dictionary in a literal then chain the key in hard brackets ... and only use single quote marks for f-string
print(restaurant["latitude"])
print(restaurant["longitude"])
print(f'Latitude: {restaurant["latitude"]} and Longitude: {restaurant["longitude"]}')
print()
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# Where appropriate just use the key to input the wording ... not a huge impact but may help with efficiency of overall code
print(f'Complete address for {restaurant["name"]}: {restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]}, {restaurant["zip_code"]}.')
print()
# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(restaurant["url"])
print(f'{restaurant["name"]}\'s URL:  {restaurant["url"]}')
print()

print("Question 2")
# TODO: Choose 3 of your most favorite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favorite_dish: your favorite thing to order at the restaurant (string)

# TODO: Print each dictionary
# This is exactly like school exercise did for JS but for objects and arrays
nyc_fav_res1 = {
    "name": "La'Tonia Mertica Delicioso",
    "address": "13 Satisfied Way",
    "favorite_dish": "Bama's Hot Plate"
}
print(nyc_fav_res1)
print()

nyc_fav_res2 = {
    "name": "Bama's Hot Dish",
    "address": "44 High Ground Place",
    "favorite_dish": "Spicy Cheesesteak"
}
print(nyc_fav_res2)
print()

nyc_fav_res3 = {
    "name": "Jahna Glenn's Set",
    "address": "67 Visionary Grounds East",
    "favorite_dish": "Ouneui"
}
print(nyc_fav_res3) 
print()
# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favorite_dish" : "Chicken BLT Sandwich" }
'''

print()

print("Question 3")
'''
Imagine that any 1 of your most favorite restaurants stopped serving your favorite dish there. 
Remove the 'favorite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favorite_dish' key-value pair from one of your 3 restaurants
# Use parentheses because pop is a method and the function requires parentheses
# Decided to write the word favorite how I am conditioned to write it
nyc_fav_res2.pop("favorite_dish")
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
print(nyc_fav_res2)
print()

print("Question 4")
'''
Imagine that another one of your most favorite restaurants modified its address. 
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant 
# This is simpler than it sounds - remember to take the path of least resistance ... dictionary chained with key updating followed by equal sign and content to replace previous content ... and keep the new content in proper format i.e. string versus integer
nyc_fav_res3[ "address"] = "88 Downaround Court, East New Yorkstown 12354"   
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
print(nyc_fav_res3["address"])
print(f'Write this down - new address for {nyc_fav_res3["name"]}: {nyc_fav_res3["address"]}.')
# TODO: Print the updated dictionary.
print(nyc_fav_res3)
print()