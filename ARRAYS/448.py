'''Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]'''

nums=set([int(x) for x in input("enter numbers : ").split()])

def missing(nums):
    result=[]
    n=len(nums)
    for x in range(1,n+1):
        if x not in nums:
            result.append(x)
    return result
print(missing(nums))
