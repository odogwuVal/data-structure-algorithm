from queue import Queue

if __name__ == '__main__':
    adj_list = {
        'A': ['B', 'D'],
        'B': ['C', 'A'],
        'C': ['B'],
        'D': ['A', 'E', 'F'],
        'E': ['D', 'F', 'G'],
        'F': ['D', 'E', 'H'],
        'G': ['E', 'H'],
        'H': ['F', 'G']
    }

    visited_node = {}
    level = {}
    parent = {}
    bfs_output = []

    queue = Queue()

    for node in adj_list.keys():
        visited_node[node] = False
        parent[node] = None
        level[node] = -1

    source_node = 'A'
    visited_node[source_node] = True
    level[source_node] = 0
    queue.put(source_node)

    while queue.qsize() != 0:
        # remove first element from the queue
        u = queue.get()
        # append this value to your output list
        bfs_output.append(u)

        for v in adj_list[u]:
            if not visited_node[v]:
                visited_node[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.put(v)
    print(bfs_output)

    # Shortest path to a node from source node
    v = 'G'

    path = []
    while v is not None:
        path.append(v)
        v = parent[v]
    path.reverse()
    print(path)

    # directional: DFS
    adj_list_two = {
        'A': ['B', 'C'], 
        'B': ['D', 'E'], 
        'C': ['B', 'F'], 
        'D': [],
        'E': ['F'],
        'F': [],
    }

    color = {}
    parent = {}
    trav_time = {} # [start, end]
    dfs_trav_output = []
    for node in adj_list_two.keys():
        color[node] = "W"
        parent[node] = None
        trav_time[node] = [-1, -1]
    

    time = 0
    def dfs_util(u):
        global time
        color[u] = "G"
        trav_time[u][0] = time
        dfs_trav_output.append(u)
        time += 1

        for v in adj_list_two[u]:
            if color[v] == "W":
                parent[v] = u
                dfs_util(v)
        color[u] = "B"
        trav_time[u][1] = time
        time += 1


    dfs_util("A")
    print(dfs_trav_output)
    print(parent)
    print(trav_time)