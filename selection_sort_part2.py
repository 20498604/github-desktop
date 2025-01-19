def selection_sort(array):
    for i in range(len(array)):
    
        for j in range(i+1, len(array)):
            if array[i]>array[j]:
                
                array[i], array[j] =array[j] , array[i]
            else: 
                pass
    return array



array=[29, 10, 14, 37, 14]
print(selection_sort(array))