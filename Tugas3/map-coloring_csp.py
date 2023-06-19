from typing import Dict, List

def constraints(regions: str, color: str, assignment: Dict[str, str], 
                graph: Dict[str, List[str]]) -> bool:
    for borders in graph[regions]:
        if borders in assignment and assignment[borders] == color:
            return False
    return True

def check_border(assignment: Dict[str, str], graph: Dict[str, List[str]],
              domain: Dict[str, List[str]]) -> Dict[str, str]:
    if len(assignment) == len(graph):
        return assignment
    regions = None
    for n in graph:
        if n not in assignment:
            regions = n
            break
    for value in domain[regions]:
        if constraints(regions, value, assignment, graph):
            assignment[regions] = value
            result = check_border(assignment, graph, domain)
            if result is not None:
                return result
            del assignment[regions]
    return None

def map_coloring(graph: Dict[str, List[str]], colors: List[str]) -> Dict[str, str]:
    domain = {regions: colors for regions in graph}
    return check_border({}, graph, domain)

graph = {
    'RAJ': ['GUJ', 'MP', 'UP'],
    'UP': ['RAJ', 'MP'],
    'MP': ['RAJ', 'UP', 'GUJ', 'MAH', 'CHG'],
    'GUJ': ['RAJ', 'MP', 'MAH'],
    'MAH': ['GUJ', 'MP', 'CHG'],
    'CHG': ['MP', 'MAH']
}

colors = ['red', 'green', 'blue']
solution = map_coloring(graph, colors)
print(solution)