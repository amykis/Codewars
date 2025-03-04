'''
Description:
Define a method named countCharOccurrences or count_char_occurrences that accepts
a string and a char as inputs and returns the number of times the char occurs in the string as an int.
'''

def count_char_occurrences(string, char):
    count = 0
    i = 0
    while i < len(string):
        if string[i] == char:
            count += 1
        i += 1
    return count
    pass


def count_char_occurrences1(string, char):
    count = 0
    for e in string:
        if char == e:
            count += 1
    return count
    pass

print(count_char_occurrences1("missippi", 'i'))

