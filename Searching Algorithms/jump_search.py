import math
def jump_search(arr,v,n):
	step = math.sqrt(n) 
	prev = 0
	while arr[int(min(step, n)-1)] < v: 
		prev = step 
		step += math.sqrt(n) 
		if prev >= n: 
			return -1
	while arr[int(prev)] < v: 
		prev += 1 
		if prev == min(step, n): 
			return -1
	if arr[int(prev)] == v: 
		return prev 
	return -1

arr = [1,2,3,5,8,13,21,34,55,144]
print("Given List : ",arr)
v = int(input("Enter the element to search : "))
n = len(arr)
index = jump_search(arr,v,n)
if(index == -1):
        print("Element Not Found")
else:
        print("Element",v,"is at index","%.0f"%index)
 
