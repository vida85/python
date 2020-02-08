"""
find the longest sub string,
including doubles
"""

s = 'ajksnoabcdefgemabcfedhj' # result = 'abcdefg'

def longest_sub(s):
    storage, compare, longest = [], [], []
    length = 1
    for i, ii in zip(s, s[1:]):
        if i < ii:
            storage.append(i)
            if len(storage) > length:
                length = len(storage)
                compare = storage
        else:
            if len(storage) == len(compare):
                longest = compare + [i]
            storage = []
    return longest

print(longest_sub(s))
