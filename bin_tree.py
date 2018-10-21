class Node:

    def __init__(self, valor):
        self.left = None
        self.right = None
        self.valor = valor

    def inserir(self, valor):

        if self.valor:
            if valor < self.valor:
                if self.left is None:
                    self.left = Node(valor)
                else:
                    self.left.inserir(valor)
            elif valor > self.valor:
                if self.right is None:
                    self.right = Node(valor)
                else:
                    self.right.inserir(valor)
        else:
            self.valor = valor

    def printTree(self):
        if self.left:
            self.left.printTree()
        print( self.valor, end=" "),
        if self.right:
            self.right.printTree()

    def inOrder(self, tree):
        result = []
        if tree:
            result = self.inOrder(tree.left)
            result.append(tree.valor)
            result += self.inOrder(tree.right)
        return result

    def preOrder(self, tree):
        result = []
        if tree:
            result.append(tree.valor)
            result += self.preOrder(tree.left)
            result += self.preOrder(tree.right)
        return result

    def posOrder(self, tree):
        result = []
        if tree:
            result = self.posOrder(tree.left)
            result += self.posOrder(tree.right)
            result.append(tree.valor)
        return result

    def buscaPreOrder(self, valor):
        node = None
        if self != None:
            if self.valor == valor:
                return self

            if self.left and node == None:
                node = self.left.buscaPreOrder(valor)     

            if self.right and node == None:
                node = self.right.buscaPreOrder(valor)
        
        return node

    def buscaPosOrder(self, valor):
        node = None
        if self != None:
            if self.left and node == None:
                node = self.left.buscaPosOrder(valor)

            if self.valor == valor:
                return self

            if self.right and node == None:
                node = self.right.buscaPosOrder(valor)

        return node

    def buscaInOrder(self, valor):
        node = None
        if self != None:
            if self.left and node == None:
                node = self.left.buscaInOrder(valor)

            if self.right and node == None:
                node = self.right.buscaInOrder(valor)

            if self.valor == valor:
                return self

        return node

    def remover(self, node):
        if node != None:
            node.valor = None
            node.right = None
            node.left = None
            node = None



tree = Node(1)
for i in range(15):
    tree.inserir(i)
    

print(">>> Tree: ", end="")
tree.printTree()


print("\n\n>>> In-order:",tree.inOrder(tree))
print(">>> Pre-order:",tree.preOrder(tree))
print(">>> Pos-order:",tree.posOrder(tree))

print("\n\n>>> Busca Pos-order:")
print(">", tree.buscaPosOrder(42))
print(">", tree.buscaPosOrder(10).valor)
print(">", tree.buscaPosOrder(7).valor)


print("\n\n>>> Busca In-order:")
print(">", tree.buscaInOrder(42))
print(">", tree.buscaInOrder(10).valor)
print(">", tree.buscaInOrder(7).valor)


print("\n\n>>> Busca Pre-order:")
print(">", tree.buscaPreOrder(42))
print(">", tree.buscaPreOrder(10).valor)
print(">", tree.buscaPreOrder(7).valor)
