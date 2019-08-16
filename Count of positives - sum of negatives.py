"""
Solution for the Count of positives / sum of negatives
question on codewars
    https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
Necessary to account for edge cases where the array/list is empty
@author Ni3h
"""

def count_positives_sum_negatives(arr):
    isPositive = 0
    sumNegatives = 0
    if not arr:
        return arr
    for i in arr:
        if i > 0:
            isPositive += 1
        else:
            sumNegatives += i
    newList = [isPositive, sumNegatives]
    return newList
