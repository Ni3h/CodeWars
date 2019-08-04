"""
Feels like a roundabout solution, it would clearly be better to have the dictionary created outside of the
alphabet_position method in order to minimize time. Reason this feels roundabout to me is simply time-complexity,
I think it could be made faster.
#author Ni3h
"""
def alphabet_position(text):
    alphabet_string = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dict = {}
    newString = ""
    for i, letter in enumerate(alphabet_string):
        key = i + 1
        alphabet_dict[letter] = str(key)

    for k in text.lower():
        if k in alphabet_dict:
            newString = " ".join([newString, alphabet_dict[k]])
        else:
            continue
    finalString = newString.strip()
    return finalString

