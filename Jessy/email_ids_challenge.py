# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

print('Question 1')
employee_name = 'Ash Rahman'

# You have decided the format of the email should be: Ash Rahman -> ash.rahman@ripplemedia.com
# Let's write some code that converts a name into an email id that matches this format
# 1.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name'
lower_name= employee_name.lower()
print(lower_name)
print(type(lower_name))
# I simply used the conversion function to lower all the letters.
# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list'
name_list = lower_name.split()
print(name_list)

# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names'
# joined_names
# This was tough, had to look for videos online. I don't remember viewing .split, .join videos on Canvas.....But I love it1!!
joined_name='.'.join(name_list)
print(joined_name)
# 1.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email'
# I had a hard time with this question
email=joined_name+"@ripplemedia.com"
print(email)
print()

print('Question 2')

# Congratulations! Your team is expanding. Below is a list of their names:
names = ['Max Bartlett', 'Angelita Norris', 'Stewart Mueller', 'Dominique Henry', 'Carmela Gross', 'Bettie Mcmillan', 'Sara Ellison', 'Ira Anthony', 'Pauline Riley', 'Ben Weber',
         'Joanne Mcknight', 'Loren Gould', 'Jamar Singh', 'Amanda Vance', 'Tyrell Andrade', 'Jana Clements', 'Eddy Mcbride', 'Marsha Meyer', 'Elbert Shannon', 'Alyce Hull']

# lower_names=names.lower()
# print(lower_names)
# lower_names= names.lower()
lower_names=[]
for i in names:
    # print(i)
    i.lower()
    lower_names.append(i.lower())
# names_list= names.split('')
# lower_names=names_list
# print(lower_names)
# names_list= lower_names.split('')
# joined_names='.'.join(names_list)

print(lower_names) 

names_list=[]
for ii in lower_names:
    # print(type(ii))
    stringii=ii+'@ripplemedia.com'
    names_list.append(stringii)
print(names_list)
print(type(names_list))
string_name=str(names_list)
print(string_name)
print(type(string_name))
split_names=string_name.split('')
print(split_names)
# # lower_names=[]
# # emails = []
# # for i in lower_names:
# #     emails.append(i+"@ripplemedia.com")

# # print(emails)
# # We want to convert all their names into the same format from Question 1
# # 2.1 TODO: Use a "for" loop to go over each name in the names list
# for expansion in lower_names:
#     expansion= lower_names.split('')
# print(expansion)
#     # print(expansion)
# # print()
# # 2.2 TODO: Inside the "for" loop, create the email id by re-using the logic from Question 1 and...
# for iii in names_list:

#     email=expansion+'@ripplemedia.com'
# # for ripplemedia in names:
# #     ripplemedia= "@ripplemedia, ".join(names)

# #     print(ripplemedia)
# #     break

# # 2.3 TODO: ..add the email to the emails list
# # THis was a hard challenge because I could not find a video that would help me. I dont think they covered this in canvas
# print(email)