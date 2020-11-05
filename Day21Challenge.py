# Given a list of mixed integers of different representations, 
# add up the non-string integers and subtract this from the total of string integers.

lst = [1,'2',3,'4',5]

add = []
subtract = []

for x in lst:
    if type(x) != str:
        add.append(x)
    else:
        subtract.append(int(x))

print(sum(subtract) - sum(add))

# Example:

# Input:

# [1, '2', 3, '4', 5]

# Output:

# -3, because:

# total of non-string integers = 1+3+5 = 9

# total of string integers = 2+4 = 6

# total of string integers - total of non-string integers = -3 

