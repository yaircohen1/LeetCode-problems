# Given an integer x, return true if x is a palindrome ,and false otherwise.
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Solution:
# 1. Convert the integer to a string
# 2. Check if the string is equal to its reverse
# 3. If it is, return True
# 4. If it is not, return False

def isPalindrome(x):
    return str(x) == str(x)[::-1]

# Test cases
print(isPalindrome(121)) # True
print(isPalindrome(-121)) # False
print(isPalindrome(10)) # False
print(isPalindrome(12321)) # True