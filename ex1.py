class Node:
    def __init__(self,val,droit=None,gauche = None):
        self.__val = val
        self.__filsdroit = droit
        self.__filsgauche = gauche

    def getValeur(self):
        return self.__val

    def getFilsDroit(self):
        return self.__filsdroit

    def getFilsGauche(self):
        return self.__filsgauche

    def setNode(self,node):
        self.__val = node

    def setFilsDroit(self,node):
        self.__filsdroit = node

    def setFilsGauche(self,node):
        self.__filsgauche = node

    def __str__(self):
        return str(self.__val)
