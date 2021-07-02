def heapify(arr,n,i):
    large = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[large] < arr[l]:
        large = l
    if r < n and arr[large] < arr[r]:
        large = r
    if large != i:
        arr[i] , arr[large] = arr[large] , arr[i]
        heapify(arr,n,large)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i] , arr[0] = arr[0] , arr[i]
        heapify(arr,i,0)
    print("Sorted Array : ",arr)

arr = [12,5,78,45,32,1,6,65,100,9]
print("Unsorted Array : ",arr)
heap_sort(arr)
