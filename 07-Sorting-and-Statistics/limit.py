query = """
PREFIX GOT: <https://tutorial.linked.data.world/d/sparqltutorial/>

SELECT ?ID ?FName ?LName

WHERE {
  ?person GOT:col-got-id ?ID .
  ?person GOT:col-got-fname ?FName .
  ?person GOT:col-got-lname ?LName .
}
LIMIT 5
"""