#Given two integer inputs n and d, create a function that squares all numbers 
# from 1 to n, then returns the count of all instances of d from the square 
# results.  

def num8():
    lst = []
    string = ""
    n = int(input("Enter # of numbers: "))
    d = int(input("Enter number to find instances: "))
    for x in range(1,n+1):
        lst.append(x*x)
        string += str(x*x)
    return lst, string.count(str(d))

print(num8())



# Example: 

# n: 5

# d: 1

# square of numbers from 1 to 5: 1, 4, 9, 16, 25

# returns: 2 (since there's 2 instances of the digit 1, in 1 and 16)

