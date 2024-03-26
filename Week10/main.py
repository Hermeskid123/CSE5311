import unittest
import time

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = HashMap()
        for i in range(10000):
            self.hashmap.put(i, i * 10)

    def tearDown(self):
        pass

    def test_put_performance(self):
        start_time = time.time()
        for i in range(10000, 20000):
            self.hashmap.put(i, i * 10)
        end_time = time.time()
        print("Time taken for put operation: {:.6f} seconds".format(end_time - start_time))

    def test_get_performance(self):
        start_time = time.time()
        for i in range(10000):
            self.assertEqual(self.hashmap.get(i), i * 10)
        end_time = time.time()
        print("Time taken for get operation: {:.6f} seconds".format(end_time - start_time))

    def test_remove_performance(self):
        start_time = time.time()
        for i in range(10000):
            self.hashmap.remove(i)
        end_time = time.time()
        print("Time taken for remove operation: {:.6f} seconds".format(end_time - start_time))



class Node:
    def __init__(self, key, value):
        self.next_node = None
        self.prev_node = None

        self.key = key
        self.value = value

class DoublyLinkedList:
    def __init__(self):
        self.tail = None

        self.head = None
    
    def remove(self, node):
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.head = node.next_node

        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.tail = node.prev_node

   
    def add(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

class HashMap:
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]
        self.threshold = int(self.capacity * 0.75)
        self.shrink_threshold = int(self.capacity * 0.25)

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        node = next((node for node in self.get_nodes(bucket) if node.key == key), None)
        return node.value if node else None

   
    
    def get_nodes(self, bucket):
        current_node = bucket.head
        while current_node:
            yield current_node
            current_node = current_node.next_node

    def print_table(self):
        for i, bucket in enumerate(self.buckets):
            print("Bucket ", i,": ")
            for node in self.get_nodes(bucket):
                print("    -> node key: ",node.key, " node value: " ,node.value, " ")
            print()
    def hash_function(self, key):
        return (key * 2654435761) % self.capacity

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        node = next((node for node in self.get_nodes(bucket) if node.key == key), None)
        if node:
            bucket.remove(node)
            self.size -= 1

            if self.size <= self.shrink_threshold:
                self.resize_table(max(self.capacity // 2, 1))


    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        existing_node = next((node for node in self.get_nodes(bucket) if node.key == key), None)
        if existing_node:
            existing_node.value = value
        else:
            bucket.add(key, value)
            self.size += 1

            if self.size >= self.threshold:
                self.resize_table(self.capacity * 2)


    def contains_key(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        ret = any(node.key == key for node in self.get_nodes(bucket))
        return ret

    def resize_table(self, new_capacity):
        new_buckets = [DoublyLinkedList() for _ in range(new_capacity)]

        for bucket in self.buckets:
            for node in self.get_nodes(bucket):
                new_index = self.hash_function(node.key)
                new_buckets[new_index].add(node.key, node.value)

        self.capacity = new_capacity
        self.buckets = new_buckets
        self.threshold = int(self.capacity * 0.75)
        self.shrink_threshold = int(self.capacity * 0.25)

if __name__ == "__main__":
    hashmap = HashMap()
    for i in range(1, 11):
        hashmap.put(i, i * 10)

    hashmap.print_table()

    print("Val for the key 3:", hashmap.get(3))

    hashmap.remove(3)

    print("key 3 val after removal:", hashmap.get(3))
    print("key 3 contains :", hashmap.contains_key(3))
    print("key 4 contains:", hashmap.contains_key(4))

    hashmap.print_table()
