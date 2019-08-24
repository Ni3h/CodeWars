"""
Solution for the Human Readable Time question on codewars
    https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
Using modulo makes this very simple! It is necessary to format the numbers
so that they have leading 0's
@author Ni3h
"""


def make_readable(seconds):
    SS = seconds % 60
    MMTemp = (seconds - SS)/60
    MM = MMTemp % 60
    HH = (MMTemp - MM)/60

    readableTime = ("{:02d}".format(int(HH))+":"+"{:02d}".format(int(
        MM))+":"+"{:02d}".format(int(SS)))
    return readableTime



print(make_readable(86399))
