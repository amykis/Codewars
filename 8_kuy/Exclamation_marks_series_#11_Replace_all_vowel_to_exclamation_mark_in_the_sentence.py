'''
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
'''

def replace_exclamation(st):
    for i in st:
        if i in 'aeiouAEIOU':
            st = st.replace(i, '!')
    return st

print(replace_exclamation("ABCDE"))