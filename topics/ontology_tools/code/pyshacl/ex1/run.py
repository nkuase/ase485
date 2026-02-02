from pyshacl import validate
from rdflib import Graph

# 1. 데이터 + Shape 로드
data_graph = Graph()
data_graph.parse("food-safety-shacl.ttl", format="turtle")

# 2. SHACL 검증 실행
conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=data_graph,  # 같은 파일에 Shape 포함
    inference='rdfs',
    abort_on_first=False,
)

# 3. 결과 출력
print("=" * 50)
print("SHACL Validation Results")
print("=" * 50)
print(f"\nConforms: {conforms}")
print("\nValidation Report:")
print(results_text)