def linear_search(arr,n,x):
	for i in range(0,n):
		if (arr[i] == x):
			return i
	return -1
	
arr = [2,3,4,10,40]
print("Given List : ",arr)
x = int(input("Enter the element to search : "))
n = len(arr)
res = linear_search(arr,n,x)
if(res == -1):
	print("Element Not Found")
else:
	print("Element present at index : ",res)