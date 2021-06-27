def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        value = arr[i]
        pos = i
        while pos > 0 and value < arr[pos-1] :
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = value
    print("Sorted Array : ",arr)

arr = [78,10,5,63,45,13,66,98,40]
print("Unsorted Array : ",arr)
insertion_sort(arr)
