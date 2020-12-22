from Graph import Step2_Graph as Graph
from Graph import Color_Graph, possible_imposters


graph = Graph({
    "0": ["1", "4", "5"],
    "1": ["0", "2", "6"],
    "2": ["1", "3", "7"],
    "3": ["2", "4", "8"],
    "4": ["0", "3", "9"],
    "5": ["0", "7", "8"],
    "6": ["1", "8", "9"],
    "7": ["2", "5", "9"],
    "8": ["3", "5", "6"],
    "9": ["4", "6", "7"]
})

# Adjacency matrix
print("ADJACENCY MATRIX : ")
for _ in graph.matrix():
    print(_)

print("-"*15)

colorGraph = Color_Graph(graph)

possible_imposters(colorGraph, "1")
possible_imposters(colorGraph, "4")
possible_imposters(colorGraph, "5")
