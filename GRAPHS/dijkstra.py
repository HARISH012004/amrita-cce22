# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:33:09 2023

@author: haris
"""

def prim_alternate(n, C):
    S = {1}  # Start with vertex 1
    D = [float('inf')] * (n + 1)  # Initialize distances
    for i in range(2, n + 1):
        D[i] = C[1][i]

    for i in range(1, n):
        # Find the vertex w not in S with the maximum distance initially
        min_distance = float('inf')
        w = -1
        for vertex in range(2, n + 1):
            if D[vertex] < min_distance and vertex not in S:
                min_distance = D[vertex]
                w = vertex
        
        # Add w to S
        S.add(w)

        # Update distances for vertices not in S
        for v in range(2, n + 1):
            if v not in S:
                D[v] = min(D[v], C[w][v])

    return S

# Example usage:
n = 4  # Number of vertices
# Cost matrix for edges (assuming 1-based indexing)
cost_matrix = [
    [0, 0, 0, 0, 0],  # Just to maintain 1-based indexing, unused
    [0, 0, 3, 2, 0],  # Edge costs from vertex 1
    [0, 3, 0, 0, 1],  # Edge costs from vertex 2
    [0, 2, 0, 0, 4],  # Edge costs from vertex 3
    [0, 0, 1, 4, 0]   # Edge costs from vertex 4
]

result = prim_alternate(n, cost_matrix)
print("Vertices in the Minimum Spanning Tree:", result)
