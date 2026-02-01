from rdflib import Dataset
from rdflib.namespace import RDF

g = Dataset()
g.parse("demo.trig")

for s, p, o, g in g.quads((None, RDF.type, None, None)):
    print(s, g)

# http://www.example.org/example#alice http://www.example.org/example#graph1
# http://www.example.org/example#bob http://www.example.org/example#graph2