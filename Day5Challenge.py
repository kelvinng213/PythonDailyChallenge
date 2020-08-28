#Create a function that given an n positive integer, 
# it sums all the cubed values from 1 to n. Return the sum.

def sum_cubes(n):
    sum = 0
    for x in range(1,n+1):
        sum += x*x
    return sum

print(sum_cubes(3))
