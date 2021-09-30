# Pod Leader 6 Brandon kindly introduced us to pretty print - simple and easy ... loOove it!
from pprint import pprint


# Challenge 1
print("Challenge 1: All possible laptops\n")
print("Question 1: You are given a list containing the laptop names. Print the names of each the laptops separately.")
all_laptops = ["Apple MacBook Pro", "Asus Zenbook", "Dell XPS", "Lenovo IdeaPad", "Apple MacBook Air", "Sony Viao"]
print()

# TODO: Write code to print all laptop names
# PL6 Brandon reminded re: .join option ... hope this kind of tucking in from previous lessons continues to happen explicitly
print("All laptop names:")
print('\n'.join(all_laptops))
print(f'''Names of All the Laptops: {' '.join(all_laptops)}''')
print()


# Challenge 2
print("Challenge 2: Buy a laptop")
print("Below is a list of dictionaries of the top 2 laptops of 2020 as reviewed by Tech Crunch. \
    Go through the dictionary and print out the following 3 pieces of information about the laptops: \
    \n1. The url for the Apple Macbook Pro \
    \n2. All possible prices of the 16-inch MacBook Pro. \
    \n3. All the color options for Dell XPS 13. \
    \n4. The description of Dell XPS.")
print()

# Sure I am more loopy re: this data structure than I know because wasn't able to solve color/storage exercise below using straight-forward data structure navigation as I anticipated
laptops = [
        {
            "productName": "Apple Macbook Pro",
            "url": "https://www.apple.com/macbook-pro-13/",
            "types": [
                {
                    "id": "1",
                    "screen_size": "13-inch",
                    "cpu": ["1.4GHz quad-core 8th-generation Intel Core i5 processor", "2.0GHz quad-core 10th-generation Intel Core i5 processor"],
                    "ram": ["8GB","16GB"],
                    "storage": ["256GB SSD","512 GB SSD"],
                    "colors": ["space gray", "silver"],
                    "price": [1299, 1499, 1799]
                },
                {
                    "id": "2",
                    "screen_size": "16-inch",
                    "cpu": ["2.6GHz 6-core 9th-generation Intel Core i7 processor", "2.3GHz 8-core 9th-generation Intel Core i9 processor"],
                    "ram": ["16GB"],
                    "storage": ["512 GB SSD", "1 TB SSD"],
                    "colors": ["space gray", "silver"],
                    "price": [2399, 2799]
                }
            ],
            "description": "If you're after the latest and greatest laptop from Apple, we suggest you look into the 2020 model of the MacBook Pro. The headline Touch Bar – a thin OLED display at the top of the keyboard which can be used for any number of things, whether that be auto-suggesting words as you type or offering Touch ID so you can log in with just your fingerprint – is of course included. It's certainly retained Apple's sense of style, but it comes at a cost. This is a pricey machine, so you may want to consider one of the Windows alternatives. But, if you're a steadfast Apple diehard, this is definitely the best laptop for you!"
        },
        {
            "id": "2",
            "productName": "Dell XPS",
            "url": "https://www.dell.com/en-us/shop/dell-laptops/sr/laptops/xps-laptops?~ck=bt",
            "types": [
                {
                    "id": "3",
                    "screen_size": "13-inch",
                    "cpu": ["11th Generation Intel Core i3-1115G4 Processor", "11th Generation Intel Core i5-1135G7 Processor"],
                    "ram": ["8GB"],
                    "storage": ["256GB SSD","512 GB SSD", "1 TB SSD"],
                    "colors": ["Platinum silver exterior, black interior", "Platinum silver exterior, black interior"],
                    "price": [999, 1099, 1149, 1249]
                },
                {
                    "id": "4",
                    "screen_size": "15-inch",
                    "cpu": ["10th Generation Intel Core i5-10300H"],
                    "ram": ["8GB", "16GB", "32GB", "64GB"],
                    "storage": ["256 GB SSD", "512 GB SSD", "1 TB SSD", "2 TB SSD"],
                    "colors": ["Frost White with White Palmrest", "Frost White with White Palmrest"],
                    "price": [1199, 1299, 1399, 1749, 1999, 2299]
                }
            ],
            "description": "The Dell XPS is an absolutely brilliant laptop. The 2020  version rocks an 11th-generation Intel Core i3, i5 or i7 processor and a bezel-less ‘Infinity Edge’ display. This Dell XPS continues to be the most popular Windows laptop in the world. What’s more, there’s a wide range of customization options, so you can really make the Dell XPS the best laptop for your needs. "
        }
]

# TODO: Write code to print out the MacBook Pro url
print() 
print(laptops[0]["url"])
print(f'MacBook Pro Url: {laptops[0]["url"]}')

# Can also be written as 
# Nice, quick, and simple trick Brandon shared ... I like it because it makes the final effort more streamlined ... Planned to try this for the color/storage exercise but figured if straight-forward approach not working can't see how just adding that code to a variable would work ... essentially the same content reformatted
macbook_dict = laptops[0]
print(laptops[0]["url"])
print()

# TODO: Write code to print all possible prices of the 16-inch MacBook Pro
# Tried various ways to add .join to prices to output $ at start of each price ... succeeded in adding $ at start of each character ... lol
print(f'''Two Price Points for 16-inch MacBook Pro - that\'s a total of {len(laptops[0]["types"][1]["price"])}.''')
print(f'Those Two Price Points: {laptops[0]["types"][1]["price"]}')
print()

# TODO: Write code to print all the color options for Dell XPS 13 
# Instruction above likely means 13-inch
# Printed all color options just in case
print(f'Color Options for 13-inch Dell XPS: {laptops[1]["types"][0]["colors"]}')
print(f'Color Options for 15-inch Dell XPS: {laptops[1]["types"][1]["colors"]}')
print()

# TODO: Write code to print the description of Dell XPS laptop
print(laptops[1]["description"])
print(f'Description for Dell XPS: {laptops[1]["description"]}')
print()


print("Question 2: Out of Stock laptops")
print("Suppose that the 13-inch MacBook Pro in space gray color is sold out. Also, the same laptop with 1 TB storage is out of stock as well. Update the list of dictionaries such that these options are removed. Print the updated dictionary.")
print()

# TODO: Update the laptops dictionary
# Easier to first isolate the targets in output then double back to (try to) delete
# No 1TB in 13-inch MacBook option and modified this question to answer it using the 16-inch option which does have 1TB
# Below len code per trying to figure out reasons two items in list but getting 'out of range' error when try to print
print(f'Total Items in Colors List: {len(laptops[0]["types"][0]["colors"])}')
print(f'13-inch MacBook Color Options: {laptops[0]["types"][0]["colors"]}')
print(f'13-inch MacBook Color Option Need to Delete: {laptops[0]["types"][0]["colors"][0]}')
laptops[0]["types"][0]["colors"][0]
print()

print(f'Total Items in Storage List: {len(laptops[0]["types"][1]["colors"])}')
print(f'16-inch MacBook Storage Options: {laptops[0]["types"][1]["storage"]}')
print(f'16-inch MacBook Storage Option Need to Delete: {laptops[0]["types"][1]["storage"][1]}')
laptops[0]["types"][1]["storage"][1]
print()

# Below code starting on lines 150 and 154 to update dictionaries to fulfill this assignment exercise
pprint(laptops[0]["types"][0]["colors"][0])
print(laptops[0]["types"][1]["storage"][1])
print()

# Below code didn't return removal of specified item
# laptops[0]["types"][0].pop(["colors"][0])
# pprint(laptops)

# # Below code throws error - index out of range, makes no sense to me given the current data structure ... What am I missing?
# laptops[0]["types"][1].pop(["storage"][1])
# pprint(laptops)
# print()

# TODO: Print the new dictionary
# I've moved this .pop all through these print statements to try to figure out the issue
# First two print statements below (commented out) still no-go ... any insight appreciated
# print(laptops[0]["types"][0]["colors"].pop([0]))
# print(laptops[0]["types"][1]["storage"].pop([1]))

# Below code per re-try with code example provided by Tyler ... which I think answers my 'what am I missing' and 'any insight appreciated' comments above
apple_macbook_pro = [
        {
            "productName": "Apple Macbook Pro",
            "url": "https://www.apple.com/macbook-pro-13/",
            "types": [
                {
                    "id": "1",
                    "screen_size": "13-inch",
                    "cpu": ["1.4GHz quad-core 8th-generation Intel Core i5 processor", "2.0GHz quad-core 10th-generation Intel Core i5 processor"],
                    "ram": ["8GB","16GB"],
                    "storage": ["256GB SSD","512 GB SSD"],
                    "colors": ["space gray", "silver"],
                    "price": [1299, 1499, 1799]
                },
                {
                    "id": "2",
                    "screen_size": "16-inch",
                    "cpu": ["2.6GHz 6-core 9th-generation Intel Core i7 processor", "2.3GHz 8-core 9th-generation Intel Core i9 processor"],
                    "ram": ["16GB"],
                    "storage": ["512 GB SSD", "1 TB SSD"],
                    "colors": ["space gray", "silver"],
                    "price": [2399, 2799]
                }
            ]
        }
]

print(f'APPLE MACBOOK PRO COLORS: {apple_macbook_pro[0]["types"][0]["colors"]}')
print(f'APPLE MACBOOK PRO STORAGE: {apple_macbook_pro[0]["types"][1]["storage"]}')
print()

# Below code per re-try and is no-go ... I need help understanding ... following uncommented code block works but I may still benefit from walk through of Tyler's example for better understanding
# apple_macbook_pro["colors"] = apple_macbook_pro.get('colors')
# print(apple_macbook_pro['colors'])
# apple_macbook_pro["storage"] = apple_macbook_pro.get('storage')
# print(apple_macbook_pro['storage'])

# Another re-try ... WORKS!!!
print(apple_macbook_pro[0]["types"][0]["colors"])
apple_macbook_pro[0]["types"][0]["colors"].remove("space gray")
print(f'If the above remove method works then this line will return no space gray in the colors. This line returns: {apple_macbook_pro[0]["types"][0]["colors"]}')
print(f'This is the dictionary: Type {type(apple_macbook_pro[0]["types"][0])}')
print(f'This is the list nested in the dictionary: Type {type(apple_macbook_pro[0]["types"][0]["colors"])}')
print()

print(apple_macbook_pro[0]["types"][1]["storage"])
apple_macbook_pro[0]["types"][1]["storage"].remove("1 TB SSD")
print(f'If the above remove method works then this line will return no 1 TB SSD in the storage options. This line returns: {apple_macbook_pro[0]["types"][1]["storage"]}')
print(f'This is the dictionary: Type {type(apple_macbook_pro[0]["types"][1])}')
print(f'This is the list nested in the dictionary: {type(apple_macbook_pro[0]["types"][1]["storage"])}')
print()

# These two prints statements work, but I feel like this is a hacky workaround (I did before trying to follow Tyler's example)
laptops[0]["types"][0]["colors"] = "silver"
print(f'Given there are multiple means to answer any given code question, I hope it suffices that I arrived at the answer for this exercise - meaning the print statement only reflects "{laptops[0]["types"][0]["colors"]}" - using this code way.')
print()

laptops[0]["types"][1]["storage"] = "512 GB SSD"
print(f'This print statement should only reflect "{laptops[0]["types"][1]["storage"]}" as the answer. As such, I hope it is satisfactory that I coded this answer how I have.')
print()

print("Question 3: listing all the prices")
print("Time to look at the range of prices. Print out all possible computer prices")
print()

# TODO: print out all possible prices for the laptops
print(f'Price Options for 13-inch MacBook Pro: {laptops[0]["types"][0]["price"]}')
print(f'Price Options for 16-inch MacBook Pro: {laptops[0]["types"][1]["price"]}')
print(f'Price Options for 13-inch Dell XPS: {laptops[1]["types"][0]["price"]}')
print(f'Price Options for 15-inch Dell XPS: {laptops[1]["types"][1]["price"]}')