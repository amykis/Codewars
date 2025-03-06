'''
Description:
Oh no! Timmy hasn't followed instructions very carefully
and forgot how to use the new String Template feature,
Help Timmy with his string template so it works as he expects!
'''

import re

def build_string(*args):
     # string = f"I like {args}!"
     return re.sub(r"[()']", "", f"I like {args}!")

print(build_string('Cheese','Milk','Chocolate')) #, 'I like Cheese, Milk, Chocolate!', 'Return the correct String')