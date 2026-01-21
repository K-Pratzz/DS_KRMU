'''Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index
 is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because
 there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.'''

nums=[int(x) for x in input("enter the list of numbers:").split()]

def pivot_index(nums):
    totalsum=sum(nums)
    leftsum=0
    for indx,val in enumerate(nums):
        if leftsum==totalsum-leftsum-val:
            return indx
        leftsum+=val
    return -1
print(pivot_index(nums))

