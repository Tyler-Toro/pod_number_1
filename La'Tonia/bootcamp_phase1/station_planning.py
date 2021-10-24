from stations_challenge import *
from pprint import pprint



swift_hustle_hub = BusStation(station_name='Eve Pearl', location='South End', routes=['1, 3, 7, 13, G'])

py_north_station = BusStation(station_name='Cynt Binge', location='Northern Happs', routes=['44, 2, 9, L, 12'])

dash_run_diggs = SubwayStation(station_name='Chaney', location='East Wests', lines=['P, U, L, L2, L3'])

py_way_station = SubwayStation(station_name='Back Downs', location='Inward Digey', lines=['1Y, 4S, E7, 8, K11'])

swift_hustle_hub.show_info()
py_north_station.show_info()
dash_run_diggs.show_info()
py_way_station.show_info()
print()

pprint(swift_hustle_hub.show_info())
pprint(py_north_station.show_info())
pprint(dash_run_diggs.show_info())
pprint(py_way_station.show_info())