# more oop practice courtesy w3resource at https://www.w3resource.com/python-exercises/class-exercises/python-class-basic-1-exercise-1.php

# uses built-in/pre-installed array module through import statement to show namesoace of the array module

'''
according to a general google search, 

"Namespaces in Python. A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves."

link to search result(s) https://www.google.com/search?q=what+is+namespace+python+array+module&oq=what+is+namespace+python+array+module&aqs=chrome..69i57j33i22i29i30.10550j1j4&sourceid=chrome&ie=UTF-8
'''


import array

for name in array.__dict__:
    print('PRINTS NAMESPACES OF ARRAY MODULE EACH ON\nITS OWN LINE ACCOMPANIED BY THIS TITLE')
    print(name)
    print()


# more practice courtesy https://pynative.com/python-object-oriented-programming-oop-exercise/

# create Vehicle class, add two attributes max_speed and mileage ...
class Vehicle:
    def __init__(self):
        pass


# becomes
class Vehicle:
    color = "Amethyst"

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def seating_capacity(self, capacity):
        return f"Seating Capacity: {self.name} accommodates {capacity}"

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount

# this may or may not have helped code lines 90-93 work
    # def seating_capacity(self, capacity):
    #     return super().seating_capacity(capacity=44)

class Car(Vehicle):
    pass

class Bus(Vehicle):
    pass


# instantiate
# veh_model = Vehicle(name="School Cadillac", max_speed=344, mileage=22)
# print('PRINTS MAX SPEED AND MILEAGE VALUES FOR INSTANCE OF VEHICLE\nPARENT CLASS NAMED VEH_MODEL - FIRST MAX SPEED THEN MILEAGE')
# print(veh_model.max_speed, veh_model.mileage)   
# print(F"MAX SPEED: {veh_model.max_speed}\nMILEAGE:{veh_model.mileage}")    
# print()


# instantiate
# school_bus = Bus('School Cadillac', 144, 13)
# print('PRINTS CHILD CLASS INSTANCE SCHOOL BUS\nWITH NAME, MAX SPEED, MILEAGE ATTRIBUTES\n')
# print(F"VEHICLE NAME: {school_bus.name} \nMAX SPEED: {school_bus.max_speed} \nMILEAGE: {school_bus.mileage} \n")
# print()

# print('PRINTS SEATING CAPACITY')
# print(school_bus.seating_capacity(44))
# print()


# instantiate
# car = Car("Sleek Throwback Impala", 227, 22)
# print('PRINTS COLOR FROM INSTANCE')
# print(Car.color, car.name, "\nSPEED:", car.max_speed, "\nMILEAGE:", school_bus.mileage)
# print()

# instantiate
# have code belwo working but think I bootlegged the outcome
school_bus = Bus('School Cadillac', 144, 13, capacity=44*100)
print('PRINTS FARE PER CAPACITY')
print(f'TOTAL BUS FARE:', '$', school_bus.fare())
print()

# should be ... nopes - still no-go ... still need to add capacity ... supposed to pull from definition/value set for capaciry above I THINK
school_bus = Bus('School Cadillac', 144, 13, capacity=44*100)
print('PRINTS FARE PER CAPACITY')
print(f'TOTAL BUS FARE:', '$', school_bus.fare())
print()


print('PRINTS CLASS FOR SPECIFIC BUS OBJECT/INSTANCE')
print(type(school_bus))
print()

# contains instance first separated by parent class second with comman to determine if instance is of the parent class ... True means yes it is
print('PRINTS INSTANCE FOR PARENT CLASS')
print(isinstance(school_bus, Vehicle))
print()


   







