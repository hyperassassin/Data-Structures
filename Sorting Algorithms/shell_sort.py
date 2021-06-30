def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = gap//2
    print("Sorted Array : ",arr)
arr = [88,100,23,45,11,77,83,8,18]
print("Unsorted Array : ",arr)
shell_sort(arr)
