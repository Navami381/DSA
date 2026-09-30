"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""
nums = [0, 1, 0, 3, 12]

position = 0

for num in nums:
    if num != 0:
        nums[position] = num   #add non zero number to position
        position += 1

while position < len(nums): #len(nums) is 5 and position=3 ,so 3<5
    nums[position] = 0
    position += 1

print(nums)