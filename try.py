class Node(object):
    def __init__(self, char):
        self.letra = char
        self.filhos = []
        self.finaLetra = False

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

        nodeAtual.finaLetra = True # marca a folha como fim da palavra

    def searcPalavra(self, palavra):

        nodeAtual = self.root
        # foundLetra = True

        for le in palavra:

            for i in nodeAtual.filhos:
                if le == i.letra:
                    print(i)
                    nodeAtual = i
                    break #proxima letra
                else:
                    # foundLetra = False
                    # break
                    return False

        # return True if foundLetra else False
        return True


t = Trie()
t.addPalavra("bota")
t.addPalavra("botata")
t.addPalavra("bota")
t.addPalavra("bola")

print(t.searcPalavra("botas"))
print(t.searcPalavra("bot"))
print(t.searcPalavra("calo"))
print(t.searcPalavra("bota"))
print(t.searcPalavra("bolas"))
