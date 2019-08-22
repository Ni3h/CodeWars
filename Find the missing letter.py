"""
Solution for the Find the missing letter question on codewars
    https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
This was a fun and easy one! I learnt from one I did previously that instead
of making a library for the alphabet I could take advantage of ASCII conversion
@author Ni3h
"""


def find_missing_letter(chars):
    ordStart = ord(chars[0])
    iterChars = iter(chars)
    next(iterChars)

    for i in iterChars:
        if ord(i) != (ordStart+1):
            return chr(ordStart+1)
        ordStart = ord(i)


find_missing_letter(['a','b','c','d','f'])

