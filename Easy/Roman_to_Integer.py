#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
#Input: s = "III"
#Output: 3
#Explanation: III = 3.

#Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Solution:
# 1. Create a dictionary with the Roman numerals and their corresponding values
# 2. Initialize a variable to store the result
# 3. Loop through the input string
# 4. Check if the current Roman numeral is smaller than the next Roman numeral
# 5. If it is, subtract the current value from the result
# 6. If it is not, add the current value to the result
# 7. Return the result

def romanToInt(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s) - 1):
        if roman_dict[s[i]] < roman_dict[s[i + 1]]: # Check if the current value is smaller than the next value
            result -= roman_dict[s[i]] # Subtract the current value
        else:
            result += roman_dict[s[i]] # Add the current value
    result += roman_dict[s[-1]] # Add the last value
    return result

# Test cases
print(romanToInt("III")) # 3
print(romanToInt("LVIII")) # 58
print(romanToInt("MCMXCIV")) # 1994