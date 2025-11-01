# Creating graphs
graph = {
    '5': ['3', '4'],
    '3': ['2', '1'],
    '4': ['8'],
    '2': [],
    '1': ['8'],
    '8': []
}

# List the visited
visited = []

# Intialize a queue
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver code
print("Following is the BFS ")
bfs(visited, graph, '5')