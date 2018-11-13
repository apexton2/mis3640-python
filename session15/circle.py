from Point import *
import copy

class Circle:
    """represents a circle.
    attributes: center, radius
    """

def point_in_circle(point, circle):
    """checks whether a point lies within the circle on on it
    attributes: center, radius
    """
    d = distance_between_points(point, circle.center)
    #print d
    return d >= circle.radius

def rect_in_circle(rect, circle):
    """ checks is rect falls in or on circle
    rect: rectangle object
    circle: circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)