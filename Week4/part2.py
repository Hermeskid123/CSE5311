def removeDups(arr):
    l = len(arr)
    dummy = [] 
    k = 0
    for i in range(0, l-1):
        if arr[i] != arr[i+1]:
            dummy.append(arr[i])
    

    dummy.append(arr[l-1]) 
 
    arr = dummy
 
    return dummy
 


array = [2, 2, 2, 2, 2]
res = removeDups(array)
print(res)
array = [1, 2, 2, 3, 4, 4, 4, 5, 5]

res = removeDups(array)
print(res)

