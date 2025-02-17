import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        heapq.heappush(self.heap, key)

    def pop(self):
        if len(self.heap) == 0:
            return None 
        root = self.heap[0]
        last_element = self.heap.pop()     
        if len(self.heap) == 0:
            return root  

        self.heap[0] = last_element
        self._heapify(0)
        return root

    def _heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify(smallest) 
    def __str__(self):
        return str(self.heap)


min_heap = MinHeap()

min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(15)
min_heap.insert(30)
min_heap.insert(25)
min_heap.insert(40)

print("MinHeap após inserções:")
print(min_heap)

removed_element = min_heap.pop()
print(f"Elemento removido: {removed_element}")
print("MinHeap após remoção da raiz:")
print(min_heap)
