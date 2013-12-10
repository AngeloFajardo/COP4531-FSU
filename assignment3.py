# Angelo Fajardo
# COP4531
# Assignment 3

from collections import namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')
 
class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))
 
    def dijkstra(self, source):
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, int(cost)))
            
        #pp(neighbours)
 
        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            print(dist)
            q.remove(u)
            if dist[u] == inf:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                                  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u

        for x in dist:
            print(x, dist[x])                   

def main() :
    
    inputFile = open("input.txt")

    first_line = inputFile.readline()   
    if(first_line[0] == 'D'):           
        print ("Directed\n")            
    if(first_line[0] == 'U'):           
        print ("Undirected\n")          

    graph = []
    nodeList = {}
    
    for line in inputFile:
        if line[0] != '#':
            nodeList = tuple(line.split())
            graph.append(nodeList)

    graphs = Graph(graph)
##    print(graphs.edges)
##    print(graphs.vertices)

    print(graphs.dijkstra('A'))


if __name__ == '__main__':

    main()
