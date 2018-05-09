from getVertices import *
from getEdges import *
from getEdgesForLobe import *


class ZeroCell:
    def __init__(self, l):
        self.name=l
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()        
        
class OneCell:
    def __init__(self, i,f,m):
        self.letter=m # We store one cell as a ordered tuple of zero cells. 
        self.initZeroCell= i
        self.finZeroCell= f

    def __str__(self):
        return self.letter

    def __repr__(self):
        return self.__str__()        
 
class TwoCell:
    def __init__(self, l):
        self.list=l # We store a two cells as an ordered list of 2-tuple ( once-cell, orientation) 

    def __str__(self):
        s = ""
        for o in self.list:
            s += (o[0].__str__() + "' ") if o[1] else  (o[0].__str__() + " ") # adds apostrophe if inverse

        return s.strip()

    def __repr__(self):
        return self.__str__()        
 
class Complexes:
    def __init__(self,z,o,t):
        self.zeroCells=z
        self.oneCells=o
        self.twoCells=t
        self.edgeList=getEdges(self)
        self.vertexList=getVertices(self)
        self.lobeList = getEdgesForLobe(self)

    def __str__(self):
        s = ""

        for z in self.zeroCells:
            s += z.__str__()

        s += (",") if (s != "") else ""

        for o in self.oneCells:
            s += o.__str__()

        s += "|"

        for t in self.twoCells:
            s += t.__str__() + ","
        
        return s.strip(" ,")
 
    def __repr__(self):
        return self.__str__()        
