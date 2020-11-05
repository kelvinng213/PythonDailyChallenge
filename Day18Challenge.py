# Given an integer greater than 0, return a list of all possible palindromes of the integer.

int = str(34322122)
lst = []

while len(int) > 0:
    for x in range(1,len(int)+1,1):
        lst.append(int[0:x])
        if int[0:x] == int:
            int = int[1:]

palindromes = []

for x in lst:
    if len(x) > 1 and x == x[::-1]:
        palindromes.append(x)

palindromes = set(palindromes)

print(palindromes)

# Example:

# Input: 

# 34322122

# Output:

# [22, 212, 343, 22122]