

totes = {
    'the TOTE': {
        'title': 'the La',
        'label': 'the Word',
        'address': 'Ink' 
    },
    'a TOTE': {
        'pronoun': 'a Bag',
        'calling': 'a Tote',
        'name': 'a Carry'
    },
    'TOTE': {
        'nickname': 'backpack',
        'shoutout': 'side straddle',
        'moniker': 'tuck and go'
    }
}

# Print whole dictionary of dictionaries
# Print but notice order of dictionaries is scrambled - is this an intentional feature of python? ... if so is weird choice given it appears to be reverse alpha order
# UPDATE: ran code on wrong version (2 not 3) of python ... printing in correct order now
# This practice helped me re-learn keys must be unique and ensure open and close quotes
print(totes)
print(totes['TOTE']['moniker'])
print(type(totes['TOTE']))
print()

# Update item in a dictionary nested in a dictionary
totes['a TOTE']['calling'] = 'more tote' 
print(totes)
print()

#Remove/Delete item from dictionary nested in a dictionary
totes['TOTE'].pop('nickname')
print(totes)
print()

