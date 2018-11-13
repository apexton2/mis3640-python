import math

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return '{},{}'.format()

    # def print_point(self):
    #     """Print a Point object in human-readable format."""
    #     print('({}, {}).'.format(self.x, self.y))

    def __add__(self, other):
        new_point = Point(self.x + other.x, self.y + other.y)
        return new_point

    def __eq__(self, other):
        return self.x == other.x



  

def main():
    defne = Point(4, 3)
    print(defne)
    Shirley = Point(1, 1)
    print(defne + Shirley)
  
    print(angel)
#     my_point = Point()
#     print(Point.__doc__)
#     my_point.x = 3
#     my_point.y = 4
#     print('My point', end=' ')
#     print_point(my_point)

#     print('Is my_point an instance of Point?', isinstance(my_point, Point))
#     print('Is my_point an instance of Rectangle?',
#           isinstance(my_point, Rectangle))
#     print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
#     print('Does my_point have an attribute z?', hasattr(my_point, 'z'))


if __name__ == '__main__':
    main()
