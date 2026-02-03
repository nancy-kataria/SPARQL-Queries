query = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?house (MAX(?age) as ?maxAge)

WHERE {
	?person GOT:col-got-house ?house ;
        	GOT:col-got-age ?age .
}
GROUP BY ?house
"""

query2 = """
#The average age of each house within our dataset.

PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?house (MAX(?age) as ?maxAge)

WHERE {
	?person GOT:col-got-house ?house ;
        	GOT:col-got-age ?age .
}
GROUP BY ?house
"""