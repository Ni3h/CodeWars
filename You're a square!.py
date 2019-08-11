"""
Solution for the Mumbling question on codewars
    https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
Simple solution, could be compacted to one line, just used math import to
sqrt something and see if it is an integer or not (is a square if it is an
integer).
Uses a try to check if the int given is negative (not a square)
@author Ni3h
"""
import math
def is_square(n):
    try:
        a = math.sqrt(n)
    except ValueError:
        return False
    if a.is_integer():
        return True
    else:
        return False
