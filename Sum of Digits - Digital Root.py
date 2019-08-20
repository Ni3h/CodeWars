"""
Solution for the Sum of Digits / Digital Root question on codewars
    https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
I did the solution with recursion(digital_root) and a loop(digital_loop_root)!
To be honest the loop took me longer than recursion.
@author Ni3h
"""
def digital_root(n):
    nStr = str(n)
    if len(nStr) == 1:
        return n
    else:
        sum = 0
        for x in nStr:
            sum += int(x)
        return digital_root(sum)

def digital_loop_root(n):
    y = True
    nStr = str(n)
    sum = 0

    while y == True:
        if len(nStr) == 1:
            return int(nStr)
            y = False
        for x in nStr:
            sum += int(x)
        nStr = str(sum)
        sum = 0


print(digital_root(263))
print(digital_loop_root(263))