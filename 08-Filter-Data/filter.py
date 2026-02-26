query1 = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?FName ?LName ?Age

WHERE {
	?person GOT:col-got-fname ?FName .
    ?person GOT:col-got-lname ?LName .
    ?person GOT:col-got-age ?Age .
	FILTER (?Age > 10)
}
"""

query2 = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?FName ?LName ?Age

WHERE {
	?person GOT:col-got-fname ?FName .
    ?person GOT:col-got-lname ?LName .
    ?person GOT:col-got-age ?Age .
	FILTER (?Age > 10)
}
ORDER BY DESC(?Age)
"""

query3 = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>
PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>

SELECT ?FName ?LName ?BirthDate

WHERE {
	?person GOT:col-got-fname ?FName .
    ?person GOT:col-got-lname ?LName .
    ?person GOT:col-got-birthdate ?BirthDate .
	FILTER (?BirthDate < "0280-01-01"^^xsd:date)
}
"""