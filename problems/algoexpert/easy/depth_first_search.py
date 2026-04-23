def dfs(graph, source):
    if len(graph) == 0:
        return []
     
    result = []
    visited = set()
    stack = [source]

    while stack:

        node = stack.pop()

        if node in visited:
            continue

        for neighbor in graph[node]:
            stack.append(neighbor)
        
        if not node in visited:
            result.append(node)
            visited.add(node)

    return result

dfs(graphB, 0)
