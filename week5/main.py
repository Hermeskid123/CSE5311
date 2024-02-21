class min_heap:
    __slots__ = ['heap']
    def __init__(self):
        self.heap = []
    @staticmethod
    def left(i):
        return (i << 1) + 1
    @staticmethod
    def right(i):
        return (i << 1) + 2
    @staticmethod
    def parent(i):
        return (i - 1) >> 1

    def heapify(self, index, direction):
        target = index
        child_index = direction(index)

        if child_index < len(self.heap) and self.heap[child_index] < self.heap[target]:
            target = child_index

        child_index = direction(target)

        if child_index < len(self.heap) and self.heap[child_index] < self.heap[target]:
            target = child_index

        if target != index:
            self.heap[index], self.heap[target] = self.heap[target], self.heap[index]
            self.heapify(target, direction)

    def build_min_heap(self, arr):
        self.heap = arr
        lenght = len(arr)

        for i in range(lenght // 2, 0, -1):
            self.heapify(i - 1, self.left)
        
    def insert(self, num):
        self.heap.append(num)
        current_index = len(self.heap) - 1

        while current_index > 0:
            parent_index = self.parent(current_index)

            if self.heap[current_index] < self.heap[parent_index]:
                self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index]
                current_index = parent_index
            else:
                break




    def pop_root(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0, self.left)
        return root

heap = min_heap()
heap.build_min_heap([4, 1, 3, 2, 5, 1, 6, 6, 9,10,9.4,12,8.3])
print("min heap:", heap.heap)
heap.insert(0.1)
print("after insert", heap.heap)
popped = heap.pop_root()
print("poped root:", popped)
print("Heap now", heap.heap)