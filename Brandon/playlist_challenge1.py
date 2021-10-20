# Music playlist challenge!
# In this challenge, you'll have to both work on this script, and the accompanying script playlist_functions.py
# All of your functions should be in the other script (playlist_functions.py)
# But, you'll run your functions here

# 1 Import all the functions in playlist_functions.py
from typing import get_type_hints
# importing all functions from the function portion of the challenge
from playlist_challenge_function import *
# This code initializes your playlist as an empty list. no songs in it yet!
my_playlist = []


# 2 Check what is in your playlist using the display_playlist() function
# HINT: the display_playlist() function in playlist_functions.py to figure out how to use it
print('Question 2')
# displayed my_playlist
display_playlist(my_playlist)
print()


# 3 Add a song to my_playlist using the add_song() function
# The song that you add should be a dictionary, with the following key-value pairs
# 'artist' (string)
# 'title' (string)

'''
example_song = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
'''
# did it the lazy way, but effective none the less. copy and paste is your friend.
example_song = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
add_song(my_playlist, example_song)
print()

# 4 Check that you've added the song by running the display_playlist() function again
print('Question 4')
# displayed playlist again to varify if the song was added.
display_playlist(my_playlist)
print()
# 5 Add 2 more songs to my_playlist, then display it again using the display_playlist() function
print('Question 5')
# more copy and paste, just changed the songs and artists
# diplayed after to make sure the songs were added
example_song = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
example_song2 = {'artist': 'Miguel', 'title': 'Coffe'}
example_song3 = {'artist': 'Jay-Z', 'title': 'Already Home'}

add_song(my_playlist, example_song2)
add_song(my_playlist, example_song3)
display_playlist(my_playlist)
print()

# 6 In playlist_functions.py, define a function called get_playlist_length()
# See playlist_functions.py for details on how to define this function
# THEN, call that function in this script to get the length of my_playlist
print('Question 6')
# printed the function.
print(get_playlist_length(my_playlist))
print()


# 7 At the top of this script, import numpy using the usual alias
import numpy as np
print()
# 8: Using numpy, calculate the average monthly plays for a song
'''monthly_plays = []
np.mean(monthly_plays)'''
# TODO: using the mean() function from numpy, calculate the average of monthly_plays
# You don't have to write any functions for this question
print('Question 8')
monthly_plays = [127030, 274920, 232453, 98278, 500301, 235462]
# used np to get the mean of the monthly plays.
average_plays = np.mean(monthly_plays)
print(average_plays)



# BONUS In playlist_functions.py, define a new function called play_track()
# See playlist_functions.py for details on how to define this function
# Then play a few tracks, and run display_playlist() again to make sure it works
print('BONUS')


