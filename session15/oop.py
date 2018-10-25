class Point:
    """represents a point in 2-D space"""

my_point = Point()

print(type(my_point))
print(isinstance(my_point, Point))

my_point.x = 3
my_point.y = 4

print(my_point.x)
print(my_point.y)
x = my_point.y
print(x)
print(my_point.x)

import math

print('(%g, %g)' % (my_point.x, my_point.y))
distance = math.sqrt(my_point.x**2 + my_point.y**2)
print(distance)

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))
print_point(my_point)

print(hasattr(my_point, 'x'))
print(hasattr(my_point, 'z'))

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    x_diff = p2.x - p1.x
    y_diff = p2.y - p1.y
    distance = math.sqrt(x_diff**2 + y_diff ** 2)
    return distance


#rectangle

class Rectangle:
    """attributes = width, height, corner."""
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box)
print_point(center)

box.width = box.width + 50
box.height = box.height + 100

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width)
print(box.height)
print('grow')
grow_rectangle(box, 50, 100)
print(box.width)
print(box.height)

p1 = Point()
p1.x = 3.0
p1.y = 4.0

import copy
p2 = copy.copy(p1)

print_point(p1)
print_point(p2)

print(p1 is p2)
print(p1 == p2)

class Circle:
    """ This is a class of Circle in 2D space"""

circle = Circle()
circle.center=Point()
circle.center.x=150.0
circle.center.y=100.0
circle.radius=75.0

print(circle.center.x)
print(circle.center.y)
print(circle.radius)

def point_in_circle(point, circle):
    d = distance_between_points(point, circle.center)
    print(d)
    return d<=circle.radius

alden = Point()
alden.x = 151
alden.y = 101

print(point_in_circle(alden, circle))

def rect_in_circle(rect, circle):
    """checks wheter rectangle is within circle"""
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False
    return True

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

print(rect_in_circle(box, circle))



def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.
    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False




print(rect_circle_overlap(box, circle))