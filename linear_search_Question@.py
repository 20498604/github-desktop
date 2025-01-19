array=[0, 4, 2, 8, 6, 3,12,-1, 2]
target=0
list1=[]
for i in range(len(array)):
    if array[i]==target:
        list1.append(i)
print(list1)