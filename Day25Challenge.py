# An anagram is a word, x, formed by rearranging the letters that make up another word, y, and using up all the letters in y at the same frequency. For example, "dear" is an anagram of "read" and "plead" is an anagram of "paled".

# The Hamming distance between two strings is the number of positions at which they differ. Hamming distances can only be calculated for strings of equal length.

# s1 = "eleven"

# s2 = "twelve"

# They only have the third position (index 2) in common, giving them a Hamming distance of 5.

# As anagrams are of identical length, the Hamming distance between them can be calculated.

# s1 = "read"

# s2 = "dear"

# These strings differ at the first and last positions, giving them a Hamming distance of 2. "Plead" and "paled" have a Hamming distance of 3.

# Create a function that takes two strings, and returns:

# True if they are anagrams of each other and their Hamming distance is equal to their length (i.e. no letters in the same positions).

# False if they aren't anagrams, or Their Hamming distance if they are anagrams with >=1 letter at the same index. Examples

# max_ham("dear", "read") ➞ 2

# max_ham("dare", "read") ➞ True

# max_ham("solemn", "molest") ➞ False