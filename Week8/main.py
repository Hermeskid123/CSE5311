import random
import time
import matplotlib as plt
class SortingBenchmark:
    def __init__(self, sizes, repetitions=3):
        self.sizes = sizes
        self.repetitions = repetitions
    
    @staticmethod
    def quicksort_random_pivot(arr):
        random.shuffle(arr)
        SortingBenchmark.quicksort(arr)

    @staticmethod
    def best(n):
        return list(range(n))

    @staticmethod
    def worst(n):
        return list(range(n, 0, -1))

    @staticmethod
    def average(n):
        return [random.randint(0, 1000) for _ in range(n)]
    
    @staticmethod
    def partition(array, start, end):
        pivot_value = array[end]
        partition_index = start - 1

        for current_index in range(start, end):
            if array[current_index] <= pivot_value:
                partition_index += 1
                array[partition_index], array[current_index] = array[current_index], array[partition_index]

        array[partition_index + 1], array[end] = array[end], array[partition_index + 1]
        return partition_index + 1

    @staticmethod
    def quicksort(array):
        stack = [(0, len(array) - 1)]

        while stack:
            start, end = stack.pop()

            if start < end:
                pivot_index = SortingBenchmark.partition(array, start, end)

                if pivot_index - start < end - pivot_index:
                    stack.extend([(start, pivot_index - 1), (pivot_index + 1, end)])
                else:
                    stack.extend([(pivot_index + 1, end), (start, pivot_index - 1)])

    @staticmethod
    def quickselect(array, k):
        """
        Finds the k-th smallest element in the array using the Quickselect algorithm.
        """
        if not 1 <= k <= len(array):
            raise ValueError("k is out of bounds")
        
        random.shuffle(array)
        left = 0
        right = len(array) - 1
        while left <= right:
            pivot_index = SortingBenchmark.partition(array, left, right)
            if pivot_index == k - 1:
                return array[pivot_index]
            elif pivot_index > k - 1:
                right = pivot_index - 1
            else:
                left = pivot_index + 1

    @staticmethod
    def benchmark(sort_func, input_generator, size, repetitions=3):
        total_time = 0
        for _ in range(repetitions):
            arr = input_generator(size)
            with SortingBenchmark.Timer() as timer:
                sort_func(arr)
            total_time += timer.elapsed_time
        avg_time = total_time / repetitions
        return avg_time

    def run(self):
        best_case_times = [self.benchmark(
            SortingBenchmark.quicksort, SortingBenchmark.best, size) for size in self.sizes]
        worst_case_times = [self.benchmark(
            SortingBenchmark.quicksort, SortingBenchmark.worst, size) for size in self.sizes]

        average_case_times = [self.benchmark(
            SortingBenchmark.quicksort, SortingBenchmark.average, size) for size in self.sizes]

        return best_case_times, worst_case_times, average_case_times

    class Timer:
        def __enter__(self):
            self.start_time = time.perf_counter()
            return self

        def __exit__(self, *args):
            self.end_time = time.perf_counter()
            self.elapsed_time = self.end_time - self.start_time
arr = [4,5,2,7,5,3,2,9,12,34,12,54,1322,4,23,122,134,1324,121321,1231314,10]
arr =[10,8,9,6,7,4,5,2,3,11,12,15,14,13,1]
print(arr)
ith = 5
print("The ith({0}th) largest number in arr is ".format(ith))
print(SortingBenchmark.quickselect(arr, ith))
