from rdflib import Graph

g = Graph()
g.parse("http://www.w3.org/People/Berners-Lee/card")
print(len(g))
# prints: 86

# this file/URI has 86 statements

# parse() can process local files, remote data via a URL, as in this example, or RDF data in a string (using the data parameter).