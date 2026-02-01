from rdflib import Graph, URIRef, Literal
from rdflib.namespace import FOAF

g = Graph()
bob = URIRef("http://example.org/people/Bob")

g.add((bob, FOAF.age, Literal(42)))
print(f"Bob is {g.value(bob, FOAF.age)}")
# prints: Bob is 42

# For some properties, only one value per resource makes sense (i.e they are functional properties, or have a max-cardinality of 1). The set() method is useful for this

g.set((bob, FOAF.age, Literal(43)))  # replaces 42 set above
print(f"Bob is now {g.value(bob, FOAF.age)}")
# prints: Bob is now 43