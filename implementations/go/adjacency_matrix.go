package main

type GraphMatrix struct {
	Matrix      [][]int
	NumVertices int
}

func NewGraphMatrix(numVertices int) *GraphMatrix {
	matrix := make([][]int, numVertices)
	for i := range matrix {
		matrix[i] = make([]int, numVertices)
	}
	return &GraphMatrix{
		Matrix:      matrix,
		NumVertices: numVertices,
	}
}

func (g *GraphMatrix) AddEdge(source, destination int, bidirectional bool) {
	if source >= 0 && source < g.NumVertices && destination >= 0 && destination < g.NumVertices {
		g.Matrix[source][destination] = 1
		if bidirectional {
			g.Matrix[destination][source] = 1
		}
	}
}
