import numpy as np
from StudyCaseUdemy.Graph import Graph

class OrderVector:
    def __init__(self, size):
        self.size = size
        self.last_pos = -1
        self.values = np.empty(self.size, dtype=object)

    def insert(self, vertex):
        if self.last_pos == self.size - 1:
            print('Capacidad max do Vector atingida')
            return
        pos = 0
        for i in range(self.last_pos+1):
            pos = i
            temp = self.values[i]
            if self.values[i].distance > vertex.distance:
                break
            if i == self.last_pos:
                pos = i + 1
        x = self.last_pos
        while x >= pos:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[pos] = vertex
        self.last_pos += 1

    def printer(self):
        if self.last_pos == -1:
            print('Empty Array')
        else:
            for i in range(self.last_pos+1):
                print(i, ' - ', self.values[i].label, ' - ', self.values[i].distance)


class Greedy:
    def __init__(self, objective):
        self.objective = objective
        self.found = False

    def search(self, current):
        print('------')
        print('Current Vertex: {}'.format(current.label))
        current.visited = True
        if current == self.objective:
            self.found = True

        else:
            orderVector = OrderVector(len(current.adjacents))
            for adj in current.adjacents:
                if not adj.vertex.visited:
                    adj.vertex.visited = True
                    orderVector.insert(adj.vertex)
            orderVector.printer()
            if orderVector.values[0] is not None:
                self.search(orderVector.values[0])



grafo = Graph()
# vector = OrderVector(5)
# vector.insert(grafo.arad)
# vector.insert(grafo.craiova)
# vector.insert(grafo.bucharest)
# vector.insert(grafo.dobreta)
# vector.insert(grafo.lugoj)


# vector.printer()
greedy = Greedy(grafo.bucharest)
greedy.search(grafo.arad)
