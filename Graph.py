class Step2_Graph(object):
    def __init__(self, dictionary=None):
        if dictionary == None:
            dictionary = {}
        self.dictionary = dictionary

    def vertices(self):
        return list(self.dictionary.keys())

    def edges(self):
        edges = []
        for vertex in self.dictionary:
            for neighbour in self.dictionary[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def matrix(self):
        return [[1 if str(_) in self.dictionary[vertex] else 0 for _ in range(len(self.dictionary))] for vertex in self.dictionary.keys()]


index = ["Admin", "Cafetaria", "Storage", "Weapons", "Medbay",
         "O2", "Navigations", "Shield", "Communications", "Electrical",
         "Lower E.", "Security", "Reactor", "Upper E."]


# Hamiltonian path
class Step4_Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.V = vertices

    ''' Check if this vertex is an adjacent vertex  
            of the previously added vertex and is not  
            included in the path earlier '''

    def isSafe(self, v, pos, path):
        if self.graph[path[pos-1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamCycleUtil(self, path, pos):
        if pos == self.V:
            return True

        # Try different vertices as a next candidate
        # in Hamiltonian Cycle. We don't try for 0 as
        # we included 0 as starting point in hamCycle()
        for v in range(1, self.V):

            if self.isSafe(v, pos, path) == True:

                path[pos] = v

                if self.hamCycleUtil(path, pos+1) == True:
                    return True

                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V

        ''' Let us put vertex 0 as the first vertex  
            in the path. If there is a Hamiltonian Cycle,  
            then the path can be started from any point  
            of the cycle as the graph is undirected '''
        path[0] = 0

        if self.hamCycleUtil(path, 1) == False:
            print("Solution does not exist\n")
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print("Solution Exists: Following",
              "is one possible Hamiltonian path")
        for vertex in path:
            print(index[vertex], end=" ")


# Graph coloring principle modified to suits our necessities
# If a player has seen another player he cannot be an imposter => relation = 0
def Color_Graph(graph):
    return {
        vertex: {
            other_vertex: (
                0 if other_vertex == vertex or other_vertex in graph.dictionary[vertex] else 1
            )
            for other_vertex in graph.vertices()
        } for vertex in graph.vertices()
    }


# Finds a set of possible imposters from a given color graph and a first imposter
def possible_imposters(colorGraph, _):
    print(
        f"If the first imposter is PLAYER {_}, the other imposter is one of these players :")
    for __ in colorGraph[_]:
        if colorGraph[_][__] == 1:
            print(__, end=" ")
    print()
