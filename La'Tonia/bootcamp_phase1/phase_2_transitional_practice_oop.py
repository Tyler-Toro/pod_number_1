# WILL TRY TO REVISIT THIS - TREATED AS SCRATCHPAD AFTER PRINT STATEMENTS NO-GO
# Revisited and code working ... seems to have been a scoping issue

from pprint import pprint


# to date we've worked with procedural programming as noted below
tyler = {
    'name': 'Tyler',
    'bio': 'Pod 1 Leader',
    'tweets': ['Pod 1 is the best pod, naturally!', 
    'When you practice, code things happen']
}

def add_tweet(user, text):
    user['tweets'].append(text)

add_tweet(tyler, 'OOP is awesome - do not run away. We git this! We got this!')

print('\nPRINTS ONLY FIRST TWEET')
print(tyler['tweets'][0])
# print all tweets - in dict for variable tyler and appended
# also print all pretty/prettier than standard output
print('\nPRINTS ALL TWEETS AND PRETTIER THAN STANDARD OUTPUT')
pprint(tyler['tweets'])
# print formatted per f-string
# notice rogue single quote after word include in output 
print('\nPRINTS FORMATTED PER F-STRING USING DOUBLE QUOTES TO AVOID STRING-USE ISSUES')
pprint(F"{tyler['name']} is {tyler['bio']}. He likes to tweet about his pod. His tweets include {tyler['tweets']}")
print()


# this is powerful stuff, still much more flexibility comes with object-oriented programming ... buckle in
print('\nJTC PHASE 2: OBJECT-ORIENTED PROGRAMMING')
print('~keyword class, class name, parentheses, colon~')
print(' WRITTEN AS class Person(): ')
print('#############################################\n')

# creates class - once and done
class Person():

# initialization fn - set attributes for the class
# object creation process is instantiating a class
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'Good Day, you\'re listed as {self.name} - is that you?'

person0 = Person('Evelyn Pearls')

print('\nPRINTS NAME OF SPECIFIED PERSON INSTANTIATED AS PERSON0')
print(person0.name)
print()


# practice simple print statements using class Person and name - limitless instantiation
print('\nPRINTS 5 NAMES OF SPECIFIED PERSONS INSTANTIATED SEPARATELY')
person1 = Person('Mattanis Shynnes')
print(person1.name)
person2 = Person('Anthony Brandon')
print(person2.name)
person3 = Person('Tyler Jessy')
print(person3.name)
person4 = Person('James Jason')
print(person4.name)
person5 = Person('La\'Tonia Mertica')
print(person5.name)

person6 = Person('Debra Anne Wintynn')
print(person6.name)
print()

# attempting same from one print statement
# first attempt returned objects on separate lines with hexacode locations
print('\nPRINTS SAME FROM ONE PRINT STATEMENT')
print(F"{tyler['name']}, {tyler['bio']}, guides full stack python code hopefuls: -{person0}\n -{person1}\n -{person2}\n -{person3}\n -{person4}\n -{person5} ")
print()

# second attempt ... duh - forgot to add .name aka target info want to output
print('\nPRINTS SAME FROM ONE PRINT STATEMENT')
print(F"{tyler['bio']} {tyler['name']} mentors ful stack python coding hopefuls:\n - {person0.name}\n - {person1.name}\n - {person2.name}\n - {person3.name}\n - {person4.name}\n - {person5.name} ")
print()

# syntax for method <object>.method_name() aka def greeting(self) - must w/in the class meaning s/b as noted above on line 28 
print('\nPRINTS GREETING FOR PERSON6')
print(person6.greeting())
print()

# comparing structure ... Person object at hexacode memory address v. class main dot Person v. True 
print('\nPRINTS PERSON OBJECT WITH HEXACODE ADDRESS v PERSON CLASS v TRUE\nTO ILLUSTRATE THESE TWO OBJECTS EQUAL IN THIS CODE SITUATION')
print(person6)
print(type(person6))
print(type(person6) == Person)
print()


# adding more attributes - must add to initialization fn and pass in as additional parameters THEN add into fn itself
class Professional():
    def __init__(self, name, title, duties):
        self.name = str(name)
        self.title = str(title)
        self.duties = int(duties)
    
    def greeting(self):
        return f"Welcome, my name is {self.name} - my title is {self.title} and I have {self.duties} duties."

# method to modify info in a class - best when do not know info being added in advance
class Cart():
    def __init__(self):
        self.items = []

    def add(self, label, price):
        item = {}
        item['label'] = label
        item['price'] = price
        self.items.append(item)

    def total(self):
        cart_total = 0
        for item in self.items:
            cart_total += item['price']
        return f"${cart_total}"

cart = Cart()

cart.add("Wafers", 7)
cart.add("Turk Burgs", 13)
cart.add("Bottled Happiness", 144)
cart.add("Perfect Endings", 247)
cart.add("Wedge-Cut Taters", 11)
cart.add("Spicy Sauce", 3)
cart.add("Juice", 24)

# items is not written as fn items() below because this items is an attribute of the class aka a variabe w/in the class
print('\nPRINTS ALL ITEMS IN CART PRETTY FORMATTED')
pprint(cart.items)
print()

# total() is a method in the class aka a function that adds stuff in which is the reason need the parentheses
print('\nPRINTS TOTAL FOR ITEMS IN CART')
# print(cart.total())
print(f'TOTAL COST: ${cart.total()}')
print()

# classes allow for setting attributes outside initialization function
# setting attributes outside of the init fn sets a global attribute meaning it is auto added to all added to the class
# setting attributes outside init fn means initializing the variable outside the init fn


class Person():
    title = 'Communication Specialist'
    start_date = '11 February 2023'
    duties = 44

    def __init__(self, name, title, duties):
# startdate will be added to all persons added to the class
        self.name = str(name)
        self.title = str(title)
# commented out to figure our where duties being passed from into the f-string - clearly not from here ... when comment back in need to add title as attribute in parens line 163 ... duties works per the global attribute initialized outside the parent class
        # self.duties = int(duties)

    def greeting(self, title, duties):
        self.title = title
        self.duties = duties
        return f"Howdy. My name is {self.name}. The blurby title I use is {self.title}.\nAt least {self.duties} duties weigh on my daily obligations. I love doing it, though."

# prints the person object with its hexacode address ... wanted address
    person = Person('La\'Tonia Mertica')
    person = Person(name='La\'Tonia Mertica')

    print('\nPRINTS NAME ONLY')
    print(person.name)
    print()

    print('\nPRINTS STRING WITH ALL ATTRIBUTES')
    print(f'{person.name}, {title}, specializes in {duties} areas. She\'s been building expertise since {start_date}.')

    print('\nPRINTS THE GREETING FROM GREETING FUNCTION')
    print(greeting(person, title='Comms Fanatic', duties=44))   
    print()


# final comment - I worked through this file addressing errors throughout by referencing my notes and hints in the error message/stack trace ... proud of myself ... still bit wonky with some stuff ... given I went from having no print statements at ALL from this file to everything noew works, time and energy and hope well vested



