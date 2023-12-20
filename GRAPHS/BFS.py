# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:48:35 2023

@author: haris
"""

from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        # For an undirected graph, you might want to add both ways
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = {node: False for node in self.adj_list}
        queue = deque()

        queue.append(start)
        visited[start] = True

        while queue:
            current_node = queue.popleft()
            print(current_node)  # or do any operation you want with the node

            for neighbor in self.adj_list[current_node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS Traversal:")
g.bfs(0)  # Start BFS from node 0
