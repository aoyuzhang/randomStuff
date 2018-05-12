#simple file to check everything works
from cwComplexes import *
from complexBuilder import *
from getEdges import *
from getVertices import *
from getEdgesForLobe import *

str = "a,b,c|a b c,b a c,b b c"
complex = prescomplex_builder(str)
#print(getVertices(complex))
print(getEdges(complex))
print(getEdgesForLobe(complex))
