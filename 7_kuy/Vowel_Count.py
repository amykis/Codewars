'''
Description:
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

def get_count(sentence):
    i = 0
    count = 0
    vowel_point = ['a', 'e', 'i', 'o', 'u']
    while i < len(sentence):
        if sentence[i] in vowel_point:
            count += 1
        i += 1
    return count
    pass