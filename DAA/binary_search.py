def binarySearch(arr,start,end,target):
    if end >= start:
        mid = (start +end)//2
        if arr[mid]==target:
            return mid+1
        elif arr[mid]>target:
            return binarySearch(arr,start,mid-1,target)
        else:
            return binarySearch(arr,mid+1,end,target)
    else:
        return "target not found"

a=[1,2,3,4,5,6,7,8,9]
x=binarySearch(a,0,8,5)
print(x)

