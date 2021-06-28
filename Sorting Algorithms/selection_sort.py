def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        sindex=i
        for j in range(i+1,n):
            if arr[j] < arr[sindex]:
                sindex = j
        if sindex != i:
            arr[i] , arr[sindex] = arr[sindex] , arr[i]
    print("Sorted Array : ",arr)

arr = [88,100,23,45,11,77,83,8,18]
print("Unsorted Array : ",arr)
selection_sort(arr)
