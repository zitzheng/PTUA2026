# adjacency.py

from pathlib import Path


# Node
class Node:
    def __init__(self, node_id: int):
        self.id = node_id
        self.neighbors: list[int] = []

    def degree(self) -> int:
        return len(self.neighbors)


# Graph
class Graph:
    def __init__(self):
        self.nodes: dict[int, Node] = {}

    def load_from_gal(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        i = 1  # skip header

        while i < len(lines):
            parts = lines[i].split()
            node_id = int(parts[0])

            neighbors = list(map(int, lines[i + 1].split()))

            node = Node(node_id)
            node.neighbors = neighbors
            self.nodes[node_id] = node

            i += 2

    def average_connectivity(self) -> float:
        total = sum(node.degree() for node in self.nodes.values())
        return total / len(self.nodes)

    def max_connectivity(self):
        max_deg = max(node.degree() for node in self.nodes.values())
        max_nodes = [node for node in self.nodes.values() if node.degree() == max_deg]
        return max_deg, max_nodes

    def min_connectivity(self):
        nonzero_nodes = [node for node in self.nodes.values() if node.degree() > 0]
        min_deg = min(node.degree() for node in nonzero_nodes)
        min_nodes = [node for node in nonzero_nodes if node.degree() == min_deg]
        return min_deg, min_nodes

    def disconnected_nodes(self):
        return [node for node in self.nodes.values() if node.degree() == 0]


if __name__ == "__main__":
    gal_file = Path(__file__).with_name("Lab07-1.gal")

    g = Graph()
    g.load_from_gal(str(gal_file))

    print("Average connectivity:", g.average_connectivity())

    max_deg, max_nodes = g.max_connectivity()
    print("Max connectivity:", max_deg, "Nodes:", [n.id for n in max_nodes])

    min_deg, min_nodes = g.min_connectivity()
    print("Min connectivity:", min_deg, "Nodes:", [n.id for n in min_nodes])

    disconnected = g.disconnected_nodes()
    if disconnected:
        print("Disconnected nodes:", [n.id for n in disconnected])
    else:
        print("No disconnected nodes")