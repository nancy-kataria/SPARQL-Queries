# https://docs.data.world/tutorials/sparql/

sparql_query = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?ID ?FName

WHERE {
?person GOT:col-got-id ?ID .
?person GOT:col-got-fname ?FName .
}
"""

# The first statement "?person GOT:col-got-id ?ID ." tells the SPARQL processor to look in the data and find a resource that has an ID property and store that value in ?ID. 
# In this case it will likely find the resource referring to Tyrion, because he is listed first in the data, but that is not always the case; the SPARQL processor may find the 
# data in any order. For now, let's say ?ID gets value "1".

# The SPARQL processor then binds that resource (Tyrion's row - GOT:row-got-0) to ?person for the remainder of the query's statements.

# The next statement "?person GOT:col-got-fname ?FName ." then tells the SPARQL processor to check whether the resource stored in ?person has a GOT:col-got-fname property, and, 
# if so, to store that value in ?FName. The first row does have an FName, so "Tyrion" gets stored in ?FName.

# Now that all the query statements have run, the SPARQL processor reiterates them for every resource in the data, storing all ID and FName values in the ?ID and ?FName variables. 
# It does this for all resources that contain data in both properties.

## query without a prefix

query = """
SELECT ?ID ?FName

WHERE
{
    ?person <https://tutorial.linked.data.world/d/sparqltutorial/col-got-id> ?ID .
    ?person <https://tutorial.linked.data.world/d/sparqltutorial/col-got-fname> ?FName .
}
"""

query2 = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?FName ?LName

WHERE {
    ?person GOT:col-got-fname ?FName .
    ?person GOT:col-got-lname ?LName .
}
"""

query3 = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?FName ?LName ?House ?Age

WHERE
{
    ?person GOT:col-got-fname "Daenerys" .
    ?person GOT:col-got-fname ?FName .
    ?person GOT:col-got-lname ?LName .
    ?person GOT:col-got-house ?House .
    ?person GOT:col-got-age ?Age .
}
"""

query4 = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?FName ?LName ?House ?Age

WHERE
{
    ?person GOT:col-got-age 34 .
    ?person GOT:col-got-fname ?FName .
    ?person GOT:col-got-lname ?LName .
    ?person GOT:col-got-house ?House .
    ?person GOT:col-got-age ?Age .
}
"""