# Create a function that calculates how many times an integer can be divided by another given integer. 
# If the answer of resulting divisions does not result in an integer, that division is not counted towards 
# the number of times. As an example: 

# If n is 10 and divisor is 3, since in the first division 10/3 doesn't return an integer, 
# this division doesn't count towards the number of times and therefore its number of times should be 0.

def divisions(n,division):
    number_of_times = 0
    while True:
      if n%division == 0:
        x = n//division
        n = n - x
        number_of_times += 1
      elif n%division != 0:
        break
    return(number_of_times)

print(divisions(100,2))

