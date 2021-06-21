def binary_search(arr,data):
    first = 0
    last = len(arr)-1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if data == arr[mid]:
            found = True
        else:
            if data < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
    
arr = [2,3,4,10,50]
print("Given List :- " , arr)
x = int(input("Enter the element to search :- "))
print("Found :-" , binary_search(arr,x))
