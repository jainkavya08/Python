# creating a graph first
graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '2' : [],
    '4' : ['8'],
    '7' : ['8'],
    '8' : []
}

# Lisiting visited nodes
visited = []

# Intializing queue
queue = []

def bfs (visited,graph,node) :
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
print ("Following is the BFS Code : ")
bfs(visited,graph,'5')



