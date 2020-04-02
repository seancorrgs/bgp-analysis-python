def matrixexists(s4arch, matrix):
    if s4arch in matrix[0]:
        return True


## Find the index of a location in the matrix
def matrixcityloc(s4arch, matrix):
    loc = matrix[0].index(s4arch)
    return loc ## Return the x/y of where that city is

def returnedgeweight(city1, city2, matrix):
    city1loc = matrixcityloc(city1, matrix); city2loc = matrixcityloc(city2, matrix)
    return matrix[city2loc][city1loc]
    # Need to search for the location of city 1 and city 2 first the    

def displaymatrix(matrix):
    for x in matrix:
        print(x)

def importdata():
    matrix = [["_______"]]
    with open("network.txt","r") as file:
        while True:
            line = file.readline()
            if line == "": break 
            elif line == "\n": continue
            line = line.replace("\n",("")); line = line.split(" ") ## Clean up the output and make list
            ## Now put data into our graph
            ## First search to make sure the city is in the matrix
            for i in range(2):
                ## Check to see if the City allready has a slot in the table
                if matrixexists(line[i], matrix) == True:
                    pass
                else: 
                    matrix[0].append(line[i]); matrix.append([line[i]])
            ## Add the distance that was provided
            city1 = matrixcityloc(line[0],matrix); city2 = matrixcityloc(line[1],matrix)    ## This will give us the locations in matrix[0] of the city
            
            ## Put the distance in the right chord on the matrix
            while True:
                try:
                    matrix[city2][city1] = line[2]
                    matrix[city1][city2] = line[2]
                    break
                except IndexError:
                    # If the Index doesn't exist add spacers to get it to right size
                    matrix[city2].append("------")
                    matrix[city1].append("------")
    return matrix


def debug(matrix):
     # Testing Area
    print("\nTESTING\n-------")
    displaymatrix(matrix)
    print("\nOttawa to Oshawa Dist.")
    print(returnedgeweight("Ottawa","Oshawa",matrix)) 
    # loc = matrixcityloc("", matrix)
    # print(loc)
    # print(matrix[loc][0], matrix[0][loc])
    input("")

def init():
    while True:
        print("\n" * 50)
        print("Choose a function\n\
            1. Build initial Graph\n\
            2. Change an Edge weight\n\
            3. Remove Edge\n\
            4. Find and Display all shortest paths\n\
            5. Minimum Spanning Tree\n\
            6. Quit\n\
            9. Debug")
        choice = input("choice:   ")
        if int(choice) == 1:
            importdata()
        elif int(choice) == 2:
            print(choice)
        elif int(choice) == 3:
            print(choice)
        elif int(choice) == 4:
            print(choice)
        elif int(choice) == 5:
            print(choice)
        elif int(choice) == 6:
            break
        elif int(choice) == 9:
            debug(matrix)
        
        matrix = importdata()
       

if __name__ == "__main__":
    init()