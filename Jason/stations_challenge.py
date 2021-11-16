

class Station:     # Note, you should NOT need to change the Station class 
    def __init__(self, station_name, location):
        self.station_name = station_name
        self.location = location
    
    def show_info(self):
        print(f'{self.station_name} station is located in {self.location}')
       


print('Question 1: Making the SubwayStation Class')
print()
# Using the Station class below as the parent, make a child class called SubwayStation
# SubwayStation should:
# have an additional attribute called 'lines' that is user-defined as a list during initialization. 
# this will indicate which subway lines stop at the station (for example ['A', 'C']) 


class SubwayStation(Station):
    def __init__(self, station_name, location, lines):
        super().__init__(station_name, location)
        self.lines = lines 

    
    def show_info(self):
        print(f'{self.station_name} station is located in {self.location} and it has these subway lines: {self.lines}')
        print()
        


print('Question 2: Make an example subway station')
print()
# Using your SubwayStation class, instantiate a subway station with the info below. 
# Then run the show_info() method to make sure you get the station_name, location, and lines printed out
# station_name: '14th street'
# location: '14th street'
# lines: ['1', '2', '3', 'L']

sub_station_1 = SubwayStation(station_name= '14th street', location= '14th street', lines= ['1', '2', '3', 'L'])
sub_station_1.show_info()
print()


print('Question 3: Making the BusStation Class')
print()
# Using the Station class below as the parent, make a child class called BusStation
# BusStation should:
# -have an additional attribute called 'routes' that is user-defined as a list during initialization. 
# this will indicate where buses can go from this station. For example, ['DC', 'Philly', 'Pittsburgh']
# -have an additional attribute called 'open' that is always initalized as True (a boolean variable)
# -have additional methods called open_station() and close_station() to open and close the station
# -override the show_info() method from Station to display the bus routes and if the station is open, in addition to the station name and location


class BusStation(Station):
    def __init__(self, station_name, location, routes):
        super().__init__(station_name, location)
        self.routes = routes  
        self.open = True 

    def show_info(self):
        print(f'{self.station_name} station is located in {self.location} and it has these routes: {self.routes}')
        if self.open:
            print('The station is open!')

        else:
            print('Station is closed!')


    def open_station(self):
            self.open = True
            # print('The station is open')

    def close_station(self):
            self.open = False 
            # print('The station is closed')
print()



print('Question 4: Make an example bus station')
print()
# Using your BusStation class, instantiate a bus station with the info below. 
# Then, run the show_info() method to make sure you get the station_name, location, routes, and whether the station is open printed out
# Then, demonstrate that you can close and open the bus station
# i.e. that the show_info() method reflects correctly when the station is open versus closed


bus_stop = BusStation(station_name= 'NYC Megabus Stop', location = '34th street and 12th avenue', routes = ['Boston', 'DC', 'Philly'])
bus_stop.open_station()
bus_stop.close_station()
bus_stop.show_info()
print()






