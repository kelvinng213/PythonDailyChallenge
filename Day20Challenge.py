# Given a string, count all the lowercase letters. Return a dictionary with the keys as the lowercase letters and the values as the letters' counts respectively. 
#The keys should be sorted in alphabetical order.

string = "apple"

dict = {}

for x in string:
    if not x.islower() :
        continue
    elif x not in dict:
        dict[x] = 1
    elif x in dict:
        dict[x] += 1

print(sorted(dict.items()))

# Example:

# Input:

# "apple"

# Output:

# {'a': 1, 'e': 1, 'l': 1, 'p': 2}