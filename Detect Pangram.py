"""
Solution for the Detect Pangram question on codewars
    https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
Python makes this really easy with the sort method alphabetizing, important
to make sure that it doens't add spaces or duplicates!
@author Ni3h
"""


def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newList = []
    for a in s:
        if a.lower() in alphabet and a.lower() not in newList:
            newList.append(a.lower())
    newList.sort()
    stringForm = "".join(newList)
    if alphabet == stringForm:
        return True
    else:
        return False


pangram = "The quick, brown fox jumps over the lazy dog!"

print(is_pangram(pangram))