nums=[int(x) for x in input("enter numbers : ").split()]
def maxConsecutiveOnes(nums):
    max_count=0
    count=0
    for x in nums:
        if x==1:
            count+=1
            max_count=max(max_count,count)
        else:
            count=0
    return max_count
print(maxConsecutiveOnes(nums))

