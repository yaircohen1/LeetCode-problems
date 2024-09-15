# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Solution:
# 1. Create an empty dictionary
# 2. Loop through the array
# 3. Calculate the difference between the target and the current number
# 4. Check if the difference is in the dictionary
# 5. If it is, return the index of the difference and the current index
# 6. If it is not, add the current number and its index to the dictionary

def twoSum(nums, target):
    num_dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in num_dict:
            return [num_dict[diff], i]
        num_dict[nums[i]] = i

# Test cases
print(twoSum([2,7,11,15], 9)) # [0, 1]
print(twoSum([3,2,4], 6)) # [1, 2]
print(twoSum([3,3], 7)) # None
print(twoSum([3,2,4,5,6,7,8,9,10], 15)) # [5, 6]

