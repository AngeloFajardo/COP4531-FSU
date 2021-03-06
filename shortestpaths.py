# Angelo Fajardo
# COP4531
# Assignment 3

import itertools
from heapq import heapify, heappush, heappop

inf = float('inf')
readFile = open(input("Please input filename: "))

class PriorityQueue():
    def __init__(self):
        self.pq = []
        self.entry_finder = {}

    def addNode(self, node, priority=0):
        entry = [priority, node]
        self.entry_finder[node] = entry
        heappush(self.pq, entry)

    def popNode(self):
        priority, node = heappop(self.pq)
        return (node, priority)
            
    def printQueue(self):
        for i in self.pq:
            print (i[1], ':', i[0], '')

    def getPriority(self, value):
        if value in self.entry_finder:
            return self.entry_finder[value][0]

def main():

    setMode = True
    directed = ''

    G = []
        
    for line in readFile:
        if line[0] != '#':
            if setMode:
                if line[0] == "D":
                    print ('Directed')
                    directed = True
                elif line[0] == "UD":
                    print ('Undirected')
                    directed = False
                setMode = False
            else:
                if directed == True:
                    temp = line.split()
                    G.append((temp[0], temp[1], int(temp[2])))
                else:
                    temp = line.split()
                    G.append((temp[0], temp[1], int(temp[2])))
                    G.append((temp[1], temp[0], int(temp[2])))

                    
    vertices = set()

    for i in G:
        vertices.add(i[0])
        vertices.add(i[1])

    loop = True
    source = ''
    
    while loop:
        if source not in vertices:
            source = input('Enter Start Node: ')[0]
        else:
            loop = False

    edges = {vertex: set() for vertex in vertices} 

    for start, end, cost in G:
        edges[start].add((end, cost))

    Q = PriorityQueue()

    for i in vertices:
        if i == source:
            Q.addNode(i, 0)
        else:
            Q.addNode(i, inf)

    uq = Q.popNode() 
        
    while(True):
        if uq[1] == inf: break
        uVal, uPrio = uq 

        for adjV in edges[uVal]: 
            if uPrio + adjV[1] < Q.getPriority(adjV[0]):
                newPrio = uPrio + adjV[1]
                Q.addNode(adjV[0], newPrio)

        
        uq = Q.popNode() 

    writer = open('out.txt', 'w')
    writer.write('Dijkstra\n')
    for i in Q.entry_finder:
        writer.write('NODE ')
        writer.write(i)
        writer.write(' : ')
        writer.write(str(Q.entry_finder[i][0]))
        writer.write('\n')
    writer.write('End Dijkstra')

    
if __name__ == '__main__':
    main()












        


