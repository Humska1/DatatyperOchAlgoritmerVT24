# -*- coding: utf-8 -*-
# Written by Vuk Dimovic <vudi0001@student.umu.se>
# Free to use, no license required  

import sys
from PrioQueueDirectedList import PrioQueueDirectedList
from DirectedGraph import DirectedGraph
from Edge import Edge



def equality_function(node1,node2):
    """
    Purpose: 
        Determines equality between two nodes.
    Parameters:
        node1: The first node.
        node2: The second node.
    Returns:
        True if the nodes are equal, False otherwise.
    """
    return node1 == node2

def read_file(filename):
    """
    Purpose:
        Reads data from a file and returns it as a tuple.
    Parameters:
        filename: Name of the file with data.
    Returns:
        nodes: A list of nodes extracted from the file.
        edges: A list of edges extracted from the file.
    """
    nodes = []
    edges = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line.isdigit() or not cleaned_line or cleaned_line.startswith('#'):
                    continue 

                parts = cleaned_line.split('#')[0].strip().split()
                if len(parts) < 2:
                    print(f"Warning: Line not in the specified format and will be ignored: {line.strip()}")
                    continue 

                node1, node2 = parts[:2]
                if node1 not in nodes:  
                    nodes.append(node1)
                if node2 not in nodes: 
                    nodes.append(node2)
                edges.append((node1, node2))  

        return nodes, edges

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return [], []


def construct_graph(nodes, edges):
    """
    Purpose:
        Constructs a directed graph from the given nodes and edges.
    Parameters:
        nodes: A list of nodes extracted from the file.
        edges: A list of edges extracted from the file.
    Returns:
        graph: The directed graph constructed from the file.
    """
    graph = DirectedGraph(eqFcn=equality_function)
    for node in nodes:
        graph.insertNode(node)  
    for node1, node2 in edges:
        graph.insertEdge(Edge(node1, node2))  

    return graph


def bfs(graph, start, goal):
    """ 
    Purpose: 
        Breadth-first search in a directed graph from a start node to a goal node.
    Parameters:
        graph: The directed graph to search.
        start: The starting node for the search.
        goal: The goal node to reach.
    Returns:
        True if there is a path from the start node to the goal node, False otherwise.
    """
    visited = []
    queue = PrioQueueDirectedList(equality_function)
    queue.insert(start)

    while not queue.isEmpty():
        current = queue.inspectFirst()
        queue.deleteFirst()

        if current == goal:
            return True

        if current not in visited:
            visited.append(current)
            for neighbor in graph.neighbours(current):
                if neighbor not in visited:
                    queue.insert(neighbor) 
    return False


def main():
    """
    Purpose: The main function of the program.
    """
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Error: No filename provided.")
        print("Usage: python isConnected.py <filename>")
        sys.exit(1)

    nodes, edges = read_file(filename)
    if not nodes or not edges:
        sys.exit(1)

    graph = construct_graph(nodes, edges)

    print("Enter origin and destination (quit to exit):")
    while True:
        line = input()
        if line == 'quit':
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
