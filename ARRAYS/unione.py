arr1=sorted([int(x) for x in input("enter numbers : ").split()])
arr2=sorted([int(x) for x in input("enter numbers : ").split()])
def union(arr1,arr2):
    i=0
    j=0
    unionarr=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            if len(unionarr)==0 or unionarr[-1]!=arr1[i]:
                unionarr.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            if len(unionarr)==0 or unionarr[-1]!=arr2[j]:
                unionarr.append(arr2[j])
            j+=1
        else:
            if len(unionarr)==0 or unionarr[-1]!=arr2[j]:
                unionarr.append(arr1[i])
            i+=1
            j+=1
    while i<len(arr1):
        if unionarr[-1]!=arr1[i]:
            unionarr.append(arr1[i])
        i+=1
    while j<len(arr2):
        if unionarr[-1]!=arr2[j]:
            unionarr.append(arr2[j])
        j+=1
    return unionarr
print(union(arr1,arr2))
    
