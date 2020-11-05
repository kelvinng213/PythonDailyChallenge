# Given an integer n, 
# find all the integers that is the multiple of 3 from 0 to n.
# Return the sum of all these integers.

n = 15

lst = []

for i in range(0,n+1,3):
    lst.append(i)

print(lst[1:])
print(sum(lst))


# Example:

# Input: 

# 10

# Multiples of 3 from 0 to 10:

# 3, 6, 9

# Return sum of these integers:

# 18