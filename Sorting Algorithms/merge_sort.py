def merge_sort(arr):
    if len(arr) > 1 :
        mid = len(arr)//2
        lh=arr[:mid]
        rh=arr[mid:]
        merge_sort(lh)
        merge_sort(rh)
        i=0;j=0;k=0
        while(i < len(lh) and j < len(rh)):
            if lh[i] < rh[j]:
                arr[k]=lh[i]
                i = i + 1
            else :
                arr[k]=rh[j]
                j = j + 1
            k = k + 1
        while(i < len(lh)):
            arr[k]=lh[i]
            i = i + 1
            k = k + 1
        while(j < len(rh)):
            arr[k]=rh[j]
            j = j + 1
            k = k + 1
        return(arr)
    
arr = [88,100,23,45,11,77,83,8,18]
print("Unsorted Array : ",arr)
print("Sorted Array : " , merge_sort(arr))
