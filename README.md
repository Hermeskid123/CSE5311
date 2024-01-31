Preston Mann

1.) 
in this repo I have implmented insertion sort,selection sort and bubble sort
2.)
selection sort divids the A into two sections a sorted part and the unsorted part. In each iteration, we select the smallest element from the unsorted selection then we swap it with the first element of the unsorted section like cards this algo will cont until the entire array is sorted.

the algo has is correct since 

Initialization: At the beginning of each iteration the we have the let side as sorted and the right side as unsorted

Maintenance: After each iteration, the smallest element is moved into the sorted part keeping its correctness 
    
Termination: The algorithm terminates when the un sorted side is empty and the left side is sorted 

Invariant: At the end of each iteration for the loop we put the smallest element into the sorted side of the section 


3.) code results refer to benchmark.png for graph 
     *-memory
          description: System memory
          physical id: 0
          size: 16GiB
     *-cpu
          product: Intel(R) Core(TM) i7-6820HQ CPU @ 2.70GHz
          vendor: Intel Corp.
          physical id: 1
          bus info: cpu@0
          size: 3281MHz
          capacity: 3600MHz
          width: 64 bits



Results CLI 
array size for Isertion sort:  5
time it took:  4.291534423828125e-06
array size for Isertion sort:  10
time it took:  5.245208740234375e-06
array size for Isertion sort:  20
time it took:  2.9325485229492188e-05
array size for Isertion sort:  50
time it took:  9.107589721679688e-05
array size for Isertion sort:  100
time it took:  0.0003333091735839844
array size for Isertion sort:  200
time it took:  0.0011131763458251953
array size for Isertion sort:  500
time it took:  0.0074727535247802734
array size for Isertion sort:  1000
time it took:  0.03108072280883789
array size for Isertion sort:  9999
time it took:  3.186392068862915
array size for Isertion sort:  19999
time it took:  13.21232557296753


array size for selection sort:  5
time it took:  5.245208740234375e-06
array size for selection sort:  10
time it took:  7.152557373046875e-06
array size for selection sort:  20
time it took:  3.3855438232421875e-05
array size for selection sort:  50
time it took:  0.0004220008850097656
array size for selection sort:  100
time it took:  0.0005826950073242188
array size for selection sort:  200
time it took:  0.002168893814086914
array size for selection sort:  500
time it took:  0.01118016242980957
array size for selection sort:  1000
time it took:  0.03776216506958008
array size for selection sort:  9999
time it took:  3.325484037399292
array size for selection sort:  19999
time it took:  15.275840282440186


array size for bubble sort:  5
time it took:  4.76837158203125e-06
array size for bubble sort:  10
time it took:  3.0517578125e-05
array size for bubble sort:  20
time it took:  2.6226043701171875e-05
array size for bubble sort:  50
time it took:  0.0001475811004638672
array size for bubble sort:  100
time it took:  0.0005600452423095703
array size for bubble sort:  200
time it took:  0.0023431777954101562
array size for bubble sort:  500
time it took:  0.016957998275756836
array size for bubble sort:  1000
time it took:  0.06634163856506348
array size for bubble sort:  9999
time it took:  7.735508441925049
array size for bubble sort:  19999
time it took:  29.475936889648438


python3 sort.py  74.04s user 0.62s system 98% cpu 1:16.05 total

