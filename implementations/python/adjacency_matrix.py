class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # Initialize an empty VxV matrix with zeros
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, v1, v2, bidirectional=True):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.matrix[v1][v2] = 1
            if bidirectional:
                self.matrix[v2][v1] = 1

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))
