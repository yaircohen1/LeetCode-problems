# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Solution:
# 1. Initialize the prefix variable with the first string in the array
# 2. Loop through the remaining strings in the array
# 3. Compare each character of the prefix with the characters of the current string
# 4. Update the prefix to the common characters

def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0: # Check if the prefix is a substring of the current string
            prefix = prefix[:-1] # Remove the last character from the prefix
            if not prefix: # If the prefix becomes empty, return an empty string
                return ""
    return prefix
