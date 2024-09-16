# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
#
# Example 1:
# Input: timePoints = ["23:59","00:00"]
# Output: 1
#
# Example 2:
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
#
# Constraints:
# 2 <= timePoints.length <= 2 * 104
# timePoints[i] is in the format "HH:MM".

# Solution:
# 1. Convert the time in minutes and sort the list.
# 2. sort the time points and find the difference between two consecutive time points.
# 3. Find the minimum difference between two consecutive time points.

def findMinDifference(time_points):
    def convert(time):
        return int(time[:2]) * 60 + int(time[3:]) # Convert the time in minutes

    time_points = sorted(map(convert, time_points)) # Sort the time points
    return min((y - x) % (24 * 60) for x, y in zip(time_points, time_points[1:] + time_points[:1])) # Find the minimum difference between two consecutive time points
    # zip is function which combines two lists and returns a tuple of the elements of the two lists.
    # list 1 is the time_points and list 2 is the time_points shifted by 1 element to the right + the first element of the list)

    # Time complexity: O(nlogn) where n is the number of time points
    # convert function takes O(1) time
    # sorted function takes O(nlogn) time

    # min function takes O(n) time because:
    # zip function takes O(n) time
    # calculating the difference between two consecutive time points takes O(1) time

    # Overall time complexity = O(nlogn) + O(n) = O(nlogn)


# Test Cases
print(findMinDifference(["23:59","00:00"])) # 1
print(findMinDifference(["00:00","23:59","00:00"])) # 0
print(findMinDifference(["00:00","12:00","23:59"])) # 1
print(findMinDifference(["00:00","12:00"])) # 720 (12*60)

