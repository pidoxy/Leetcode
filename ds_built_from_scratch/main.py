from min_heap import MinHeap
from max_heap import MaxHeap

def main():
    # Test MinHeap
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(30)
    min_heap.insert(2)
    print("MinHeap: ", min_heap.get_min())
    min_heap.extract_min()
    print("MnHeap fter extract_min:", min_heap)

    # Test MaxHeap
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(5)
    max_heap.insert(30)
    max_heap.insert(2)
    print("MaxHeap: ", max_heap.get_max())
    max_heap.extract_max()
    print("MnHeap fter extract_max:", max_heap)

    if __name__ == "__main__":
        main()