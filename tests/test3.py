#Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.
#Example 1:
#Input: nums = [-4,-2,1,4,8]
#Output: 1

nums = [-4,-2,1,4,8]

# def findClosestNumber(nums):
#     num = float('inf')
#     for i in nums:
#         a=abs(num)
#         # if abs(i) < a:
#         #     num=i
#         # elif i == a:
#         #     if i>num:
#         #         num=i
#     return num

def clnumber(nums):
    num = float('inf')
    for i in nums:        
        a = abs(num)
        if abs(i)<= a:
            num = i
        elif i == a:
            if i> num:
                num = i
        print("The vallule of I is",i)
        print("The value of num is ", num)
        print("the value of a is ", a)
    return num
print(clnumber(nums))