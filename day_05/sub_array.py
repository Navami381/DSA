nums = [-2,1,-3,4,-1,2,1,-5,4]

largest = nums[0]

for i in range(0,len(nums)):
  
  total = nums[i]
  
  for j in range(i+1,len(nums)):
    
    total+=nums[j]
    
    if total>largest:
    
     largest=total
    
print(largest)