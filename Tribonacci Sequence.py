"""
Solution for the Tribonacci Sequence
question on codewars
    https://www.codewars.com/kata/tribonacci-sequence/train/python
Pretty simple, loop through the total numbers wanted while appending the list!
Important though to have some way to check for edge-cases that have an n < 3
@author Ni3h
"""


def tribonacci(signature, n):
    if n < 4:
        newSeq = []
        for j in range(n):
            newSeq.append(signature[j])
        return newSeq
    else:
        for i in range(n-3):
            newNumber = signature[i] + signature[i+1] + signature[i+2]
            signature.append(newNumber)
        return signature



