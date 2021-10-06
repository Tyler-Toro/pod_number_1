# added pip to imports per import error for numpy despite install
import pip
import numpy as np

# Music playlist challenge!
# In this challenge, you'll have to both work on this script, and the accompanying script playlist_functions.py
# All of your functions should be in the other script (playlist_functions.py)
# But, you'll run your functions here

# 1 Import all the functions in playlist_functions.py
# start with from where and follow with what from where 
print('EXERCISE 1')
print(' "importing pip and numpy w/alias np at top of file" ')
print(' "also in this part of assignment importing all fns from fn file using asterick wildcard" ')
print()

from playlist_functions import *

# This code initializes your playlist as an empty list. no songs in it yet!
# variable my_playlist will store value of songs as songs go through the (initially) empty list 
my_playlist = []

# 2 Check what is in your playlist using the display_playlist() function
# HINT: see the display_playlist() function in playlist_functions.py to figure out how to use it
print('EXERCISE 2')
print(' "checking contents of playlist by running display_playlist function passing as parameter my_playlist" ')
print(f'The Result: {display_playlist(my_playlist)}, and the note above that the playlist is empty is printing from the fns file.')
print()

# 3 Add a song to my_playlist using the add_song() function
# The song that you add should be a dictionary, with the following key-value pairs
# 'artist' (string)
# 'title' (string)
print('EXERCISE 3')
print(' "creating new song as datatype dict to add to add_song()" ')
vibrant_song = {
    'artist': 'BlaqRose\'', 
    'title': "Sideways in Its"
    }

add_song(my_playlist, vibrant_song)
print()

# 4 Check that you've added the song by running the display_playlist() function again
print('EXERCISE 4')
print(' "checking contents of playlist by re-running display_playlist function passing as parameter my_playlist" ')
display_playlist(my_playlist)
print()

# 5 Add 2 more songs to my_playlist, then display it again using the display_playlist() function
print('EXERCISE 5')
print(' "adding more songs as independent variables assigned values of dicts with artist and title key-value pairs" ')
print()

guest_song = {
    'artist': 'Host Swoona',
    'title': 'Drenchy Lifetimes'
}

timeless_song = {
    'artist': 'Grainy Say',
    'title': 'Going On'
    }

add_song(my_playlist, guest_song)
add_song(my_playlist, timeless_song)
display_playlist(my_playlist)
print()

# attempting two parameters to call songs in function display_playlist while meeting all param criteria
print('EXERCISE 5 EXTENDED')
print(' "same as above BUT displaying contents of playlist from one/combined fn - instead of multiples ... should be exactly the same result ... interesting it pulls in second track again at end of call" ')
# gone_song(my_playlist, guest_song, timeless_song)
# display_playlist(my_playlist)
# print()

# 6 In playlist_functions.py, define a function called get_playlist_length()
# See playlist_functions.py for details on how to define this function
# THEN, call that function in this script to get the length of my_playlist
print('EXERCISE 6')
print(' "getting how many items are in variable my_playlist by calling fn get_playlist_length and passing my_playlist" ')
print(' "also interesting duplication error cascades to this result - adding one to produce four for what should be a total of three" ')
print(f'RESULT: {get_playlist_length(my_playlist)} songs in here.')
print()

# 7 At the top of this script, import numpy using the usual alias
print('EXERCISE 7')
print(' "exercise that led to importing pip and numpy w/alias np at top of file" ')
print()

# 8: Using numpy, calculate the average monthly plays for a song
# TODO: using the mean() function from numpy, calculate the average of monthly_plays
# You don't have to write any functions for this question
# wrapping existing code in mean function to get average
print('EXERCISE 8')
print(' "averaging times song plays in a month and displaying result whole then followed by rounded version in an f-string" ')
monthly_plays = np.mean([127030, 274920, 232453, 98278, 500301, 235462])
print(monthly_plays)
print()

# wrapping code to get mean in round fn to drop value after decimal while not losing numeric value - i.e. rounds up
monthly_plays = round(np.mean([127030, 274920, 232453, 98278, 500301, 235462]))
print(f'Average Monthly Plays for Song: {monthly_plays}')
print()


# BONUS In playlist_functions.py, define a new function called play_track()
# See playlist_functions.py for details on how to define this function
# Then play a few tracks, and run display_playlist() again to make sure it works
print('BONUS')
print(' "creating new fn play_track() from previous code in fns file" ')
print(' "to play a few tracks and ensuring code works" ')
play_track(my_playlist, 0)
print()

play_track(my_playlist, 1)
print()

play_track(my_playlist, 2)
print()
