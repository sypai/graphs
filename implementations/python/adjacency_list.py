class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, bidirectional=True):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.adjacency_list[vertex1].append(vertex2)
        if bidirectional:
            self.adjacency_list[vertex2].append(vertex1)

    def __str__(self):
        return "\n".join([f"{v}: {neighbors}" for v, neighbors in self.adjacency_list.items()])
