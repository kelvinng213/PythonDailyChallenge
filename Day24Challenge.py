# Given a number, return the difference between 
# the maximum and minimum numbers that can be formed when the digits are rearranged.

x = int(input("Input a number:"))

lst = []

largest = ''
smallest = ''

for i in str(x):
    lst.append(i)

ascending = sorted(lst)
descending = sorted(lst,reverse=True)

for i in ascending:
    smallest+=i

for i in descending:
    largest+=i

print(int(largest)-int(smallest))