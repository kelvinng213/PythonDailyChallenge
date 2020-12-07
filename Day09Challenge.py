#Given a string, add or subtract numbers and return the answer.



#Example:

#Input: 1plus2plus3minus4

#Output: 2

#Input: 2minus6plus4plus7

#Output: 7

def evaltoexpression(s):
    
    s = s.replace('plus','+')
    s = s.replace('minus','-')
    return eval(s)

print(evaltoexpression('1plus2plus3minus4'))