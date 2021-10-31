# Spotify Challenge
<br>
<br>



### Songs
| PK  | Song        |
| --- | ----------- |
| 1   | Breathe |
| 2   | Somebody Someone |
| 3   | Happy Days |
| 4   | Code for Life |
| 5   | Sunshine |
| 6   | Koffee |

<br>
<br>


### Genre
| PK  | Unique_ID 
| --- | ---------- | 
| 1   | Rock | 
| 2   | Jazz |

<br>
<br>


### Subgenre
| ID  | Genre_ID (FK)   | Song_ID (FK) |
| --- | ------ | -------- |
| 1   | 2   | 1        |
| 2   | 1   | 2        |
| 3   | 2  | 3       |
| 4   | 1 | 4        |
| 5   | 2   | 5        |
| 6   | 1 | 6       |
| 7   | 2   | 6        |

<br>
<br>


# Question 1
a) Briefly describe a better way of modeling genre data in the database to avoid some of the issues listed above. You can assume for the sake of simplicity there can be only one genre per song.

<br> 
b) What relationship best describes how genre relates to songs in your answer to Question 
1a?


<br>
<br>

# Answer 1
a) The genre table has a foreign key relationship with the song table. This is because each genre has a unique ID and each song has a genre ID. This allows us to relate the genre ID to the song ID.

<br> 

b) The relationship is many to one because there is only one genre per song.

<br> 
<br> 


# Question 2
What changes would you make to the modeling of genre data if we could assign more than one genre to a song?

<br>
<br>

# Answer 2
Add another intermediary table to the database that would allow us to assign more than one genre to a song.

<br>
<br>

<img
src="/Users/jasondoze13/Desktop/pod_number_1/Jason/spotify_challenge/image/db tables.jpg"/> 

