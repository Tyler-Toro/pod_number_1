
from Trains import *
train_stop1 = BusStation(station_name = 'NYC Megabus Stop', location= '34th street and 12th avenue', routes=  ['Boston', 'DC', 'Philly'])

bus_stop2 = BusStation(station_name = 'NYC EGGABUS Stop', location= '43th street and 21th avenue', routes=  ['Tonville', 'CD', 'WILLiF'])

bus_stop3 = BusStation(station_name = 'Differnt Names', location= 'Same Names', routes=  ['Pick a City', 'I like this spot', 'Hey there'])

train_stop1.show_info()
bus_stop2.show_info()
bus_stop3.show_info()

 