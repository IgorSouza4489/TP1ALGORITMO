import heapq

#Utilizei biblioteca apenas para exemplificar a resposta dada na questão.
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        heapq.heappush(self.heap, -key)

    def remove(self):
        if len(self.heap) == 0:
            return None
        return -heapq.heappop(self.heap)

    def __str__(self):
        return str([-x for x in self.heap])


max_heap = MaxHeap()
max_heap.insert(50)
max_heap.insert(30)
max_heap.insert(40)
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(35)
max_heap.insert(45)

print("MaxHeap após inserções:")
print(max_heap)

removed_element = max_heap.remove()
print(f"Elemento removido: {removed_element}")
print("MaxHeap após remoção:")
print(max_heap)
