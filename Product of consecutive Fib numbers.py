"""
Solution for the Product of consecutive Fib numbers
question on codewars
    https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python
This one was fun! It slowly goes through the Fibonaci sequence, but the
original question didn't state how long it should be so I had it manually
build the sequence. this one was harder than previous ones!
@author Ni3h
"""


def productFib(prod):
    x = True
    fibStart = 0
    fibSecond = 1
    prodArray = []
    while x == True:
        temp = fibStart + fibSecond
        fibStart = fibSecond
        fibSecond = temp
        prodTest = fibStart * fibSecond
        if prodTest > prod:
            prodArray.append(fibStart)
            prodArray.append(fibSecond)
            prodArray.append(False)
            x = False
        elif prodTest == prod:
            prodArray.append(fibStart)
            prodArray.append(fibSecond)
            prodArray.append(True)
            x = False
    return prodArray



