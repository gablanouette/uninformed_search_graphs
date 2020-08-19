# This project is a wonderful introduction project when learning Artificial Intelligence
# This project will visualize graphs 

# This purpose of this project is to:
#   - use Python to represent trees and graphs
#   - manipulate trees and graphs
#   - visualize trees and graphs
#   - use Python for uninformed graph search

# a graph is a collection of vertices, or nodes, and edges, which are connections between different 
# vertices (https://en.wikipedia.org/wiki/Graph_(discrete_mathematics). These graphs are visually
# represented with labels enclosed in a circle for the vertices, and lines connecting vertices
# which are the edges.

# a directed graph has edges that are arrows, meaning there is a connection from one vertex to 
# another, any other graph is an undirected graph.

# Python library to use when working with graphs: networkx

# import packages
import pandas as pd
import networkx as nx
import warnings
warnings.filterwarnings('ignore')

# create a graph from a dictionary of lists
graph_string_labels = {
  'A': ['B', 'D', 'F'],
  'B': ['A', 'C'],
  'C': ['B', 'E'],
  'D': ['A', 'C', 'E', 'F'],
  'E': ['C', 'D', 'F'],
  'F': ['A', 'D', 'E']
}

graph = nx.from_dict_of_lists(graph_string_labels)
print(type(graph))

nx.draw_networkx(graph, with_labels=True, node_color='cyan', node_size=500)

