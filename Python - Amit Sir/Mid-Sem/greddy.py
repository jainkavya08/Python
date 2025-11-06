def greedy_search(graph,start,goal,heuristic) :
    queue = [start]
    visited = set()
    parent = {start: None}

    def get_heuristic(node):
        return heuristic[node]

    while queue:
        # sort by heuristic value
        queue.sort(key=get_heuristic)
        current = queue.pop(0)
        print(f"visiting:  {current}")

        if current == goal:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in queue:
                parent[neighbour] = current
                queue.append(neighbour)

    return none

# Example graph
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

# Heurisitc values
heurisitic = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 5, 'D': 3, 'E': 4,
    'F': 2, 'G': 0
}

path = greedy_search(graph,'S','G',heurisitic)
print("\n path found : ", path)
