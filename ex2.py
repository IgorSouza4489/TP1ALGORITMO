class MinHeap:
    def __init__(self):
        self.heap = []

    def pai(self, i):
        return (i - 1) // 2

    def filho_esquerdo(self, i):
        return 2 * i + 1

    def filho_direito(self, i):
        return 2 * i + 2

    def inserir(self, chave):
        self.heap.append(chave)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.pai(i)] > self.heap[i]:
            self.heap[self.pai(i)], self.heap[i] = self.heap[i], self.heap[self.pai(i)]
            i = self.pai(i)

    def remover(self):
        if len(self.heap) == 0:
            return None
        raiz = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._ajustar(0)
        return raiz

    def _ajustar(self, i):
        esquerdo = self.filho_esquerdo(i)
        direito = self.filho_direito(i)
        menor = i

        if esquerdo < len(self.heap) and self.heap[esquerdo] < self.heap[menor]:
            menor = esquerdo
        if direito < len(self.heap) and self.heap[direito] < self.heap[menor]:
            menor = direito

        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self._ajustar(menor)

    def tamanho(self):
        return len(self.heap)

    def vazio(self):
        return len(self.heap) == 0

    def ver_topo(self):
        return self.heap[0] if self.heap else None