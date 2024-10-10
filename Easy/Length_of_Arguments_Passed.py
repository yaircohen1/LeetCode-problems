# Write a function argumentsLength that returns the count of arguments passed to it.

# Example 1:

# Input: args = [5]
# Output: 1
# Explanation:
# argumentsLength(5); // 1

# One value was passed to the function so it should return 1.

# Example 2:

# Input: args = [{}, null, "3"]
# Output: 3
# Explanation:
# argumentsLength({}, null, "3"); // 3

# Three values were passed to the function so it should return 3.

# Solution:
# 1. Use the len() function to return the count of arguments passed to the function.

def argumentsLength(*args):
    return len(args)

# Test cases
print(argumentsLength(5)) # 1
print(argumentsLength({}, None, "3")) # 3
print(argumentsLength(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # 10