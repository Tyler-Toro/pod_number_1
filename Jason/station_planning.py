
from stations_challenge import *
# Now, it's time to design a few more stations of your own in another script! 
# Make a new python script called "station_planning.py"
# -In this script, *import* the classes you made in this challenge file
# -Instantiate 3 more stations of your choosing (at least 1 bus and 1 subway)
# -Feel free to make up names, locations, lines, and routes!


print('Question 5: Importing your classes')
print()
bus_stop2 = BusStation(station_name= 'NYC Super Stop', location = '55th street and 12th avenue', routes = ['Elif', 'CD', 'Taft'])

bus_stop3 = BusStation(station_name= ' Super Stop', location = '57th street and 13th avenue', routes = ['Compton', 'Long Beach', 'San Pedro'])

train_stop1 = BusStation(station_name= ' Turbo Stop', location = '7th street and 21st avenue', routes = ['Vacaville', 'Victorville', 'Lompoc'])

bus_stop2.show_info()
bus_stop3.show_info()
train_stop1.show_info()
print()