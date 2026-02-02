import requests

endpoint = "http://mini23:7200/repositories/food"

query = """
PREFIX food: <http://www.semanticweb.org/smcho/ontologies/2026/0/food-ontology#>

SELECT ?person WHERE {
    ?person food:eats food:Apple .
}
"""

response = requests.get(
    endpoint,
    headers={"Accept": "application/sparql-results+json"},
    params={"query": query},
    timeout=30,
)

response.raise_for_status()

data = response.json()

for row in data["results"]["bindings"]:
    print(row["person"]["value"])