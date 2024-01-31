#inertionSort selection sort and bubble sort 
#import 
import time
import random
import matplotlib.pyplot as plt
def makeArr(array_size):
    arr = [random.randint(1, 100) for _ in range(array_size)]
    return arr

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
 

def benchMarkI():
    totalTime = [] 
    for i in range(0,len(sizes)):
        a = makeArr(sizes[i])
        start = time.time()
        insertionSort(a)
        end = time.time()
        print("array size for Isertion sort: " , sizes[i])
        print("time it took: ",end-start)
        totalTime.append(end-start)
    return totalTime

def benchMarkS():
    totalTime = [] 
    for i in range(0,len(sizes)):
        a = makeArr(sizes[i])
        start = time.time()
        selectionSort(a)
        end = time.time()
        print("array size for selection sort: " , sizes[i])
        print("time it took: ",end-start)
        totalTime.append(end-start)
    return totalTime

def benchMarkB():
    totalTime = [] 
    for i in range(0,len(sizes)):
        a = makeArr(sizes[i])
        start = time.time()
        bubbleSort(a)
        end = time.time()
        print("array size for bubble sort: " , sizes[i])
        print("time it took: ",end-start)
        totalTime.append(end-start)

    return totalTime



sizes = [5, 10, 20, 50, 100, 200, 500, 1000,9999,19999]

timeI = benchMarkI()
print("\n")
timeS = benchMarkS()
print("\n")
timeB = benchMarkB()
print("\n")

plt.plot(sizes, timeI, label="insertion sort")
plt.plot(sizes, timeS, label="selection sort")
plt.plot(sizes, timeB, label="bubble sort")

plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.title('Sorting Algorithm Benchmark')
plt.legend()
plt.show()
plt.savefig('benchmark.png')


