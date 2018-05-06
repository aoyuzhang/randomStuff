class ZeroCell:
    def __init__(self, l):
        self.name=l
        
class OneCell:
    def __init__(self, i,f,m,o):
        self.letter=m # We store one cell as a ordered tuple of zero cells. 
        self.initzeroCell= i
        self.finZeroCell= f
        self.orientation= o

class TwoCell:
    def __init__(self, l):
        self.list=l # We store a two cells as an ordered list of 2-tuple ( once-cell, orientation) 

class Complexes:
    def __init__(self,o,t,z):
        self.zeroCells=z
        self.oneCells=o
        self.twoCells=t


    x= OneCell('a')


def getVertices(Complex):
    ''' get the vertices on the Spine'''
    for x in complex.twoCells: # Go throught the two cells
        count=0 # count to label the vertices(create a number for the vertices)
        for y in x.list: # iterate throught the once cells in the two cells.
            count++;
            point=(count, y)
            pointsOnSpine.add(point) # add the vertices on the points on the spine
            return pointsOnSpine

def getEdges(Complex):
    edges=[]
    count=0;
    for x in complex.twoCells:
        for y in range 1 to list.amount():
            # create an edge
            edge=(x)
        
    
def check_stakcing(complex, list): # a list of tuples of (a,b,c)
    verticesOnSpine= getVertices(Complex)
    lobesDictionaries =[]
    for y in verticesOnSpine:
        .


    
    for g in complex.OneCell: # iterate throught the generators
        ginverse=oneCell(g.inizeroCell,g.finZeroCell,g.m,not g.o) # create inverse of the alphabet
        for y in verticesOnSpine: # iterate throught the oneCell
            if(y[1]==g or y[1]==ginverse):
                
            

            
            if (g==y):
                    
                    
