def quick(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j] <= pivot :
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return(i+1)
def  quick_sort(arr,low,high):
    if low < high :
        p=quick(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

arr = [88,100,23,45,11,77,83,8,18]
print("Unsorted Array : ",arr)
quick_sort(arr,0,len(arr) - 1)
print("Sorted Array : ",arr)
