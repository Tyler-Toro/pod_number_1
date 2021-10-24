# practice courtesy https://realpython.com/python-super/
# I like this exercise because it is operations ... which give me the heeby geebies

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

square = Square(4)
square.area()
print('PRINTS AREA OF SQUARE WITH VALUE 4')
print(square.area())
print()

rectangle = Rectangle(2,4)
rectangle.area()
print('PRINTS AREA OF RECTANGLE WITH VALUES 2 AND 4')
print(rectangle.area())
print()

# above code becomes code below
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# set up square class to inherit from super aka parent class
# calling super/parent class Rectangle via __init__ method on line 54 in child class Square sets the length and width attributes - only have to supply the length parameter to the Square class/constructor
# basically Square class inherits area from Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

square = Square(4)
square.area()
print('PRINTS AREA OF SQUARE WITH VALUE 4 USING SUPER()')
print(square.area())
print()


# why am I passing length twice - first length is for child class Square and second length is for parent/super/parent class length?
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

'''
code below does the same as lines 65-67
class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)
'''

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

'''
code below does the same as lines 76-83
class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length
'''

cube = Cube(3)
cube.surface_area()
print('PRINTS NUMBER THREE CUBED')
print(cube.surface_area())
print()

cube.volume()
print('PRINTS CUBE VOLUME')
print(cube.volume())
print()


# illustrating multiple inheritance with triangle
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__()

    def tri_area(self):
        return 0.5 * self.base * self.height

    def area(self):
        return 0.5 * self.base * self.height

    # class RightPyramid(Triangle, Square):
    #     def __init__(self, base, slant_height):
    #         self.base = base
    #         self.slant_height = slant_height

    #     def area(self):
    #         base_area = super().area()
    #         perimeter = super().perimeter()
    #         return 0.5 * perimeter * self.slant_height + base_area

# inspect order per resolution needs - what happens and in what order
    # RightPyramid.__mro__

# code lines 118 to 126 becomes ...
# but this whole bottom code block not working ... too ambitious at this point
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(self.base)
        super().__init__(base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area

    # pyramid = RightPyramid(2, 4)
    # RightPyramid.__mro__
    # pyramid.area()

# not working ... too ambitious at this point
pyramid = RightPyramid(base=2, slant_height=4)
pyramid.area()
pyramid.area_2()