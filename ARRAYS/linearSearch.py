nums=[int(x) for x in input("enter numbers : ").split()]
target=int(input("enter target :"))
def linearSearch(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
print(linearSearch(nums,target))
