# Creating a graph
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []

}

# listing the visited
visited = []

# intializing the queue
queue = []

# Function for bfs traversal
def bfs (graph,visited,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver code
print("Following is the BFS path")
bfs(graph,visited,'5')