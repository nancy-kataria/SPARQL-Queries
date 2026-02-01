import ssl
from rdflib import Graph

# Bypass SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

g = Graph()
g.parse("http://www.w3.org/People/Berners-Lee/card")
g.serialize(destination="tbl.ttl")
