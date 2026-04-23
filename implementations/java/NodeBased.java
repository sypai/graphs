import java.util.ArrayList;
import java.util.List;

public class NodeBased {
    public String name;
    public List<NodeBased> neighbors;

    public NodeBased(String name) {
        this.name = name;
        this.neighbors = new ArrayList<>();
    }

    public NodeBased addNeighbor(NodeBased node) {
        this.neighbors.add(node);
        return this;
    }
}
