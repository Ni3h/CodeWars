"""
Solution for the Sum of Digits / Digital Root question on codewars
    https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
This was my first 5 Kyu! It took a while to figure out. Very important to do
the deletion in the order of i+1 then i - otherwise it will be off because the
array got smaller.
@author Ni3h
"""


def dirReduc(arr):
    try:
        for i, direction in enumerate(arr):
            if direction == ('NORTH'):
                if arr[i+1] == ('SOUTH'):
                    del arr[i+1]
                    del arr[i]
                    dirReduc(arr)
            if direction == ('EAST'):
                if arr[i+1] == ('WEST'):
                    del arr[i + 1]
                    del arr[i]
                    dirReduc(arr)
            if direction == ('SOUTH'):
                if arr[i+1] == ('NORTH'):
                    del arr[i + 1]
                    del arr[i]
                    dirReduc(arr)
            if direction == ('WEST'):
                if arr[i+1] == ('EAST'):
                    del arr[i + 1]
                    del arr[i]
                    dirReduc(arr)
    except IndexError:
        return(arr)
    return(arr)


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))