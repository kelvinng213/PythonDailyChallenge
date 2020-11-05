# Given a list of integers, split the list into two, put the arrays on top of each other, 
# then add them together. Return the finished list.

import numpy as np

def day14challenge(lst):

    upto = len(lst)//2
    top = lst[0:upto]
    bottom = lst[upto:len(lst)]

    if len(lst) % 2 != 0:
        top.append(0)

    top = np.array(top)
    bottom = np.array(bottom)
    answer = top + bottom 
    return answer

print(day14challenge([1,2,3,4,5,6,7]))

# Example:

# Input:

# [1, 2, 3, 4, 5, 6, 7]



# Putting on top:

# [1, 2, 3]

# [4, 5, 6, 7]



# Adding up process:

# [1, 2, 3]

# +

# [4, 5, 6, 7]

# ------------

# [5, 7, 9, 7]



# Returns:

# [5, 7, 9, 7]