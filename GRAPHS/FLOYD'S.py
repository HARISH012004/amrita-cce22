# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:41:25 2023

@author: haris
"""

def floyd_warshall(graph):
    n = len(graph)
    # Initializing the distance matrix
    A = [[float('inf') for _ in range(n)] for _ in range(n)]

    # Base case: distances for directly connected vertices
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 0
            elif j in graph[i]:
                A[i][j] = graph[i][j]

    # Main algorithm
    for k in range(n):
        Ak_minus_1 = A.copy()  # Save the previous state of A before the k-th iteration
        for i in range(n):
            for j in range(n):
                A[i][j] = min(Ak_minus_1[i][j], Ak_minus_1[i][k] + Ak_minus_1[k][j])

    return A

# Example graph represented as an adjacency matrix with weights
# Replace this with your graph representation
graph = {
    0: {1: 3, 2: 6},
    1: {2: 2},
    2: {3: 1},
    3: {0: 1}
}

shortest_paths = floyd_warshall(graph)
print("Shortest Paths:")
for row in shortest_paths:
    print(row)
