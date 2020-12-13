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
