'''
Description:
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
'''

def find_average(numbers):
    # your code here
    if not numbers:
        return 0
    else:
        average = sum(numbers) / len(numbers)
        return average
    pass