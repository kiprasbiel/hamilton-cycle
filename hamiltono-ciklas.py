import time
import numpy

print('Iveskite dimensijas X Y')

dimensions = input()
dimensions = dimensions.split()

class Graph():
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.V = vertices

    def isSafe(self, v, pos, path):
        # Tikrinama ar esama virsune yra salia paskutines
        if self.graph[path[pos - 1]][v] == 0:
            return False

        # Tikrinama ar virsune dar nera itraukta
        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamCycleUtil(self, path, pos):

        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.V):

            if self.isSafe(v, pos, path) == True:

                path[pos] = v

                if self.hamCycleUtil(path, pos + 1) == True:
                    return True

                # Pasalinama virsune jei ji netinka takui
                path[pos] = -1

        return False

    def hamCycle(self):
        path = [-1] * self.V
        path[0] = 0

        if self.hamCycleUtil(path, 1) == False:
            print("Ciklas neegzistuoja \n")
            return False

        self.printSolution(path)
        return True

    def printSolution(self, path):
        print("Ciklas egzistuoja: \n")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0], "\n")


g1 = Graph(int(dimensions[0]))
arr = numpy.load("matrica.npy")
print(arr)


g1.graph = arr

start_time = time.time()
# Sprendimo isspausdinimas
g1.hamCycle()

time1 = (time.time() - start_time)
print("Laikas: " + str(time1) + "s")
print("Spauskite enter noredami uzdaryti")
