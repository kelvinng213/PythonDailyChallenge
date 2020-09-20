#Given an integer, create a function that finds and returns the length of the longest binary gap 
# of the binary representation of that integer. A binary gap is the sequence of consecutive zeros 
# in between ones in a binary representation. Reference for binary representation can be found here:
#  https://www.rapidtables.com/convert/number/decimal-to-binary.html

import math
def binar(n):
    binaryrep = 0
    while n != 0:
        x = math.log(n) / math.log(2)
        roundedx = math.floor(x)
        binaryrep += (10**roundedx)
        n = n - 2**roundedx
    lst = []
    lenlst = []
    for x in (str(binaryrep)).split("1"):
        lst.append(x)
    for y in lst:
        lenlst.append(len(y))
    return max(lenlst)

print(binar(529))

#Example:

#Input: 9, which has binary representation 1001

#Returns: 2
#Input: 529, which has binary representation 1000010001

#Returns: 4
#Input: 20, which has binary representation 10100

#Returns: 1

#Input: 15, which has binary representation 1111
#Returns: 0