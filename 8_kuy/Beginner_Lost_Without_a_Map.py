'''
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''

def maps(a):
    i = 0
    while i < len(a):
        a[i] *= 2
        i += 1
    return a
    pass

print(maps([1, 2, 3]))