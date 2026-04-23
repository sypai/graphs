package main

type Node struct {
	Name      string
	Neighbors []*Node
}

func NewNode(name string) *Node {
	return &Node{
		Name:      name,
		Neighbors: []*Node{},
	}
}

func (n *Node) AddNeighbor(node *Node) *Node {
	n.Neighbors = append(n.Neighbors, node)
	return n
}
