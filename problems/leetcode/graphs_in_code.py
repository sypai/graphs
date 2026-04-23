"""
Graph

0 --- 1
 \   /
   2

"""

edgesA = [[0,1],[1,2],[2,0]]

"""

0 --- 1    3 --- 5
|           \   /
|             4
2

"""

edgesB = [[0,1],[0,2],[3,5],[5,4],[4,3]]

"""Undirected (Bi directional)
  a -- c
  |    |
  b    e
  |
  d -- f
"""
edgesC = [['a', 'c'], ['a', 'b'], ['b', 'd'], ['d', 'f'], ['c', 'e']]

""" Directed Graph
  a --> c
  |    |
  b    e
  |
  d --> f
"""
edgesD = [['a', 'c'], ['a', 'b'], ['b', 'd'], ['d', 'f'], ['c', 'e']]

from collections import defaultdict

def build_adj_list(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # remove for directed
    return graph

def build_adj_list_directed(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return graph

