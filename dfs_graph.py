# directional: DFS
adj_list_two = {
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['B', 'F'], 
    'D': [],
    'E': ['F'],
    'F': [],
}

color =  {}
# W(white) signifies that the vertex is not visited
# G(grey) visited but not completely
# B completely visited
parent = {}
trav_time = {} #[start, end]
dfs_trav_output = []

for vertex in adj_list_two.keys():
    color[vertex] = 'W'
    parent[vertex] = None
    trav_time[vertex] = [-1, 1]

time = 0
def DFS(u):
    global time
    color[u] = 'G'
    trav_time[u][0] = time
    time += 1

    dfs_trav_output.append(u)
    for v in adj_list_two[u]:
        if color[v] == 'W':
            parent[v] = u
            DFS(v)
    
    color[u] = 'B'
    trav_time[u][1] = time
    time += 1 

DFS('A')
print(dfs_trav_output)