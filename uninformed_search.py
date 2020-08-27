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



# graphs using Data
# using a dataset from Facebook where the 'friends lists' are 'circles'
# node features == profiles, ego networks, circles
# certain features have been anonymized



facebook_dataset = '../facebook_combined.txt'
facebook = pd.read_csv(facebook_dataset, sep=' ', names=['A', 'B'])

print(facebook.info())
facebook.head()

# build networkx graph from a Pandas DataFrame
# the following graph object has been commented because it takes a while to run with this many edges and nodes
#G = nx.from_pandas_edgelist(facebook, 'A', 'B')
# nx.draw_networkx(G)


# building a dictionary of lists of strings that represents the graph
graph_1 = {
    'A': ['B', 'G', 'H'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F', 'G', 'H'],
    'E': ['C', 'D', 'F'],
    'F': ['E', 'D', 'G'],
    'G': ['D', 'F', 'H', 'A'],
    'H': ['A', 'D', 'G']
    }

### create a networkx graph using graph_1 and graph it
graph_2 = nx.from_dict_of_lists(ans_1)
nx.draw_networkx(graph_2, node_color='cyan')


# finding the number of edges and vertices in graph_1

graph_2_edges = nx.number_of_edges(graph_2)
graph_2_verts = nx.number_of_nodes(graph_2)
print('The graph ans_2 has {} vertices.'.format(graph_2_verts))
print('The graph ans_2 has {} edges.'.format(graph_2_edges))


# finding paths and connections:
# build a disconnected networkx Graph object

graph_3_dict = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': [],
    'E': ['F', 'G'],
    'F': ['E', 'G'],
    'G': ['E', 'F']
}

graph_3 = nx.from_dict_of_lists(graph_3_dict)

print('determine if graph_3 is a connected graph: {}.'.format(nx.is_connected(graph_3)))
print('The components of graph_3 are:')
for subgraph in nx.connected_components(graph_3):
    print('\t{}'.format(subgraph))


# graphs to represent airport connections


routes_path = '../air_routes.csv'
routes = pd.read_csv(routes_path, usecols=['source','dest','count'])

routes.head()


# build graph from the df routes using "nx.from_pandas_edgelist".
# each row == edge between the "source" and "dest" columns
routes_graph = nx.from_pandas_edgelist(routes, source = 'source', target = 'dest', edge_attr='count')


nx.draw_networkx(routes_graph)

print(routes_graph.number_of_edges())
print(routes_path.number_of_nodes())


list(nx.shortest_paths.all_shortest_paths(routes_graph, 'ALB', 'SFO'))
len(list(nx.shortest_paths.all_shortest_paths(ans_5, 'ALB', 'SFO')))

# finding all shortest paths between airports in ALB and SFO
# finding the length of any of the shortest paths from ALB to SFO
# finding the number of shortest paths from ALB to SFO
shortest_path_alb_sfo = list(nx.shortest_paths.all_shortest_paths(routes_graph, 'ALB', 'SFO'))
shortest_length_alb_sfo = len(shortest_path_alb_sfo[0])-1
shortest_number_paths = len(shortest_path_alb_sfo)

print('Length of any shortest path from ALB to SFO: {}'.format(shortest_length_alb_sfo))
print('Number of shortest paths from ALB to SFO: {}'.format(shortest_number_paths))
print('\nShortest paths from ALB to SFO:\n' + (31*'='))
for path in shortest_path_alb_sfo:
    print(path)



# building graph to represent a tree
tree_dict = {
    '4': ['2', '6'],
    '2': ['1', '3', '4'],
    '6': ['5', '7', '4'],
    '1': ['2'],
    '3': ['2'],
    '5': ['6'],
    '7': ['6']
}

tree_graph = nx.from_dict_of_lists(tree_dict)

print('Is ans_7 a tree: {}'.format(nx.is_tree(tree_graph)))
nx.draw_networkx(tree_dict, node_color='magenta')




# building a simple binary tree with the class Tree:
# edges are directed since they connect the parent nodes to their respective left and right children
# value is any data or object and does not need to be unique to the node
# the children (left and right) themselves can be trees
class Tree:
    """Simple Binary Tree"""
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        if self.left is None and self.right is None:
            return '%s (%s)' % (self.__class__.__name__, str(self.value))
        else:
            return '%s (%s, %s, %s)' % (self.__class__.__name__, self.value, self.left, self.right)
    def __repr__(self):
        if self.left is None and self.right is None:
            return '%s (%s)' % (self.__class__.__name__, repr(self.value))
        else:
            return '%s (%r, %r, %r)' % (self.__class__.__name__, self.value, self.left, self.right)



# use the class definition to determine the object of the tree:
print(9 * (2 + 3) + 7)


# encode 7 * (4 + 10) + 3 with the Tree class
first_tree = Tree('+', Tree('*', Tree(7), Tree('+', Tree(4), Tree(10))), Tree(3))
print(first_tree)


# encode 5 + ((3*2) - (7+10))
print(5 + ((3*2) - (7+10)))


# breaking up the parts:
Tree('+', Tree(3), Tree(2))
Tree('+', Tree(7), Tree(10))

# encoding second_tree with full solution using the Tree class:
second_tree = Tree('+', Tree(5), Tree('-', Tree('*', Tree(3), Tree(2)), Tree('+', Tree(7), Tree(10))))


# Tree Traversals: visiting each node only once
# function prints the tree value attribute of the node, then recursively traversing the left and right branches
# and prints their branches
def traversing_tree(tree):
    "Process Tree to print node values"
    if tree is None: return
    print(tree.value)
    traversing_tree(tree.left)
    traversing_tree(tree.right)


print('The original representation: {}\n\nThe "pre-order" traversal:'.format(first_tree))
traversing_tree(first_tree)


# function to return an in-order traversal of the tree
def traversing_tree_inorder(tree):
    "Traversing Tree using in-order traversal"
    if tree is None: return
    traversing_tree_inorder(tree.left)
    print(tree.value)
    traversing_tree_inorder(tree.right)

print('Print tree "7 * (4+10) + 3" inorder:')
print_tree_inorder(first_tree)


# finding paths in graphs
first_graph = {'A': ['B', 'D'],
         'B': ['A', 'C'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C'],
         'G': ['F']}

nx_graph = nx.from_dict_of_lists(first_graph)
nx.draw_networkx(nx_graph, with_labels=True, node_color='cyan', node_size=500, alpha=0.75)


# finding shortest paths from:
#    - C to G
#    - D to E
shortest_path_c_to_g = nx.shortest_path(nx_graph, 'C', 'G')
shortest_path_d_to_e = nx.shortest_path(nx_graph, 'D', 'E')
# To verify solutions:
print('A shortest path from node G to node G: {}'.format(shortest_path_c_to_g))
print('A shortest path from node D to node E: {}'.format(shortest_path_d_to_e))


# Uninformed Search Algorithms
# involves knowledge of both trees and graphs
# problem is to find a sequence of vertices connected by their edges from one vertex to another
# "uninformed" means that only available information is the lists of nodes next to other nodes so far\
# "informed" means there is more information available than just the adjacency


# DFS: Depth-First Search
# means of traversing through a graph or a tree. the search starts at a defined vertex (or root),
# chooses a vertex adjacent to the root, then proceeds down each branch before it starts to backtrack
# DFS wants to visit undiscovered vertices as soon as possible resulting in deep seearch trees


# function defining DFS
def depth_first(graph, initial):
    stack, explored = [initial], list()
    while stack:
        state = stack.pop()
        if state not in explored:
            explored.append(state)
            stack.extend([neighbor for neighbor in graph[state] if not ((neighbor in stack) or (neighbor in explored))])
    return explored


graph_dict = {'A': (['B', 'D']),
         'B': (['A', 'C']),
         'C': (['B', 'E']),
         'D': (['A', 'E']),
         'E': (['B'])}

print("A Depth-First Seach traversal starting at 'A': {}".format(depth_first(graph_dict, 'A')))
print("A Depth-First Search traversal starting at 'E': {}".format(depth_first(graph_dict, 'E')))


# use a generator function to find all possible paths between the initial vertex and terminal vertex
def dfs_path(graph, initial, goal):
    stack = [(initial, [initial])]
    while stack:
        (state, path) = stack.pop()
        for neighbor in [x for x in graph[state] if not (x in path)]:
            if neighbor == goal:
                yield path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))


paths = dfs_paths(graph_dict,'D', 'E')
print('type (paths): {}'.format(type(paths)))
paths = list(paths)
print("Paths from 'D' to 'E': {}".format(paths))



# BFS: Breadth-First Search
# search starts at root vertex, looks at all neighbors, then each of those neighbors, etc
# visits each vertex in order of its distance from the start (number of edges)
# vertices closer to first vertex are visited first
# BFS: first-in-first-out (FIFO) to maintain stack (stack == frontier)
# (preserve the order the nodes are visited)



def breadth_first(graph, initial):
    queue, explored = [initial], list()
    while queue:
        state = queue.pop(0)
        if state not in explored:
            explored.append(state)
            queue.extend([neighbor for neighbor in graph[state] if not ((neighbor in queue) or (neighbor in explored))])
    return explored



Here's an example of using the function `bfs` on the same toy graph from before.


graph_dict = {'A': (['B', 'D']),
         'B': (['A', 'C']),
         'C': (['B', 'E']),
         'D': (['A', 'E']),
         'E': (['B'])}

print("A BFS traversal starting from 'A': {}".format(dfs(graph_dict, 'A')))
print("A BFS traversal starting from 'E': {}".format(dfs(graph_dict, 'E')))



As with DFS, BFS can construct paths from the initial to the terminal node by tweaking the implementation of `bfs` to yield a
generator function `bfs_paths`. Notice that, with the breadth-first approach, BFS will identify shortest paths first
(in the sense of fewest edges; they may not be shortest in a geographical sense).

#%%
# use a generator function to find the shortest path (fewest edges) first
def bfs_paths(graph, initial, goal):
    queue = [(initial, [initial])]
    while queue:
        (state, path) = queue.pop(0)
        for neighbor in [x for x in graph[state] if not (x in path)]:
            if neighbor == goal:
                yield path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))


paths = bfs_paths(graph_dict,'A', 'E')
print('type (paths): {}'.format(type(paths)))
paths = list(paths)
print("BFS Paths from 'A' to 'E': {}".format(paths))



# Graph Search Algorithms in `networkx`
# networkx has implementations of DFS and BFS, as well as other algorithms


graph_dict = {'A': ['B', 'C', 'D'],
              'B': ['A', 'D'],
              'C': ['A', 'D'],
              'D': ['A', 'B', 'C', 'F'],
              'E': ['F'],
              'F': ['D', 'E', 'G'],
              'G': ['F']}

G = nx.from_dict_of_lists(graph_dict)

# find bfs
print(bfs(graph_dict, 'B'))

# compare result to networkx
edges = nx.bfs_edges(G, 'B')
nodes = ['B'] + [y for x, y in edges]
print(nodes)

list(nx.bfs_successors(G, 'B'))
