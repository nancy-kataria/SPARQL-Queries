query = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?FName ?LName

WHERE {
  ?person GOT:col-got-fname ?FName .
  ?person GOT:col-got-lname ?LName .
}
ORDER BY ?FName
"""