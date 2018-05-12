from cwComplexes import *
def getVertices(Complexes):
    ''' get the vertices on the Spine'''
    pointsOnSpine=[]
    countTwoCells=0
    count=-1 # count to label the vertices(create a number for the vertices)
    for x in Complexes.twoCells: # Go throught the two cells
        pointsInX=[]
        l = len(x.list)        

        for y in range(0,l):
            count+=1
            point={"count": count, "edgeIn": x.list[(y-1)%l], "edgeOut": x.list[y%l], "cell": x} 
            pointsInX.append(point) # add the vertices on the points on the spine
    
        for i in range(0,l):
            pointsInX[i]["vertexIn"] = pointsInX[(i-1)%l]
            pointsInX[i]["vertexOut"] = pointsInX[(i+1)%l]
            

        pointsOnSpine += pointsInX

    return pointsOnSpine
