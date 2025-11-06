def a_star(graph, start, goal, heuristic):
    open_list = {start}
    closed_list = set()
    g = {start: 0}  # cost from start to node
    parents = {start: None}

    while open_list:
        n = min(open_list, key=lambda node: g[node] + heuristic[node])

        if n == goal:
            # reconstruct path
            path = []
            while n:
                path.append(n)
                n = parents[n]
            return path[::-1]

        open_list.remove(n)
        closed_list.add(n)

        for (neighbor, cost) in graph[n]:
            if neighbor in closed_list:
                continue
            tentative_g = g[n] + cost
            if neighbor not in open_list or tentative_g < g.get(neighbor, float('inf')):
                g[neighbor] = tentative_g
                parents[neighbor] = n
                open_list.add(neighbor)

    return None


# Graph represented as adjacency list with edge costs
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('G', 2)],
    'B': [('G', 1)],
    'G': []
}

# Heuristic values
heuristic = {
    'S': 4,
    'A': 2,
    'B': 1,
    'G': 0
}

path = a_star(graph, 'S', 'G', heuristic)
print("Path found:", path)
