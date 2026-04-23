package main

type GraphList struct {
	AdjacencyList map[int][]int
}

func NewGraphList() *GraphList {
	return &GraphList{
		AdjacencyList: make(map[int][]int),
	}
}

func (g *GraphList) AddVertex(vertex int) {
	if _, exists := g.AdjacencyList[vertex]; !exists {
		g.AdjacencyList[vertex] = []int{}
	}
}

func (g *GraphList) AddEdge(source, destination int, bidirectional bool) {
	g.AddVertex(source)
	g.AddVertex(destination)
	g.AdjacencyList[source] = append(g.AdjacencyList[source], destination)
	if bidirectional {
		g.AdjacencyList[destination] = append(g.AdjacencyList[destination], source)
	}
}
