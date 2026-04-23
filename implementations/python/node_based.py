class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)
        return self

    def __str__(self):
        return f"{self.name} -> {[n.name for n in self.neighbors]}"
