# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:00:22 2023

@author: haris
"""

import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        self.vertices[u].append((v, weight))
        self.vertices[v].append((u, weight))

    def prim_minimum_spanning_tree(self, start_vertex):
        min_spanning_tree = []
        included = set()
        priority_queue = []
        
        included.add(start_vertex)
        for neighbor, weight in self.vertices[start_vertex]:
            heapq.heappush(priority_queue, (weight, start_vertex, neighbor))

        while priority_queue:
            weight, u, v = heapq.heappop(priority_queue)
            if v not in included:
                included.add(v)
                min_spanning_tree.append((u, v, weight))
                for neighbor, w in self.vertices[v]:
                    if neighbor not in included:
                        heapq.heappush(priority_queue, (w, v, neighbor))

        return min_spanning_tree

# Example usage:
g = Graph()
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 1)
g.add_edge('C', 'D', 4)

minimum_spanning_tree = g.prim_minimum_spanning_tree('A')
print("Minimum Spanning Tree:")
print(minimum_spanning_tree)
