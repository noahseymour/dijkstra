import math

class Graph:
    def __init__(self, topology):
        self.topology = topology

        self.d = [math.inf for i in range(10)]
        self.s = list()
        self.Q = self.makeQ()
    
    def makeQ(self):
        lst = list()
        for count, d in enumerate(self.d):
            lst.append((d, count))
        if self.s:
            self.s.sort(reverse=True)
            for item in self.s:
                del lst[item]
        lst.sort()
        return lst

    def cost(self, u, v):
        vs = self.topology[u[1]]
        for e in vs:
            if e == v:
                return e[1]
    
    def relax(self, u, v):
        if self.d[v[0]] > self.d[u[1]] + self.cost(u, v):
            self.d[v[0]] = self.d[u[1]] + self.cost(u, v)
    
    def fspt(self, start) -> list: # find shortest path tree
        self.d[start] = 0
        while self.Q:
            u = self.Q[0]
            for v in self.topology[u[1]]:
                self.relax(u, v)
            self.s.append(u[1])
            self.Q = self.makeQ()
        return self.d

    def fsp(self, start, finish) -> int:
        return self.fspt(start)[finish]


topology = {  # graph implemented as a weighted adjacency list
    0: ((1, 2), (7, 5), (8, 1)),
    1: ((0, 2), (2, 2), (4, 4)),
    2: ((1, 2), (3, 1), (5, 8)),
    3: ((2, 1), (9, 1)),
    4: ((1, 4), (5, 15), (6, 9)),
    5: ((2, 8), (4, 15), (6, 3)),
    6: ((4, 9), (5, 3)),
    7: ((0, 5), (8, 3), (9, 4)),
    8: ((0, 1), (7, 5), (9, 1)),
    9: ((3, 1), (7, 4), (8, 1))
}

g = Graph(topology)
print(g.fsp(0, 3))