"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""
nums = [2,7,11,15]
target = 9
result=[]
for num in nums:
    difference=target-num
    if difference in nums:
        result.append(nums.index(num))
        result.append(nums.index(difference))
        print(result)
        break
