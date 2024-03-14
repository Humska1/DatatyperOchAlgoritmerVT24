import sys
from DirectedGraph import DirectedGraph
from Edge import Edge

def equality_check(node1, node2):
    return node1 == node2

def read_graph_from_file(filename):
    graph = DirectedGraph(eqFcn=equality_check)
    expected_edges = None
    actual_edges = 0

    with open(filename, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line or cleaned_line.startswith('#'):
                continue  # Skip blank lines and comments

            if expected_edges is None:  # The first valid line should be the number of edges
                expected_edges = int(cleaned_line)
                continue

            parts = cleaned_line.split('#')[0].strip().split()  # Remove inline comments
            if len(parts) < 2:
                print(f"Warning: Skipping malformed line: {cleaned_line}")
                continue

            node1, node2 = parts[:2]
            graph.insertEdge(Edge(node1, node2))
            actual_edges += 1

    if expected_edges is not None and expected_edges != actual_edges:
        print(f"Warning: Expected {expected_edges} edges, but found {actual_edges}.")

    return graph

def bfs(graph, start, goal):
    visited = set()  # To keep track of visited nodes to avoid revisiting
    queue = [start]  # Queue for BFS traversal, initialized with the start node

    while queue:
        current = queue.pop(0)  # Dequeue the next node to explore
        if current == goal:
            return True  # Goal node found, path exists
        if current not in visited:
            visited.add(current)  # Mark the current node as visited
            neighbors = graph.neighbours(current)  # Retrieve neighbors of the current node
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)  # Enqueue unvisited neighbors
    return False  # Goal node not found, no path exists


def main():
    if len(sys.argv) != 2:
        print("Usage: python isConnected.py <graph file>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        graph = read_graph_from_file(filename)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)

    print("Enter origin and destination (quit to exit):")
    while True:
        line = input()
        if line.lower() == 'quit':
            break
        try:
            start, end = line.split()
            if bfs(graph, start, end):
                print(f"{start} and {end} are connected")
            else:
                print(f"{start} and {end} are not connected")
        except ValueError:
            print("Invalid input. Please enter two node names separated by a space.")

if __name__ == "__main__":
    main()
