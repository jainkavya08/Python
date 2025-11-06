# DFS
def dfs(graph,start,goal,stack,visited):
    stack.append(start)
    visited.append(start)
    print("Traversed path is: ")

    while stack:
        # pop the top element (LIFO)
        element = stack.pop()
        print(element, end = " ")

        # Stop if goal is found
        if element == goal :
            break

        for neighbour in graph[element]:
            if neighbour not in element:
                stack.append(neighbour)
                visited.append(neighbour)

# A dictionary representing a graph
graph = {
    'A': ['C', 'B'],
    'B': ['E', 'D'],
    'C': ['G', 'F'],
    'D': [],
    'E': ['I', 'H'],
    'F': [],
    'G': ['J'],
    'H': [],
    'I': [],
    'J': []
}

# Startin and goal nodes
start = 'A'
goal = 'J'

# List to track visited node and stack
visited = []
stack = []

dfs(graph, start,goal,stack,visited)