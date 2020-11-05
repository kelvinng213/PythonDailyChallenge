# Given a string, create a function that splits the string into pairs of two characters. 
# Put the pairs inside a list then return the list. If a character is missing in a pair, 
# use the character '?' to replace the missing character.

def challenge13(string):

    newstring = []

    if len(string) %2 != 0:
        string = string + "?"

    for i in range(0, len(string), 2):
        newstring.append(string[i:i+2])

    return newstring

print(challenge13("abcdefg"))
# Example:

# Input: "abcdefg"

# Output = ["ab", "cd", "ef", "g?"]



# Input: "abcdef"

# Output = ["ab", "cd", "ef"]