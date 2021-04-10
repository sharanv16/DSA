# keep finding the minimum element in array
# assume the first element to be the smallest compare with other elements and keep swapping it with other minimum numbers
# replace first place with new minimum
# asuume minimum to be from 2nd place and cont.....


def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j

        arr[i],arr[min]=arr[min],arr[i]

    return arr

A = [8,9,3,7,1,6,2]
print(selectionSort(A))