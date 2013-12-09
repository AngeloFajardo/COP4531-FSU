# Angelo Fajardo
# COP4531
# Assignment 3

def main() :
    
    inputFile = open("input.txt") 

    for i in inputFile:           
        if i[0] != '#':
            print (i)


if __name__ == '__main__':

    main()
