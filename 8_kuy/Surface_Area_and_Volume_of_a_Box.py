'''
Description:
Write a function that returns the total surface area and volume of a box.

The given input will be three positive non-zero integers: width, height, and depth.

The output will be language dependant, so please check sample tests for the corresponding data type, (list, tuple, struct, query, et cetera).
'''

def get_size(w,h,d):
    #your code here
    v = w * d * h
    s = 2 * (w * d + d * h + w * h)
    array = [v, s]
    return array

print(get_size(4, 2, 6))