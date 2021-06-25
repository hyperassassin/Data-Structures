def binary_search(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
def exponential_search(lys,val):
    if lys[0] == val:
        return 0
    index = 1
    while index < len(lys) and lys[index] <= val:
        index = index * 2
    return binary_search( lys[:min(index, len(lys))], val)

arr = [2,3,4,10,50,70]
print("Given List : ",arr)
x = int(input("Enter the element to search : "))
result = exponential_search(arr,x)
if(result == -1):
    print("Not Found in the array")
else:
    print("Element is present at index %d" % result)
