from cwComplexes import *
from getVertices import *
def getEdges(Complex):
    edges=[]
    count=0;
    lengthOfPrevious=0; # Total length of the previous two cells
    vertices= getVertices(Complex) # get the vertices first
    
    for x in Complex.twoCells:
        for y in range(0, len(x.list)):
            edge=(vertices[count], x.list[(count - lengthOfPrevious -1)%len(x.list)], vertices[(count+1)%len(x.list) + lengthOfPrevious])
            edges.append(edge)
            count+=1
        lengthOfPrevious+=len(x.list)
    return edges
