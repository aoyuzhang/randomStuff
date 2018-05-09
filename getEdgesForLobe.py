from getEdges import *
def getEdgesForLobe(Complex):
  edges=getEdges(Complex) # get the edges for the complex
  EdgesInLobes_dic={} # a dictionary to store a list of edges for each lobe
  for x in range(0, len(edges)): # Look throught the edges and add them in the dictionary appropriately
    if edges[x][1][0] in EdgesInLobes_dic: # if the dictionary already contains the lobe.
      EdgesInLobes_dic[edges[x][1][0]].append(edges[x])
    else:
      tempList=[] # create a temporary list to store the edges for a specific lobe
      tempList.append(edges[x]) # add the edge in the list 
      EdgesInLobes_dic[edges[x][1][0]] = tempList
  return EdgesInLobes_dic
