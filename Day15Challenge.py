# Given two lists of any data type, 
# return a list that combines the two lists by alternating the elements
# passed. The input lists can be of different lengths.

lst1 = [1,2,3,4,5,6,7]
length1 = len(lst1)
lst2 = ['a','b','c','d','e','f','g','h','i']
length2 = len(lst2)

difference = length1 - length2 

lst = []

lstfinal = (list( zip(lst1,lst2)))
for x in lstfinal:
    for y in list(x):
        lst.append(y)

if difference > 0:
    add = lst1[-difference:]
    print(lst+add)
elif difference < 0:
    add = lst2[difference:]
    print(lst+add)
else:
    print(lst)






# Example 1:

# Input lists: 

# [1, 2, 3, 4, 5]

# ['a', 'b', 'c', 'd', 'e']

# Returns:

# [1, 'a', 2, b', 3, 'c', 4, 'd', 5, 'e']



# Example 2:

# Input lists:

# [1, 2, 3]

# ['a', 'b', 'c', 'd', 'e']

# Returns:

# [1, 'a', 2, 'b', 3, 'c', 'd', 'e']



# Example 3:

# Input lists:

# [1, 2, 3, 4, 5]

# ['a', 'b']

# Returns:

# [1, 'a', 2, 'b', 3, 4, 5]