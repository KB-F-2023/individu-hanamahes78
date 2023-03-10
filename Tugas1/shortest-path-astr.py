import heapq
# Sourcecode https://www.youtube.com/watch?v=eSOJ3ARN5FM&list=PLTd6ceoshprfgFGcdiQw9LQ3fXaYC-Zs2&index=3

def a_star(graph, start, dest, heuristic):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    parent = {vertex: None for vertex in graph}
    visited = set()
    pq = [( 0 + heuristic[start], 0 ,  start)] 

    while pq: 
        curr_f, curr_dist, curr_vert = heapq.heappop(pq) 
        if curr_vert not in visited:
            visited.add(curr_vert)
            for nbor, weight in graph[curr_vert].items():
                distance = curr_dist + weight  
                f_distance = distance + heuristic[nbor] 
                if f_distance < distances[nbor]:
                    distances[nbor] = f_distance
                    parent[nbor] = curr_vert
                    if nbor == dest:
                        return distances, parent
                    heapq.heappush(pq, (f_distance, distance, nbor))
    return distances, parent

def generate_path_from_parents(parent, start, dest):
    path = []
    curr = dest
    while curr:
        path.append(curr)
        curr = parent[curr]
    return '->'.join(path[::-1])

graph = {
    'A': {'B':1, 'C':3, 'D':7},
    'B': {'D':5},
    'C': {'D':12},
    'D': {}
}

heuristic = {
    'A': 12,
    'B': 17,
    'C': 13,
    'D': 16
}

start = 'A'
dest= 'D'
distances,parent = a_star(graph, start, dest, heuristic)
print('jarak => ', distances)
print('parent => ', parent)
print('jarak terpendek => ', generate_path_from_parents(parent,start,dest))