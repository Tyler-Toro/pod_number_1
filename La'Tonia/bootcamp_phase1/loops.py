# FOR LOOP w/LIST
pod0_peeps = ['Who\s', 'Where', 'Now', "How", 'What']
pod1_peeps = ['Brandon', 'Anthony', "Jessy", 'Tyler', "Jason", 'James', "La'Tonia"]

# Lol ... works but positive this is a continuous loop ... DO NOT RUN CODE BELOW
# for peep in pod1_peeps:
#     pod1_peeps.append(peep.upper())
#     print(pod1_peeps)
#     print()


#Remember the name after for can be any name as long as remain consistent i.e. use same name in print statement
for peep in pod0_peeps:
    pod1_peeps.append(peep.upper())
    print(pod1_peeps)
    print()


# Loop through characters in a string
random_string = 'he went there then he came back because she couldn\'t find the sentence about the quck fox'
for letter in random_string:
    print(letter)

my_string_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for letter in my_string_vowels:
    if letter in my_string_vowels:
        print(f'{letter} is a vowel - yes, even letter y')
    else:
        print(f'{letter} is not a vowel')

# WHILE LOOP
count = 0
while (count <= 7):
    print(count)
    count = count + 1
    print('DONE!')