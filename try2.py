class Node(object):
    def __init__(self, char):
        self.letra = char
        self.filhos = []
        self.finalLetra = False

    def __str__(self):
        return self.letra

class Trie(object):

    def __init__(self):
        self.root = Node("*")

    def addPalavra(self, palavra ):

        nodeAtual = self.root #recebe a raix como node inical

        for le in palavra:
            foundLetra = False #essa variavel serve para saber se a letra atual foi encontrada em algum node

            for i in nodeAtual.filhos: #percorre todos nos da lista de filhos do node atual

                if le == i.letra: #se letra do momento for igual a letra do no atual
                    nodeAtual = i
                    foundLetra = True
                    break # sai do for interno para procurar a proxima letra

            if foundLetra == False: #se a letra nao existe
                newNode = Node(le) #cria um node com a letra
                nodeAtual.filhos.append(newNode) #add o node criado na lista de filhos do node atual
                nodeAtual = newNode # o node atual passa a ser o novo node, para constinuar escrevendo a palavra

        nodeAtual.finalLetra = True # marca a folha como fim da palavra

    def searcPalavra(self, palavra):

        nodeAtual = self.root

        for le in palavra:

            foundLetra = False # ex: "bola" e "bolas" sem essa variavel reotornria true para "bolas"

            for i in nodeAtual.filhos:
                foundLetra = False # ex: "bola" e "bolas" sem essa variavel reotornria true para "bolas"
                if le == i.letra:
                    nodeAtual = i
                    foundLetra = True
                    print(nodeAtual.letra,  end="  ")
                    break #

            if not foundLetra:
                return False

        return True if (foundLetra and nodeAtual.finalLetra) else False

    def delete(self, palavra):
        self._deleteHelper( self.root, palavra, 0, len(palavra))

    def _deleteHelper(self,pNode,key,level,length):
        '''
        Helper function for deleting key from trie
        '''
        if pNode:
            # Base case
            if level == length:
                # node is empty
                if pNode.finalLetra:
                    pNode.finalLetra = False

                return True if len(pNode.filhos) == 0 else False
            # recursive case
            else:
                index = 0

                for i, j in enumerate(pNode.filhos):
                    if key[level] == j.letra:
                        index = i

                # print(index, key[level])
                if self._deleteHelper(pNode.filhos[index], key,level+1,length):
                    print(pNode.filhos[index], "del")
                    del pNode.filhos[index]
                    # recursively climb up and delete
                    # eligible nodes
                    # return True if pNode.filhos >= 1 else False
                    if pNode.finalLetra == False and len(pNode.filhos) == 0:
                        return True
                    else:
                        return False
        return False

t = Trie()
#####################################
t.addPalavra("bola")
t.addPalavra("bolada")
t.addPalavra("bolinha")
t.addPalavra("bolinhazinha")
# print("bolinha", t.searcPalavra("bolinha"))
# print("bolinhazinha", t.searcPalavra("bolinhazinha"))

# print("bola", t.searcPalavra("bola"))
# print("bolada", t.searcPalavra("bolada"))
# print("bolinha", t.searcPalavra("bolinha"))
#################################
#
t.addPalavra("carro")
t.addPalavra("carroca")
t.addPalavra("carpete")
# print("carro", t.searcPalavra("carro"))
# print("carroca", t.searcPalavra("carroca"))/
# print("carpete", t.searcPalavra("carpete"))
############################

print("\n>>>>>>>>>>>>>>>>> DELETE >>>>>>>>>>>>>>>>>>>>\n")

t.delete('bolinha')
t.delete('carpete')

# t.delete('carro')

print("bola", t.searcPalavra("bola"))
print("bolada", t.searcPalavra("bolada"))
print("bolinha", t.searcPalavra("bolinha"))
print("bolinhazinha", t.searcPalavra("bolinhazinha"))

print("\n>>>>>>>>>>>>>>>>> C >>>>>>>>>>>>>>>>>>>>\n")

print("carro", t.searcPalavra("carro"))
print("carroca", t.searcPalavra("carroca"))
print("carpete", t.searcPalavra("carpete"))
