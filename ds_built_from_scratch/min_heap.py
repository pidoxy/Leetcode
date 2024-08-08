class MinHeap:
    def __init__(self):
        # initialise an empty list to storer the elements of the heap
        self.heap = []

    def insert(self, value):
        # append new value to the end of heap
        self.heap.append(value)

        # 
        self._heapify_up(len(self.heap) - 1)

    def __str__(self):
        # returns string representation of heap|list
        return str(self.heap)

    def extract_min(self):
        # check if the heap is empty or not because an element cannot be extracted from an empty heap
        if not self.heap:
            return None
        
        # If the heap has one element remove it and return it
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # swap the root (min element) with the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        # restore the heap property by moving the new root down
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, index):
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # check if the left child exists and is smaller than the current element
        if left_child_index <  len(self.heap) and self.heap[left_child_index] < self.heap[smallest_index]:
            smallest = left_child_index

        # check if the right child exists and is smaller than the current element
        if right_child_index <  len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
            smallest = right_child_index

        # if the current element is not the smallest, swap the elements and heapify down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
    
    def _heapify_up(self, index):
        # find the parent index of the current element 
        parent_index = (index - 1) // 2
        

        # if the current element is smaller than its parent swap them
        if index > 0  and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

        # recursively heapify up the parent element
        self._heapify_up(parent_index)
        
    
    def get_min(self):
        # returns the root element (minimum) if the heap is not empty
        return self.heap[0]