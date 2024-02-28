1. Implement both versions of quicksort (random and non-random choice for the pivot) and share the GitHub repository with your source code.
    in main.py 
2.  For the non-random pivot version of quicksort show the following benchmarks on the same graph:

    2a) best case (generate a set of inputs that will always be the best case, repeat for multiple array input sizes "n").

    2b) worst case (generate a set of inputs that will always be the worst case, repeat for multiple array input sizes "n").

    2c) average case (generate a set of inputs from a uniform distribution, repeat for multiple array input sizes "n").
Figure_1.png has these graphs 

3. Mathematically derive the average runtime complexity of the non-random pivot version of quicksort.
 
 denote the average runtime complexity as T(n) : n belongs to input arr 

 
the partitioning  takes O(n) time.
then the array is divided into two smaller arrays 
they will have  half the size of the original array
=> [T(n) = 2T(n/2) + O(n)]

Using the Master theorem 
the average runtime complexity of quicksort is O(n /log n).