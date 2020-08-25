# Create a function that estimates the weight loss of a person using a certain weight loss program with their gender, current weight and how many weeks they plan to do the program as input. If the person follows the weight loss program, men can lose 1.5% of their body weight per week while women can lose 1.2% of their body weight per week. 

# The possible inputs are:

# Gender: 'M' for Male, 'F' for Female

# Current weight: integer above 0

# Number of weeks: integer above 0

# Return the estimated weight after the specified number of weeks.

def lose_weight(gender, weight, duration):

    return weight