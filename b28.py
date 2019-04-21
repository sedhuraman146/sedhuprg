def rearrangeNaive(arr, n): 
temp = [0] * n 
for i in range(0, n): 
temp[arr[i]] = i 
for i in range(0, n): 
arr[i] = temp[i] 
def printArray(arr, n): 
for i in range(0, n): 
print(arr[i], end = " ") 
arr = [1, 3, 0, 2] 
n = len(arr) 
print("Given array is", end = " ") 
printArray(arr, n) 
print("")  
rearrangeNaive(arr, n) 
print("\nModified array is", end = " ") 
printArray(arr, n) 
