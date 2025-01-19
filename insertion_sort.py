def insertion_sort(arr):
    for i in range(1, len(arr)): # 1 , 2 , 3, 4 
        
        key = arr[i]                   #key ===  >  13
        j = i - 1                        # 0
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        
        arr[j + 1] = key
        print(arr)
      
# Example 1
arr1 = [19, 13, 5, 6, 15]
insertion_sort(arr1)
print(arr1)  # Output: [5, 6, 11, 12, 13]

# # Example 2
# arr2 = [3, 1, 2, 10, 7]
# insertion_sort(arr2)
# print(arr2)  # Output: [1, 2, 3, 7, 10]
