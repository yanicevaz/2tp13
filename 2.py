from ex1 import *

class BinaryTree:
    def __init__(self,root):
        self.__root = root

    def getRoot(self):
        return self.__root

    def isRoot(self,Node):
        if Node == self.__root:
            return True
        else:
            return False

    def size(self,Node):
        if Node is None:
            return 0
        else:
            return self.size(Node.getFilsGauche()) +1 + self.size(Node.getFilsDroit())

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())



arbre = BinaryTree(Node(12,None,None))
arbre.getRoot().setFilsGauche(Node(5,None,None))
arbre.getRoot().getFilsGauche().setFilsGauche(Node(4,None,None))
arbre.getRoot().getFilsGauche().setFilsDroit(Node(6,None,None))
arbre.getRoot().getFilsGauche().getFilsGauche().setFilsGauche(Node(3,None,None))

arbre.getRoot().setFilsDroit(Node(17,None,None))
arbre.getRoot().getFilsDroit().setFilsDroit(Node(19,None,None))
arbre.getRoot().getFilsDroit().getFilsDroit().setFilsGauche(Node(18,None,None))
arbre.getRoot().getFilsDroit().getFilsDroit().setFilsDroit(Node(21,None,None))

print(arbre.size(arbre.getRoot()))
