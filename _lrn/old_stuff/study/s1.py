__author__ = 'User'
import math


## a = raw_input("enter smrh")
a = -5123.99
def distance_from_zero(a):
    i = type(a)
    if i == int or i == float:
        return abs(a)
    else:
        return "This isn't an integer or a float!"
print type(a)
print distance_from_zero(a)