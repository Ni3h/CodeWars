"""
Solution for the Rot13
question on codewars https://www.codewars.com/kata/rot13-1/train/python
A bit messy, but getting back into the swing of things so don't feel too bad about it!
@author Ni3h
"""


def rot13(message):
    newMessage = ""

    for i in message:
        upperCase = False
        if i.isupper():
            upperCase = True
        y = i.lower()
        asciiKey = ord(y)
        if asciiKey >= 97 and asciiKey <= 122:
            newRot = asciiKey + 13
            if newRot > 122:
                numToRot = newRot - 123
                newRot = 97 + numToRot
            if upperCase == True:
                x = chr(newRot).upper()
            else:
                x = chr(newRot)
            newMessage = newMessage + x
        else:
            newMessage = newMessage + y
    return newMessage


    # for i in message:
    #     uppercase = False
    #     if i.isupper():
    #         uppercase = True
    #     y = i.lower()
    #     if y in alphabet:
    #         b = alphabet.find(y)
    #
    #         newNum = b + 13
    #         if newNum >= len(alphabet):
    #
    #             newerNum = newNum - len(alphabet)
    #             if uppercase:
    #                 newMessage = newMessage + alphabet[newerNum].upper()
    #             else:
    #                 newMessage = newMessage + alphabet[newerNum]
    #         else:
    #             if uppercase:
    #                 newMessage = newMessage + alphabet[newNum].upper()
    #             else:
    #                 newMessage = newMessage + alphabet[newNum]
    #     else:
    #         newMessage = newMessage + y
    # return newMessage
    #


rot13("aAbC1z")