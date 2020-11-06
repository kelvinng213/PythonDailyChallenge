# # Given an input integer x, return a list of integers in which 
# # the sum is equal to x. The integers inside the list must consist of values 
# # that are a power of 3. For example:

# # 1 is a possible number of the list because of 3^0 => 1

# # 3 is also a possible number of the list because 3^1 => 3

# # and so on.

from math import log, floor

x = int(input("Enter an integer: "))

lst = []

while x>0:
    sub = 3**floor(log(x,3))
    lst.append(sub)
    x = x - sub 

print(lst)

# # Example:

# # Input: 

# # 4



# # Output:

# # [1, 3]

# # Because 1 +3 = 4 

# # And 3^0 => 1 and 3^1 => 3



# # Invalid output:

# # [2, 2]

# # Even though 2 + 2 = 4, 

# # 2 is not a power of 3. 

# # Therefore, 2 is an invalid output in the list.

