nums=[int(x) for x in input("enter numbers :").split()]
k=int(input("enter k :"))
direction=input("enter direction :").lower()
def rotate(nums,direction,k):
    if len(nums)==0:
        return []
    if direction=="left":
        while k>0:
            first=nums[0]
            for i in range(1,len(nums)):
                nums[i-1]=nums[i]
            nums[-1]=first
            k-=1
    elif direction=="right":
        while k>0:
            last=nums[-1]
            for i in range(len(nums)-1,0,-1):
                nums[i]=nums[i-1]
            nums[0]=last
            k-=1
    return nums
print(rotate(nums,direction,k))

