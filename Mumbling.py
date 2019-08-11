"""
Solution for the Mumbling question on codewars
    https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
Pretty simple, only 'complex thing' is to ensure that the - does not get
added to the first iteration of the newString
@author Ni3h
"""

def accum(s):
    newString = ""
    for i, letter in enumerate(s):
        newAdd = (letter * (i+1)).capitalize()
        if i == 0:
            newString = newAdd
        else:
            newString = "-".join([newString, newAdd.capitalize()])
    return newString



