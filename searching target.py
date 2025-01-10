"""Search Element in Sorted Array
Write a program to search for a target element in a sorted array using Binary Search.
Input: arr = [2, 5, 8, 12, 16, 23, 38, 56, 72], target = 23
Output: Index = 5

"""

def searching_target(arr, target):
    left , right= 0, len(arr)-1
    while left <= right:
        mid=(left+right)//2
        if arr[mid]==target:
            return (mid , target)
        elif arr[mid]<target:
            left=mid+1
        
        elif arr[mid]>target:
            right=mid-1
            
    return -1 # if no target is found 

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72]
target = 2
print(searching_target(arr, target))