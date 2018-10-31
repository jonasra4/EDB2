class HeapTree:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def push(self,i):
        self.heapList.append(i)
        self.currentSize += 1
        self.promoverElemento(self.currentSize)

    def promoverElemento(self,i):
        # filho = i -- pai = i // 2
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]: #se o filho for maior que o pai
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2] # filho e papi trocam os valores
            i //= 2 #fiho vira pai para verificar se o seu pai eh
            i = i // 2

    def remove(self):
        self.currentSize -= 1
        self.heapList[0] = self.heapList[self.currentSize]
        self.rebaixarElemento(0)

    def rebaixarElemento(self,pai):

        filho = 2 * pai + 1

        while filho < self.currentSize:
            if filho < self.currentSize - 1:
                if self.heapList[filho] < self.heapList[filho+1]:
                    filho += 1
            if self.heapList[pai] >= self.heapList[filho]:
                break

            self.heapList[pai], self.heapList[filho] = self.heapList[filho], self.heapList[pai] # filho e papi trocam os

            pai = filho
            filho = 2 * pai + 1

    def printTree(self):
        for i in range(self.currentSize):
            print(self.heapList[i], end=" ")
        print()

tree = HeapTree()

tree.push(5)
tree.push(10)
tree.push(100)
tree.push(13)
tree.push(65)
tree.push(20)
tree.printTree()
tree.remove()
tree.printTree()

tree.remove()
tree.printTree()
tree.remove()
tree.printTree()
tree.remove()
tree.printTree()
