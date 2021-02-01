import random
import networkx
import matplotlib.pyplot as plt
from tkinter import *

class RIG:
    def __init__(self):
        self.colouring = None
        return

    def fromNMP(self, n, m, p):
        self.n = n
        self.m = m
        self.labelG = networkx.Graph()
        self.labelG.add_nodes_from([i for i in range(self.n + m)])
        for ni in range(self.n):
            for mi in range(m):
                if random.random() < p:
                    self.labelG.add_edge(ni, self.n + mi)
        self.fromLabel(self.n, self.labelG)


    def fromLabel(self, n, LabelGraph):
        self.RIG = networkx.Graph()
        self.RIG.add_nodes_from([i for i in range(self.n)])
        m = LabelGraph.number_of_nodes() - self.n
        for mi in range(m):
            neighbours = LabelGraph.neighbors(mi + n)
            neighbours = list(neighbours)
            for x in range(len(neighbours)):
                for y in range(1+x, len(neighbours)):
                    self.RIG.add_edge(neighbours[x], neighbours[y])


    def draw(self):
        if self.colouring == None:
            networkx.draw(graph.RIG, with_labels=True)
        else:
            networkx.draw(graph.RIG, node_color=self.colouring, with_labels=True)
        plt.show()

    #checks the colouring is proper returns 0 for bad colouring or the number of colours used
    def checkColour(self):
        if self.colouring == None:
            return 0
        if len(self.colouring) != self.n:
            return 0
        used = []
        for node in range(self.n):
            if self.colouring[node] not in used:
                used.append(self.colouring[node])
            neigh = self.RIG.neighbors(node)
            for neighbour in neigh:
                if self.colouring[node] == self.colouring[neighbour]:
                    return 0
        return len(used)
        
    def randomColour(self):
        self.colouring = []
        for node in self.RIG:
            self.colouring.append(random.randint(1,15))

    def CliqueColour(self):
        cOffset = 0
        self.colouring = [None for i in range(self.n)]
        lastU = [i for i in range(0, self.n)]
        while lastU != []:
            #step 1
            shade = [random.randint(0,self.n-1)+cOffset for i in range(self.n)]
            #step 2
            labelColours = [] #2d list of label colours
            for label in range(0, self.m):
                used = []
                Li = self.labelG.neighbors(self.n + label)
                for node in Li:
                    if node not in lastU:
                        continue
                    if shade[node] not in used:
                        used.append(shade[node])
                    else:
                        used.append(-1)
                labelColours.append(used)
            #steps 3-6
            u = []
            c = []
            for label in range(0, self.m):
                Li = self.labelG.neighbors(self.n + label)
                i = 0
                for node in Li:
                    if node not in lastU:
                        continue
                    if labelColours[label][i] != -1 and node not in c and node not in u: #get L\U+C
                        canColour = True
                        for coloured in c:#make sure there isnt a collision in L&C
                            if node in self.RIG[coloured] and self.colouring[coloured] == labelColours[label][i]:
                                canColour = False
                        if canColour:
                            self.colouring[node] = labelColours[label][i]
                            c.append(node)
                        else:
                            u.append(node)
                    i += 1

            cOffset += self.n #generate new set of colours
            lastU = u #update working graph

'''

root = Tk()
root.withdraw()
n = simpledialog.askinteger('', 'Input n')
m = simpledialog.askinteger('', 'Input m')
p = simpledialog.askfloat('', 'Input p')
root.quit()
graph = RIG()
graph.fromNMP(n, m, p)
graph.CliqueColour()
print(graph.checkColour())
graph.draw()
'''
