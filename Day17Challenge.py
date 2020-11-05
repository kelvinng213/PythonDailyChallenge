# Given a list of 11 integers, 
# return a string in the form of a Hong Kong phone number in this format: 
# +852 xxxx xxxx

# Only the numbers 2, 3, 5, 6, 7, and 9 can be added 
# after the extension 852.

lst = [6,0,1,8,5,1,4,2,6,6,2]

newlst = lst.remove(8)
newlst = lst.remove(5)
newlst = lst.remove(2)

string = ""

for x in lst:
    if str(x) == ('2' or '3' or '5' or '6' or '7' or '9'):
        string += str(x)
        lst.remove(x)
        break
    else:
        continue

for y in lst:
    string += str(y)

print('+'+'852'+' '+string[0:4]+' '+string[4:])

# Example 1:

# Input:

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]

# Returns:

# "+852 9134 6701"