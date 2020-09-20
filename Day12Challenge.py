#Given a list of 5 floats, return a tuple of the average of the middle 3 floats and the lowest float of that list.

def floatlst(lst):
    x = min(lst)
    a = round(((lst[1]+lst[2]+lst[3])/3),2)
    t = (a,x)
    return t

print(floatlst([6.4, 11.4, 7.6, 10.5, 8.1]))
#Example:

#Input:

#[6.4, 11.4, 7.6, 10.5, 8.1]

#Returns:

 #(9.83, 6.4), 9.83 (rounded off to nearest two decimal places) is the average of 11.4, 7.6 and 10.5 and 6.4 is the lowest float of the list.