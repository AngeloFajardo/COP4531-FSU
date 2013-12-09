# Angelo Fajardo
# COP4531
# Assignment 3

def main() :
    
    inputFile = open("input.txt")

    first_line = inputFile.readline()   
    if(first_line[0] == 'D'):           
        print ("Directed\n")            
    if(first_line[0] == 'U'):           
        print ("Undirected\n")          

    graph = {}
    node = {}
    
    for line in inputFile:           
        if line[0] != '#':
            node = line
            graph[node[0]] = node[2], node[4]
            print (graph)

if __name__ == '__main__':

    main()
