# Given a string of decimal digits, 
# output an integer of its binary representation like below:

str = "2973"

output = ""

step = 0
binary = 2**step


for x in str:
    if x == "9":
        output += "1001"
    elif x == "8" :
        output+="1000"
    elif x == "7" :
        output+="111"
    elif x == "6" :
        output+="110"
    elif x == "5":
        output+="101"
    elif x == "4":
        output+="100"
    elif x == "3":
        output+="11"
    elif x == "2":
        output+="10"
    elif x == "1":
        output+="1"

print(output)

    

# Example:

# Input: "2973"

# "2" => 10

# "9" => 1001

# "7" => 111

# "3" => 11

# Therefore output is 10100111111, because of 10+1001+111+11.