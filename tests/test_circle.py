
import math

import pytest
from src.circle import Circle 

class TestCircle():

    def test_area(self):
        c = Circle()
        assert (c.area() == math.pi )

    def test_perimeter(self):
        c = Circle()
        assert (c.perimeter() == 2 * math.pi)


    def test_object(self):
        c = Circle()
        assert(c.radius == 1)

