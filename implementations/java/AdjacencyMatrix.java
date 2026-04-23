public class AdjacencyMatrix {
    private int[][] matrix;
    private int numVertices;

    public AdjacencyMatrix(int numVertices) {
        this.numVertices = numVertices;
        this.matrix = new int[numVertices][numVertices];
    }

    public void addEdge(int source, int destination, boolean bidirectional) {
        if (source >= 0 && source < numVertices && destination >= 0 && destination < numVertices) {
            matrix[source][destination] = 1;
            if (bidirectional) {
                matrix[destination][source] = 1;
            }
        }
    }
}
