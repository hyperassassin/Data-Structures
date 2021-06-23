def interpolation_search(arr,lo,hi,v):
    if(lo <= hi and v >= arr[lo] and v <= arr[hi]):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo])*(v-arr[lo]))
        if arr[pos] == v:
            return pos
        if arr[pos] < v:
            return interpolation_search(arr,pos + 1,hi,v)
        if arr[pos] > v:
            return interpolation_search(arr,lo,pos - 1,v)
    return -1

arr = [50,53,56,59,65,70,80,85,88,92]
print("Given Array : ",arr)
n = len(arr)
x = int(input("Enter the element to search : "))
index = interpolation_search(arr,0,n-1,x)
if(index != -1):
    print("Element found at index :",index)
else:
    print("Element not found")
