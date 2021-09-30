# Added pretty print for practice and more ease in reviewing the code
from pprint import pprint 

# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

print('Question 1')
employee_name = 'Ash Rahman'

# You have decided the format of the email should be: Ash Rahman -> ash.rahman@ripplemedia.com
# Let's write some code that converts a name into an email id that matches this format
# 1.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name'
# .lower method changes all string characters to lowercase
lower_name = employee_name.lower()
print(lower_name)
print()

# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list'
# split makes most sense. still, we did something similar using .join so wonder if join method is a solid option
# in this use case split method creates two separate lists from the split string - one list for each name (first v. last) in the string
names_list = lower_name.split(' ')
print(names_list)
print()

# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names'
# join method feels awkward at first because have empty strings - that may or may not fill with a symbol or text etc. - connected to period symbol then parens to finish the method ... and odd that auto fill does not include the parens - we can auto select the method but have to add the parens at the end
# line 28 re-combines the first and last name anchored to a period symbol between them 
joined_names = '.'.join(names_list)
print(joined_names)
print()

# 1.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email'
# simpler than thought given just use + symbol to concatenate ... must be way to also achieve result using a for loop
email = joined_names + '@ripplemedia.com'
print(email)
print()

print('Question 2')

# Congratulations! Your team is expanding. Below is a list of their names:
# now imagine this list has hundreds and thousands of names - the magic is really felt then
names = ['Max Bartlett', 'Angelita Norris', 'Stewart Mueller', 'Dominique Henry', 'Carmela Gross', 'Bettie Mcmillan', 'Sara Ellison', 'Ira Anthony', 'Pauline Riley', 'Ben Weber',
         'Joanne Mcknight', 'Loren Gould', 'Jamar Singh', 'Amanda Vance', 'Tyrell Andrade', 'Jana Clements', 'Eddy Mcbride', 'Marsha Meyer', 'Elbert Shannon', 'Alyce Hull']

emails = []


# We want to convert all their names into the same format from Question 1
# basically go step by step from what did above and combine into code block below while using a for loop

# 2.1 TODO: Use a "for" loop to go over each name in the names list
# 2.2 TODO: Inside the "for" loop, create the email id by re-using the logic from Question 1 and...
# 2.3 TODO: ..add the email to the emails list

for name in names:
    lower_name = name.lower()
    names_list = lower_name.split(' ')
    joined_names = '.'.join(names_list)
    email = joined_names + '@ripplemedia.com'
    emails.append(email)
    print()     

    # print(lower_name) ... to check what code is doing at this stage
    # print(names_list) ... to check what code is doing at this stage
    # print(joined_names) ... to check what code is doing at this stage

    # used pretty print for print statement below because returned result is a big block of text/characters
    # realize now that for each loop the returned results adds a name to the content ... lol
    pprint(emails) 
