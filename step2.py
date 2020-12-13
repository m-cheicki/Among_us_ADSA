from Graph import Step2_Graph as Graph


def Color_Graph(graph):
    return {
        vertex: {
            other_vertex: (
                0 if other_vertex == vertex or other_vertex in graph.dictionary[vertex] else 1
            )
            for other_vertex in graph.vertices()
        } for vertex in graph.vertices()
    }


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


for _ in graph.matrix():
    print(_)

c_g = Color_Graph(graph)

_ = "1"
for __ in c_g[_]:
    if c_g[_][__] == 1:
        print(__, end=" ")
print()

_ = "4"
for __ in c_g[_]:
    if c_g[_][__] == 1:
        print(__, end=" ")
print()

_ = "5"
for __ in c_g[_]:
    if c_g[_][__] == 1:
        print(__, end=" ")
print()
