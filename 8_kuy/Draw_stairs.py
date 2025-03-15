'''
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

For example n = 3 result in:

"I\n I\n  I"
or printed:

I
 I
  I
Another example, a 7-step stairs should be drawn like this:

I
 I
  I
   I
    I
     I
      I
'''
def draw_stairs(n):
    word = ''
    i = 0
    while i < n - 1:
        word = word + (' ' * i + 'I\n')
        i += 1
    return word + ' ' * i + 'I'

print(draw_stairs(3))