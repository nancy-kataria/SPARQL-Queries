# RDF data is a graph where the nodes are URI references, Blank Nodes or Literals. In RDFLib, these node types are 
# represented by the classes URIRef, BNode, and Literal. URIRefs and BNodes can both be thought of as resources, such
# a person, a company, a website, etc.

# A BNode is a node where the exact URI is not known - usually a node with identity only in relation to other nodes.
# A URIRef is a node where the exact URI is known. In addition to representing some subjects and predicates in RDF graphs, URIRefs are always used to represent properties/predicates
# Literals represent object values, such as a name, a date, a number, etc. The most common literal values are XML data types, e.g. string, int… but custom types can be declared too

from rdflib import URIRef, BNode, Literal, Namespace

bob = URIRef("http://example.org/people/Bob")
linda = BNode()  # a GUID is generated

name = Literal("Bob")  # passing a string
age = Literal(24)  # passing a python int
height = Literal(76.5)  # passing a python float

# For creating many URIRefs in the same namespace, i.e. URIs with the same prefix, RDFLib has the Namespace class

n = Namespace("http://example.org/people/")

n.bob  # == rdflib.term.URIRef("http://example.org/people/bob")
n.eve  # == rdflib.term.URIRef("http://example.org/people/eve")

# This is very useful for schemas where all properties and classes have the same URI prefix. RDFLib defines Namespaces 
# for some common RDF/OWL schemas, including most W3C ones:

from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD

RDF.type
# == rdflib.term.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")

FOAF.knows
# == rdflib.term.URIRef("http://xmlns.com/foaf/0.1/knows")

PROF.isProfileOf
# == rdflib.term.URIRef("http://www.w3.org/ns/dx/prof/isProfileOf")

SOSA.Sensor
# == rdflib.term.URIRef("http://www.w3.org/ns/sosa/Sensor")