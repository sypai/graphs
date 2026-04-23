import java.util.*;

public class AdjacencyList {
    private Map<Integer, List<Integer>> adjList;

    public AdjacencyList() {
        this.adjList = new HashMap<>();
    }

    public void addVertex(int vertex) {
        adjList.putIfAbsent(vertex, new ArrayList<>());
    }

    public void addEdge(int source, int destination, boolean bidirectional) {
        addVertex(source);
        addVertex(destination);
        adjList.get(source).add(destination);
        if (bidirectional) {
            adjList.get(destination).add(source);
        }
    }
}
