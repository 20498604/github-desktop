'''Given an array of integers, write a function to find all pairs of elements whose sum equals 
a given target using:
A naive approach (nested loops).
An optimized approach using sorting and Binary Search.

'''
# a naive appproach (nested loops)

array=[1,10,13,4,5,6,0, 5 ]
Target=10
# for i in range(0, len(array)):
#     for j in range(i+1, len(array)):
#             #print(array[i], array[j])
#             if array[i]+array[j]==Target:
#                   print(array[i], array[j])

# lets sort this array first using sorting algorithm

for i in range(len(array)):                  # 0 ,1 , 2 , 3, 4, 5 ,6 , 7
      for j in range(0, len(array)-i-1):       
            if array[j]>array[j+1]:
                array[j] , array[j+1]=array[j+1] , array[j]
                  
print("sorted array is:::", array)

                  
# let assume our target is 4 and we need to find its index using binary search.
left=0
right=len(array)-1
while left<=right:
     mid=(left+right)//2
     if array[mid]==Target:
          
          print("index is :: ", mid," and element is :::" , array[mid])
          break
     elif array[mid] < Target:
          left = mid +1
     else:
           right = mid -1

# lets find out how can we find the pair whose sum is target.


def find_pair(array, target):
     
    list1=[]
    left=0
    right=len(array)-1
    while left<=right:
          
        if array[left]+array[right]==target:
             list1.append((array[left] , array[right]))
             left+=1
             right-=1
            
        elif array[left]+array[right]>target:
               right=right-1
        elif array[left]+array[right]<target:
             left+=1
    return list1
print(find_pair([0, 1, 4, 5, 5, 6,9,  10,10, 12,  13], 10))