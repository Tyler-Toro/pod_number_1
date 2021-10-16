# NOTE: these first two functions do not have to be edited

# prints out what is in your playlist
# takes one argument: 'playlist' (a list)

# outlines fn setup to play through tracks/playlist
def display_playlist(playlist):
	if len(playlist) == 0:
		print('Playlist is empty!')
	else:
		for i in range(len(playlist)):
			print(f'Track {i+1}: {playlist[i]["plays"]} plays \
				  \n\t-{playlist[i]["title"]} by {playlist[i]["artist"]}')

# function to add a song to the playlist
# takes two arguments: 'playlist' (a list), and 'song' (a dictionary)
def add_song(playlist, song):
	# automatically initialize play count of song to 0
	# song['plays'] = ''
	song['plays'] = 0
# below code increases play by one but only one/once
	# song['plays'] += 1
	playlist.append(song)

# # attempting more parameters
# def gone_song(playlist, song, song0):
# 	# automatically initialize play count of song to 0
# 	song0['plays'] = 0
# 	playlist.append(song0)

'''
TODO (Question 6): define a function called get_playlist_length()
This function should have one parameter called 'playlist'
The function should return an integer value indicating how many songs there are
'''
# solid/same result without adding int fn
def get_playlist_length(playlist):
# return (int(len(playlist)))
	return (len(playlist))



'''
TODO (BONUS): define a function called play_track()
It should have two parameters
-'playlist' (a list)
# MAKING A PARAM OPTIONAL SIMPLY MEANS SETTING A VALUE TO IT IN THE FUNCTION()
-'track' (an integer) - this should be optional, and by default play track 1

This function should 'play' the song corresponding to the input track #

For example play_track(my_playlist,3) should print out:

'Now playing track 3, Controversy by Prince' 
Assuming that the third track in your playlist 'Controversy' by 'Prince'

This function should ALSO increase the 'plays' value for that song's dictionary by 1
So, if 'Controversy' has 0 plays so far, it should now be increased to 1
'''

# can *args be used to set optional value for param two?
# playlist = []
# track = int

# code below primary attempt at bonus ... works while not fulfilling full bonus requirements ... worked on w/Brandon Grant
# songs = str('Number of Plays Goes Here: x ')

# def play_track(playlist, num = 0):
# 	if len(playlist) == 0:
# 		print('Playlist is empty!')
# 	else:
# 		for i in playlist:
# 			print(f'Now playing track {num+1}: {songs} plays \
# 				  \n\t-{playlist[num]["title"]} by {playlist[num]["artist"]}')
# 			return play_track


# code below another primary attempt at bonus ... maybe works while not fulfilling full bonus requirements ...
def play_track(playlist,num=0):
	songs = str('Song Here')
	if len(playlist) == 0:
		print('Playlist is empty!')
	else:
		for i in playlist:
			print(f'Now playing track {num+1}: {songs} plays \
				  \n\t-{playlist[num]["title"]} by {playlist[num]["artist"]}')
			for i in range(len(playlist)):
				print(f'Track {i+1}: {playlist[i+1]["plays"]} plays \
					\n\t-{playlist[i]["title"]} by {playlist[i]["artist"]}')
			return play_track

# code below initial attempt at bonus ... breaks code
# def play_track(playlist, track):
# 	for track in playlist:
# 		playlist.append(track)

# 	if len(playlist) == 0:
# 		print('Playlist is empty!')
# 	else:
# 		for i in range(len(playlist)):
# 			print(f'Track {i+1}: {playlist[i]["plays"]} plays \
# 				  \n\t-{playlist[i]["title"]} by {playlist[i]["artist"]}')

# final round ... re-try per Paul graciously showing us in class
# copy/pasted from what i typed into Slack to share with other student to see if get tab error ... received syntax error and tab error/inconsistent use of spaces and tab error ... so it worked

def play_track(playlist, track=1):
	track -= 1
	print(f"Playing: track {track}, by {playlist[track]['title']}, {playlist[track]['artist']}")
	playlist[track]['plays']+=1 