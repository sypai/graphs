def connected_components(graph):
    visited = set()
    count = 0

    def explore(graph, current):
        if current in visited:
            return False
        
        visited.add(current)

        for neighbor in graph[current]:
              explore(graph, neighbor)
        return True
    
    for node, _ in graph.items():
        if explore(graph, node):
            count += 1
    
    return count

gr = {
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}

"""
    1 -- 2 -- 8 -- 9
              |
         6 -- 7
"""

connected_components(gr)