def largest_component(graph):
    visited = set()
    largest = 0

    def get_size(node):
        if node in visited:
            return 0
        
        visited.add(node)
        size = 1 # Count current node
        
        for neighbor in graph[node]:
            # Aggregate sizes of neighbors recursively
            size += get_size(neighbor) 
            
        return size
    
    for node in graph:
        if node not in visited:
            current_size = get_size(node)
            largest = max(largest, current_size)
            
    return largest