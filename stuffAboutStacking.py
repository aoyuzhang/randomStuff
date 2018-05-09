def perm(list):
	if len(list)==0:
  	return []
  elif len(list)==1:
  	return [list]
  else:
  	temp=[]
    for i in range(len(list)):
    	x=list[i]
      xs= lst[:i]+ list[i+1:]
      for p in perm(xs):
      	temp.append([x]+p)
      return temp
 
def getPermutationOfVerticesForPairOfEdges(pairOfEdges,permutation):
	temp=[]
	temp.append(pairOfEdges[0][0])
	temp.append(pairOfEdges[0][2])
	temp.append(pairOfEdges[1][0])
	temp.append(pairOfEdges[1][2])
  temp2=[]
  for x in permutation:
  	if x in temp:
    	temp2.append(x)
  return temp2  

def checkForIntersection(pairOfEdges, orderedListOfvertices):
	initialvP1=pairOfEdges[0][0]
  finalvP1=pairOfedges[0][2]
	initialvP2=pairOfEdges[1][0]
  finalvP2=pairOfedges[1][2]
  orderingOfvertices=getPermutationOfVerticesForPairOfEdges(pairOfEdges, orderedListOfvertices)
  ''' 
  check if the vertices are ordered in a dsjoint way
  '''
  temp1=[finalvP1,initialvP1] #vertices of the first edge
  temp2=[initialvP2,finalvP2] #vertices of the second edge
  ''' check for nested edges'''
  if orderingOfvertices[0] in temp1 and orderingOfvertices[1] in temp2 and orderingOfvertices[2] in temp2:
  	return True
  if orderingOfvertices[0] in temp2 and orderingOfvertices[1] in temp1 and orderingOfvertices[2] in temp1:
  	return True
    
    ''' check orientation '''
    if orderingOfvertices[0] in temp1 and orderingOfvertices[1] in temp[2] and orderingOfvertices[2] in temp1 and orderingOfvertices[3] in temp2:
    	if pairOfEdges[0][1][1] != pairOfEdges[1][1][1] and initalvP1 > finalvP1                         #talk about orientation but we also need to talk about ordering of vertices too
    
    
    if orderingOfvertices[0] in temp1 and orderingOfvertices[1] in temp[2] and orderingOfvertices[2] in temp1 and orderingOfvertices[3] in temp2:
    	
      
    
    #Heyyu maybe only check for cases where intersection = true then do else: false   ?? 
    
  

def checkStacking(compelx):
	vertices=getVertices(Complex)
  edges=getEdges(complex)
	edgesInLobe= getEdgesForLobe(complex)
  permutationOfVertices=list(itertools.permutations(vertices))
  for y in permutationOfVertices: # iterate throught the permutations of vertices
  	for x in edgesInLobe: # iterate throught the lobes
  		pairOfEges=list(itertools.combinations(edgesInlobe(x),2)) # get a list of pair of edges in the lobe
    	for m in pairOfEges: # iterate throught the pair of edges
      	m[0] m[1]
