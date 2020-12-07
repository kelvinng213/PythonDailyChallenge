#Given a list of integers, 
# create a function that finds the odd one out in the list.

def oddoneout(lst):
    dic = {}
    for x in lst:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    if min(dic,key=dic.get) == max(dic,key=dic.get):
        return "No odd one in the list"
    else:
        return(min(dic,key=dic.get))       

print(oddoneout([1,1,1,1,1,1,1,2]))

#Example:

#Input: [1,1,1,1,1,1,1,2]

#Output: 2

