query1 =  """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT (MIN(?FName) AS ?firstName)
  # Stores the minimum value bound to the ?FName variable in the ?firstName variable - only displays this value

WHERE {
  ?person GOT:col-got-fname ?FName .
}
"""

query2 = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT (AVG(?age) AS ?avgAge)
  # Stores the average of values bound to the ?age variablae in the ?avgAge variable - only displays this value

WHERE {
  ?person GOT:col-got-age ?age .
}
"""

query3 ="""
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT (SUM(?age) AS ?totalYears)
  # Stores the total of values bound to the ?age variable in the ?avgAge variable - only displays this value

WHERE {
  ?person GOT:col-got-age ?age .
}
"""

query4 = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT (MAX(?age) as ?highage)

WHERE{
    ?person GOT:col-got-age ?age
}
"""