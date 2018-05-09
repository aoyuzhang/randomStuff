from cwComplexes import *
def getVertices(Complexes):
    ''' get the vertices on the Spine'''
    pointsOnSpine=[]
    countTwoCells=0
    count=0 # count to label the vertices(create a number for the vertices)
    for x in Complexes.twoCells: # Go throught the two cells
        countTwoCells+=1
        for y in range(0,len(x.list)):
            count+=1
            '''Points are stored as (number, edge that goes in, edge that goes out, which 2-cell it beongs)'''
            point=(count, x.list[(y-1)%len(x.list)],x.list[y%len(x.list)],countTwoCells) 
            pointsOnSpine.append(point) # add the vertices on the points on the spine
    return pointsOnSpine
