'''Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.'''

nums=[int(x) for x in (input("enter the list of numbers:")).split()]
def max_sub_sum(nums):
    max_sum=nums[0]
    curr_sum=nums[0]
    for x in nums[1:]:
        curr_sum=max(x,curr_sum+x)
        max_sum=max(max_sum,curr_sum)
    return max_sum
print(max_sub_sum(nums))