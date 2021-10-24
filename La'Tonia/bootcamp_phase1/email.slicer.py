# accept user input and remove white space with strip fn/method ... line 5
print('\nDIVIDE EMAIL INTO TWO STRINGS')
print('~uses @ symbol as separater~\n')

email = input('Enter Email: ').strip()

# finds index of @ symbol from user input
username = email[:email.index("@")]
# stores index of @ symbol in variable domain_name to split email in two
domain_name = email[email.index('@')+1:]

# sets how to display output
format_ = (f'\nUsername: {username}\nDomain: {domain_name}\n')

print(format_)