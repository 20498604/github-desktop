"""
Test Result
35. Search Insert Position
Solved
Easy

Topics
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexit
"""


def searching_target(nums, target):
  
    left=0
    right=len(nums)-1

    while left <=right:
        mid=(left + right)//2
        if nums[mid]==target:
            return mid 
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left
nums=[1,2,3,4,6,7,8]
target=5
print(searching_target(nums, target))