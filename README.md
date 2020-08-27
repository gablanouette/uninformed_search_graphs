# Artificial Intelligence: Uninformed Search Graphs


This project is an introduction to uninformed search graphs in Artificial Intelligence and will visualize graphs.

This purpose of this project is to:
  - use Python to represent trees and graphs
  - manipulate trees and graphs
  - visualize trees and graphs
  - use Python for uninformed graph search

A graph is a collection of vertices, or nodes, and edges, which are connections between different vertices (https://en.wikipedia.org/wiki/Graph_(discrete_mathematics). These graphs are visually represented with labels enclosed in a circle for the vertices, and lines connecting vertices which are the edges.

A directed graph has edges that are arrows, meaning there is a connection from one vertex to another, any other graph is an undirected graph.

# Uninformed Search Algorithms:
involves knowledge of both trees and graphs problem is to find a sequence of vertices connected by their edges from one vertex to another. "uninformed" means that only available information is the lists of nodes next to other nodes so far, "informed" means there is more information available. than just the adjacency

# DFS: Depth-First Search
Means of traversing through a graph or a tree. the search starts at a defined vertex (or root), chooses a vertex adjacent to the root, then proceeds down each branch before it starts to backtrack. DFS wants to visit undiscovered vertices as soon as possible resulting in deep seearch trees

# BFS: Breadth-First Search
search starts at root vertex, looks at all neighbors, then each of those neighbors, etc. visits each vertex in order of its distance from the start (number of edges). vertices closer to first vertex are visited first. first-in-first-out (FIFO) to maintain stack (stack == frontier). preserves the order the nodes are visited.
