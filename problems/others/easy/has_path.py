"""

Write a function, hasPath, that takes in an object representing 
the adjacency list of 
a directed acyclic graph and two nodes (src, dst).

The function should return a boolean indicating whether or not there exists a 
directed path between the source and destination nodes.
"""

def hasPath(graph, src, dst):
    # Base Case: Found the destination
    if src == dst:
        return True
    
    # Recursive Step: Check all neighbors
    for neighbor in graph[src]:
        # "Check before you call" to reduce stack overhead
        if hasPath(graph, neighbor, dst):
            return True
            
    return False

from collections import deque

def hasPathIterative(graph, src, dst):
    if src == dst:
        return True
    
    q = deque([src])
    
    while q:
        node = q.popleft()
        if node == dst:
            return True
        for neighbor in graph[node]:
            q.append(neighbor)
 
    return False
    
# Example Usage
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print(hasPath(graph, 'a', 'f'))  # Output: True
print(hasPath(graph, 'a', 'g'))  # Output: False

