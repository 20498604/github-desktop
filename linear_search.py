# #2. Find Maximum and Minimum in an Array

# Input 1:
# Array: [4, 2, 8, 6, 3]
# Output: Max: 8, Min: 2

# Input 2:
# Array: [10, 15, 7]
# Output: Max: 15, Min: 7

array=[0, 4, 2, 8, 6, 3,12,-1]
max=array[0]
min=array[0]
for i in range(1, len(array)):
    if array[i]>max:
        max=array[i]
    if array[i]<min:
       
        min=array[i]
print("max", max)
print("min", min)




