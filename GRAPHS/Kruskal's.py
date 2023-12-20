# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:04:50 2023

@author: haris
"""

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def kruskal(graph):
    edges = []
    for u in range(len(graph)):
        for v, weight in graph[u]:
            edges.append((u, v, weight))

    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    n = len(graph)
    ds = DisjointSet(n)
    minimum_spanning_tree = []

    for edge in edges:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            minimum_spanning_tree.append((u, v, weight))

    return minimum_spanning_tree


# Example usage:
# Example graph represented as an adjacency list with weights
# Replace this with your graph representation
graph = {
    0: [(1, 4), (2, 3)],
    1: [(2, 2), (3, 1)],
    2: [(3, 5)],
    3: []
}

minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:")
print(minimum_spanning_tree)
