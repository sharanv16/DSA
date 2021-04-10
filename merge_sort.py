# divide the array into two halves until only one element is present



def mergesort(arr):

    if len(arr) >1:
        mid = len(arr)//2
        l = arr[:mid]
        r= arr[mid:]

        mergesort(l)
        mergesort(r)

        i=j=k=0

        while i < len(l) and j < len(r):
            if l[i]>r[j]:
                arr[k]=l[i]
                i += 1
            else:
                arr[k]=r[j]
                j +=1
            k+=1

        while i <len(l):
            arr[k]=l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k]=r[j]
            j+=1
            k+=1



