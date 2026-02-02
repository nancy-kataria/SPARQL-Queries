import rdflib
import ssl
import certifi

# Configure SSL to use certifi's certificate bundle
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

g = rdflib.Graph()
g.parse("http://dbpedia.org/resource/Albert_Einstein")

# Query for name, birth date, and birth place
query1 = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?name ?birthDate ?birthPlace
WHERE {
    <http://dbpedia.org/resource/Albert_Einstein> rdfs:label ?name .
    <http://dbpedia.org/resource/Albert_Einstein> dbo:birthDate ?birthDate .
    <http://dbpedia.org/resource/Albert_Einstein> dbo:birthPlace ?birthPlace .
    FILTER (lang(?name) = "en")
}
"""

# Breakdown:
# •  PREFIX dbo/rdfs: Shortcuts for long URIs (like dbo:birthDate instead of http://dbpedia.org/ontology/birthDate)
# •  SELECT ?name ?birthDate ?birthPlace: Returns these three variables (? marks variables)
# •  WHERE block: Each line is a triple pattern (subject-predicate-object):
# ◦  Albert_Einstein rdfs:label ?name → Gets the name/label
# ◦  Albert_Einstein dbo:birthDate ?birthDate → Gets birth date
# ◦  Albert_Einstein dbo:birthPlace ?birthPlace → Gets birth place
# •  FILTER (lang(?name) = "en"): Only returns English labels (DBpedia has multilingual data)

print("Query 1: Basic Information")
print("=" * 50)
qres1 = g.query(query1)
for row in qres1:
    print(f"Name: {row.name}")
    print(f"Birth Date: {row.birthDate}")
    print(f"Birth Place: {row.birthPlace}")
    print()

# Query for description
query2 = """
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?name ?description
WHERE {
    <http://dbpedia.org/resource/Albert_Einstein> rdfs:label ?name .
    <http://dbpedia.org/resource/Albert_Einstein> dbo:description ?description .
    FILTER (lang(?name) = "en")
    FILTER (lang(?description) = "en")
}
"""

print("Query 2: Name and Description")
print("=" * 50)
qres2 = g.query(query2)
for row in qres2:
    print(f"Name: {row.name}")
    print(f"Description: {row.description}")
    print()

# Query for all types
query3 = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?name ?type
WHERE {
    <http://dbpedia.org/resource/Albert_Einstein> rdfs:label ?name .
    <http://dbpedia.org/resource/Albert_Einstein> rdf:type ?type .
    FILTER (lang(?name) = "en")
}
LIMIT 5
"""

print("Query 3: Name and Types (first 5)")
print("=" * 50)
qres3 = g.query(query3)
for row in qres3:
    print(f"Name: {row.name}")
    print(f"Type: {row.type}")
    print()
