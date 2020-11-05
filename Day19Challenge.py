# Given a string of names with a certain pattern, return a formatted string with a certain pattern. 

import re, string

str = 'Alfred:Black;Carey:Drake;Elena:Ferguson;Georgina:Harrison'

punc = string.punctuation

lst = re.split("[" + string.punctuation + "]+", str)[::-1]
print(lst)

for x in lst:
    print(x)

# Example:

# Input:

# "Alfred:Black;Carey:Drake;Elena:Ferguson;Georgina:Harrison"

# Output:

# "(BLACK, ALFRED)(DRAKE, CAREY)(FERGUSON, ELENA)(HARRISON, GEORGINA)"

