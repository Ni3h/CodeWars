"""
Solution for the Count characters in your string on codewars
    https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
Use a dictionary! Very easy, should be made 7 Kyu in my opinion!
@author Ni3h
"""
def count(string):
    countDic = {}
    for i in string:
        if i not in countDic.keys():
            countDic[i] = 1
        else:
            countDic[i] += 1

    return countDic

count('aba')