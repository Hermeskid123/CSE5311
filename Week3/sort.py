
def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        
        m = array[r:]
        l = array[:r]
        
        mergeSort(l)
        mergeSort(m)

        i = j = k = 0

        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = m[j]
                j += 1
            k += 1
        
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(m):
            array[k] = m[j]
            j += 1
            k += 1

arr = [5, 2, 4, 7, 1, 3, 2, 6]
mergeSort(arr)
print("Sorted Array:", arr)
