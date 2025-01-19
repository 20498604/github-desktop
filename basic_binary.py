# 1. Basic Binary Search Implementation

# Input 1:
# Array: [1, 3, 5, 7, 9, 11], Target: 7
# Output: 3 (Index of 7)

# Input 2:
# Array: [2, 4, 6, 8, 10], Target: 5
# Output: -1 (5 not found)

Array= [ 1, 3, 5, 7, 9, 11] # 6
Target= 7

left=0
right=len(Array)-1

while left<=right:
    mid=(left+right)//2
    if Array[mid]==Target:
        print(mid, Array[mid])
        break
    elif Array[mid]<Target:
        left=mid+1
    elif Array[mid]>Target:
        right=mid-1
    

    