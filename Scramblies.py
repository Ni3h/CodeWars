"""
Solution for the Scramblies kata on codewars
   https://www.codewars.com/kata/scramblies/train/python
Using count made this really simple! Hurray learning new things!
I was originally going to insert all the counts into a dictionary but
figured out how to do it without that!
@author Ni3h
"""
# def scramble(s1, s2):
#     for i in s2:
#         if i in s1:
#             continue
#         else:
#             return False
#     return True
#
#
# scramble('rkqodlw', 'world')


def scramble(s1, s2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i in s2:
            y = s2.count(i)
            z = s1.count(i)
            if y > z:
                return False
    return True


print(scramble('codewarsaba', 'codewarsa'))
