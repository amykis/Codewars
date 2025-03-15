'''
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

a can contain numbers or strings. x can be either.

Return true if the array contains the value, false if not.
'''

def check(seq, elem):
    while elem in seq:
        return True
    else:
        return False
    pass


print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))