from rdflib import Graph

g = Graph()
g.parse("demo.nt")

print(len(g))

# “pretty-print” for python

import pprint
for stmt in g:
    pprint.pprint(stmt)

# It prints "drewp is a FOAF Person:"
# and "drep says “Hello World"
# stored in tripes

# The simplest format is ntriples, which is a triple-per-line format