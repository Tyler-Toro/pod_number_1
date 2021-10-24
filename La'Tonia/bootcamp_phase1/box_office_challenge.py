
# this variable is assigned a string
movies_str = "House on Haunted Hill,Cruel Intentions,10 Things I Hate About You,My Favorite Martian,8MM,Fight Club,The Matrix,Any Given Sunday,The Thin Red Line,A Bug's Life, For Love of the Game, Instinct, Mickey Blue Eyes, The Best Man, Bicentennial Man, The 13th Warrior, October Sky, Lake Placid, Random Hearts, Mighty Joe Young, Superstar, Mystery Men, The Talented Mr. Ripley, Dogma, The Out-of-Towners, The Other Sister, Baby Geniuses, The Story of Us, Blast from the Past, The Insider, Saving Private Ryan, Mysteries of Egypt, The Wood, Arlington Road, T-Rex: Back to the Cretaceous, The Iron Giant, Edtv, At First Sight, The Faculty, Summer of Sam, The Bachelor, Stir of Echoes, Anna and the King, Man on the Moon, Galaxy Quest, Enemy of the State, Waking Ned Devine, Doug's 1st Movie,An Ideal Husband,Everest"
# this variable is assigned a list of strings
top_50_list = ['Star Wars: Episode I - The Phantom Menace', 'The Sixth Sense', 'Austin Powers: The Spy Who Shagged Me', 'Toy Story 2', 'The Matrix', 'Tarzan', 'Big Daddy', 'The Mummy', 'Runaway Bride', 'The Blair Witch Project', 'Notting Hill', 'The World Is Not Enough', 'Double Jeopardy', 'Wild Wild West', 'Analyze This', "The General's Daughter", 'American Pie', 'Inspector Gadget', 'Shakespeare in Love', 'Sleepy Hollow', 'The Haunting', 'Patch Adams', 'Entrapment', 'Pokémon: The First Movie - Mewtwo Strikes Back', 'Payback', 'Deep Blue Sea', 'American Beauty', 'The Thomas Crown Affair', 'Stuart Little', 'Blue Streak', 'The Green Mile', 'Bowfinger', 'Life', 'The Bone Collector', "She's All That", 'End of Days', 'Three Kings', 'A Civil Action', 'Stepmom', 'Eyes Wide Shut', 'Never Been Kissed', 'Forces of Nature', 'Varsity Blues', 'Message in a Bottle', "You've Got Mail", 'South Park: Bigger, Longer & Uncut', 'Stigmata', 'Life Is Beautiful', 'The Prince of Egypt',
               'Deuce Bigalow: Male Gigolo']


# TODO: Take the string "movies_str" and convert it into a list and assign it to a variable called "remaining_50_list"
# Note: Print your new variable to see the list of movies
# This felt straightforwward but really it was clear notes that helped me see the solution w/o struggle
remaining_50_list = movies_str.split(',')
len_50_list = len(remaining_50_list)
# Bit of formatting to lead into the list with a title
print(f'remaining_50_list = {remaining_50_list}')
print(len_50_list)
print()

# TODO: Hmm. Looks like "remaining_50_list" contains the movie "The Matrix" which is also in the "top_50_list". Let's remove this duplicate title from "remaining_50_list".
# Note: Make sure to double check the list you are removing from!
# This felt starightforward, too
remaining_50_list.remove('The Matrix')
print(len(remaining_50_list))
print()


# TODO: We're down to 49 movies in "remaining_50_list". Let's add a movie to the list called "Anywhere But Here"
# Note: Print the variable "remaining_50_list" and see if the movie has been added!
# This is one of the exercises I answered in class, and it went smoothly. I took time to read the question, formulate my thoughts, then articulated the solution verbally for us all.
remaining_50_list.append('Anywhere But Here')
print(remaining_50_list)
print()

# Straightforward for me
# TODO: Let's make sure "remaining_50_list" has exactly 50 movie titles
print(len(remaining_50_list))
print()

# TODO: Great! Let's join the two lists into one list called "top_100".
# Note: Print your new variable to see the combined list of movies
# I thought we could use .join method for this but it was much simpler - just concatenate
top_100 = top_50_list + remaining_50_list
print(top_100)
print(len(top_100))
print()



# TODO: Let's print the first movie in our "top_100" list. Let's use the index lookup method to do this.
# This I knew w/o struggle
print(top_100[0])
print()

# TODO: Let's print the top 10 movies in "top_100" as a list. Let's use the slice syntax to accomplish this!
# This solution I was confused at first because tried [0 : 11] thinking I had to go an extra number on the end because the end number is exclusive. However, it is appropriate and accurate to use end number that is equal to the total items want to return/print because zero-indexing puts the count one ahead
print(top_100[0 : 10])
print(len(top_100[0: 10]))
print()

# TODO: Let's convert the list "top_100" back into a string. Assign it to a variable called "top_100_str".
# Note: Print your new variable to see the string version of the movies
# For this solution, I re-introduced .join method as an option and was correct. Guarav showed variations for the delimiter which was great illustratively because revisiting my copious notes didn't initially help me gain clarity about how to implement the method ... I was confused about what went between the leading quotes
top_100_str = ", ".join(top_100)
print(top_100_str)
print(type(top_100_str))
print()
