#Given a string, return the character with the most value. 
# The value of a character is the difference between the index of its first occurrence 
# and the index of its last occurrence. If there is a tie, return the character that goes 
# first alphabetically.

x = 'abcdbcd'
setx = set(x)
alpha = {}
for y in setx:
    value = x.rfind(str(y)) - (x.find(str(y)))
    alpha[y] = value
abc = sorted(alpha, key=lambda x: (-alpha[x], x))
print(abc[0])

#Example:

#Input: 'abcdbcd'

#Output: 'b', since difference between first index and last index = 4 - 1 = 3, which ties with the values of c and d but since b goes first alphabetically, that's the most valuable character.