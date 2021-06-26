def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    print("Sorted Array : ",arr)

arr = [52,20,60,87,10,14,36,56,96,5]
print("Unsorted Array : ",arr)
bubble_sort(arr)
