"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

"""

def minSubArrayLen(target, nums):
    start = 0
    total = 0
    min_length = float('inf')

    for end in range(len(nums)):
        total += nums[end]

        while total >= target:
            length = end - start + 1

            if length < min_length:
                min_length = length

            total -= nums[start]
            start += 1

    if min_length == float('inf'):
        return 0

    return min_length


target = 7
nums = [2, 3, 1, 2, 4, 3]

print(minSubArrayLen(target, nums))