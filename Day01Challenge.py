#Create a function that removes all capital letters and punctuation in a string. Return the clean string.

import string 
def clean_string(s):
    new = ''     
    for n in s:         
        if (n.isupper() == False) and n not in string.punctuation: 
            new += n     
    return new 

print(clean_string("!@#$%^&*()ASDFGHJKLasdfghjkl;"))