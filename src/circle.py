

import math

class Circle(object):
    
    def __init__(self, r=1):
        self.radius = r 

    def perimeter(self):
        return 2 * math.pi * self.radius 


    def area(self):
        return math.pi * (self.radius**2)

    def __str__(self):
        return f'Circle radius {self.radius}'

    def __repr__(self):
        return f'Circle radius (radius={self.radius})'


