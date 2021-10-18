# accept user input of text/string
# wrap input in str fn to ensure input translates as text/string
user_input = str(input('Enter Phrase: '))

# use split method to separate each character from user input
text = user_input.split()

# create empty string as assignment for variable for user input to cycle through before output
char = ' '

# create for loop to take each first character in the text/string from user input and change it into a capital letter
for first_char in text:
    char = char + str(first_char[0]).upper()

# output/display the characters that have been isolated
print(f'ACRONYM CREATED: {char}') 