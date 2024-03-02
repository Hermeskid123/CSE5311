#preston Mann
# testing function on hard coding arr
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key :
                A[i + 1] = A[i]
                i = i - 1
        A[i + 1] = key

def selectionSort(A):
    for j in range(len(A)):
        min_index = j
        for i in range(j + 1, len(A)):
            if A[i] < A[min_index]:
                min_index = i
        A[j], A[min_index] = A[min_index], A[j]
     
def bubbleSort(A):
    for i in range(len(A)):
        for j in range(0,len(A) - i-1): 
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
A = [4,7,3,34,7,2,6,4,3,56,4,3,6]
insertionSort(A)
print(A)
A = [4,7,3,34,7,2,6,4,3,56,4,3,6]
selectionSort(A)
print(A)
A = [99,2,3,34,7,23,6,9,3,56,4,3,0]
bubbleSort(A)
print(A)
