#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.

#Example 1:

#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]

nums = [1,2,3,4]

leng = len(nums)
result = 1
for i in range(leng):
    if i == nums[i]:
        print(f'{i} is skipped')
        pass
    else:    
        result = result * nums[i]
    
    print(result)
   