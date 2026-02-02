from rdflib import Graph
from pyshacl import validate

# 1. Data 
data_graph = Graph()
data_graph.parse("../ex2/data.ttl", format="turtle")

# 2. Shape graph load (separate file)
shapes_graph = Graph()
shapes_graph.parse("shapes.ttl", format="turtle")

# 3. SHACL 
conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shapes_graph,  # 다른 그래프 사용!
    inference='rdfs',
    abort_on_first=False,
)

# 4. Results 
print(f"Conforms: {conforms}")
print("\nValidation Report:")
print(results_text)