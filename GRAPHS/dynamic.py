# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:57:42 2023

@author: haris
"""

class Graph:
    def __init__(self):
        self.vertices = {}  # Dictionary to store vertices and their links
        self.costs = {}  # Dictionary to store computed costs for vertices

    def add_vertex(self, vertex, links):
        self.vertices[vertex] = links

    def compute_costs(self, start_node):
        self.costs[start_node] = 0  # Set the starting node cost to 0
        queue = [start_node]  # Initialize a queue with the starting node

        while queue:
            current_node = queue.pop(0)  # Get the first node from the queue
            for neighbor in self.vertices[current_node]:
                if neighbor not in self.costs:  # Check if neighbor cost is not computed
                    if all(node in self.costs for node in self.vertices[neighbor]):
                        # If all linked nodes have costs computed, compute the cost for this node
                        self.costs[neighbor] = self.compute_cost(neighbor)
                        queue.append(neighbor)  # Add this node to the queue for further computation

    def compute_cost(self, node):
        # Replace this with your specific cost computation logic for a node
        return sum(self.costs[neighbor] for neighbor in self.vertices[node])

# Example usage:
g = Graph()
g.add_vertex('z', [])
g.add_vertex('i', ['z'])
g.add_vertex('j', ['i'])
g.add_vertex('k', ['i'])

g.compute_costs('z')  # Start computing costs from node 'z'

print("Computed Costs:")
print(g.costs)
