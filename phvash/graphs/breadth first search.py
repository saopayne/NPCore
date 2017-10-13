""" 
BFS visits all the nodes of a graph (connected component)
following a breadthward motion. 

In other words, BFS starts from a node, 
then it checks all the nodes at distance one from the starting node,
then it checks all the nodes at distance two and so on. 

In order to remember the nodes to be visited, BFS uses a queue. 
The algorithm can keep track of the vertices
it has already checked to avoid revisiting them, 
in case a graph had one or more cycles.
"""

# graph implementation using an adjacency list
graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

# visit all the nodes of a graph (connected component)
def traverse(graph, start):
    # keep track of all visited nodes
    # this prevents an infinite loop in case of cyclic component
    visited = []
    
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are no nodes left unchecked
    while queue:
        # pop the shallowest (first node) from the queue
        node = queue.pop(0)
        if node not in visited:
            # add node to list of checked nodes
            visited.append(node)
            neighbours = graph[node]

            # add neigbours to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

print(traverse(graph, 'A'))