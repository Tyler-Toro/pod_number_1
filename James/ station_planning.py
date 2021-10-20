
from stations_challenge import *

train_stop1 = BusStation(station_name = 'NYC Megabus Stop', location = '34th street and 12th avenue' , routes = ['Boston', 'DC', 'Philly'])

bus_stop2 = BusStation(station_name = 'Port Authority', location = '20 W 48th St' , routes = ['Poughkeepsie', 'New Hampshire', 'Stamford'])

bus_stop3 = BusStation(station_name = 'Empire State Building', location = '20 W 34th St' , routes = ['Bridgport', 'New Haven', 'Fairfeild'])

train_stop1.show_info()
bus_stop2.show_info()
bus_stop3.show_info()
