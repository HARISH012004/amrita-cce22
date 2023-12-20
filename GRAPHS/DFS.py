# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:54:16 2023

@author: haris
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")  # Process current vertex

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_vertex):
        visited = [False] * (max(self.graph) + 1)
        self.dfs_util(start_vertex, visited)

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Search Traversal:")
g.dfs(2)  # Starting DFS traversal from vertex 2
