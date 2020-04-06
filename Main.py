##########################
# Sean Corrigan 2020
# 100693058
# https://gitlab.platinumnetworks.ca/imp4ct
##########################

def matrixexists(s4arch, matrix): ## Check if the city exists in the matrix
    if s4arch in matrix[0]:
        return True

def matrixcityloc(s4arch, matrix): ## Find the index of a location in the matrix
    loc = matrix[0].index(s4arch)
    return loc # Return the x/y of where that city is

def returnedgeweight(city1, city2, matrix): ## Return the edge weight of 2 cities
    city1loc = matrixcityloc(city1, matrix); city2loc = matrixcityloc(city2, matrix)
    weight =  matrix[city2loc][city1loc]
    try:
        weight = int(weight)
    except: return False
    return weight

def displaymatrix(matrix): ## Print the matrix nicely for the debug screen
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

def listcities(matrix): ## Return a list of the cities in the array
    citylist = []
    for i in range(len(matrix[0])):
        if i == 0: continue # Dont Index Placeholder
        citylist.append(matrix[0][i])
    return citylist

def chooseandreturn(): ## condense the return cities repetitive code.
    global matrix
    ## Choose a city to view the edges on it
    availpaths = returnpaths(availcities[choicecity1], matrix) # Get all paths for the chosen city
    print("-- Current Paths --\n\n"); counter = 0; # , start counter
    for k, v in availpaths.items(): # display all dictionary keys
        print("{}. {} - {}km".format(counter,k,v)); counter += 1
    try: # Ask for user to choose a path to modify
        choice = int(input("Path to modify (hit enter to return):   "))
    except ValueError: input("\n\n\nYou must enter a int value,\npress enter to return to main menu"); return
    return 


# def returnpaths(city1, matrix): ## return a list of the paths len available to a city
#     loc = matrixcityloc(city1, matrix)
#     return(matrix[loc])

def returnpaths(city1, matrix): ## Return a dictionary of each path and weight from a point
    loc = matrixcityloc(city1, matrix) # find the xy of city
    cityweight = matrix[loc] # pick the weights froms the matrix
    cityweight.pop(0) # RM name of the path
    pathdict = dict() # init Dictionary
    for i in range(len(cityweight)):
        # if cityweight[i] == "------": continue we need to keep the structure of the matrix to be able to convert back
        pathdict[matrix[0][i+1]] = cityweight[i]
    return pathdict
    ### Ref
    # Provice city name and the matrix 
    # Paths will be returned as a DICT

def changeedge():
    global matrix # We want to edit matricies easier + error handeling
    availcities = listcities(matrix)
    print("-- Please choose starting node --")
    for i in range(len(availcities)):
        print("{}. {}".format(i, availcities[i]))
    try:
        choicecity1 = int(input("choice:   "))
    except ValueError: print("You must enter a int value"); return
    

    ### WANT TO CONVERT THIS TO chooseandreturn function for simplicity. ###
    ## Choose a city to view the edges on it
    availpaths = returnpaths(availcities[choicecity1], matrix) # Get all paths for the chosen city
    print("-- Current Paths --\n\n"); counter = 0; # , start counter
    for k, v in availpaths.items(): # display all dictionary keys
        print("{}. {} - {}km".format(counter,k,v)); counter += 1
    try: # Ask for user to choose a path to modify
        choice = int(input("Path to modify (hit enter to return):   "))
    except ValueError: input("\n\n\nYou must enter a int value,\npress enter to return to main menu"); return
    
    ## convert the Path into a city name
    counter = 0
    for k, v in availpaths.items():
        if counter == choice: choicecity2 = k
        counter += 1 
    
    ## set new value in matrix
    try: # Ask for user for new weight
        newfloat = float(input("New weight (hit enter to cancel modification):   "))
    except ValueError: input("\n\n\nYou must enter a int value,\npress enter to return to main menu"); return
    availpaths[choicecity2] = newfloat # Update dict with new value
    pushmatrix = [listcities(matrix)[choicecity1]] # matrix to add back [add name into matrix]
    for k, v in availpaths.items(): # add all values back into a matrix
        pushmatrix.append(v)
    matrix[choicecity1 +1] = pushmatrix # push to main matrix
    ### ONLY CHANGES THE FROM MATRIX FOR THAT NODE ###
        # need to change it in the other axis for #

def deleteedge(): ## Pretty much 80% the same as edit edge
    global matrix # We want to edit matricies easier + error handeling
    availcities = listcities(matrix)
    print("-- Please choose starting node --")
    for i in range(len(availcities)):
        print("{}. {}".format(i, availcities[i]))
    try:
        choicecity1 = int(input("choice:   "))
    except ValueError: print("You must enter a int value"); return
    
    ## Choose a city to view the edges on it
    availpaths = returnpaths(availcities[choicecity1], matrix) # Get all paths for the chosen city
    print("-- Current Paths --\n\n"); counter = 0; # , start counter
    for k, v in availpaths.items(): # display all dictionary keys
        print("{}. {} - {}km".format(counter,k,v)); counter += 1
    try: # Ask for user to choose a path to modify
        choice = int(input("Path to delete (hit enter to return):   "))
    except ValueError: input("\n\n\nYou must enter a int value,\npress enter to return to main menu"); return
    ## convert the Path into a city name
    counter = 0
    for k, v in availpaths.items():
        if counter == choice: choicecity2 = k
        counter += 1  

    ## set new value in matrix
    availpaths[choicecity2] = "------" # Update dict with "blank"
    pushmatrix = [listcities(matrix)[choicecity1]] # matrix to add back [add name into matrix]
    for k, v in availpaths.items(): # add all values back into a matrix
        pushmatrix.append(v)
    matrix[choicecity1 +1] = pushmatrix # push to main matrix
    ### ONLY CHANGES THE FROM MATRIX FOR THAT Path, as it could be directed.


def shortestpath(): ## Compute the shortest path from one vertex to the rest of the verticies
    global matrix
    ## this will need to make the user choose a path to generate all the different cities to choose from
    

def importdata():
    global matrix
    matrix = [["------"]]
    with open("network.txt","r") as file:
        while True:
            line = file.readline()
            if line == "": break 
            if "#" in line: continue
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
                    matrix[city1][city2] = line[2]
                    break
                except IndexError:
                    # If the Index doesn't exist add spacers to get it to right size
                    matrix[city2].append("------")
                    matrix[city1].append("------")
    return matrix

def saveall(matrix): # Save the updated matrix
    print("Forcing Save")
    print("Save Complete.")



def debug(matrix):
     # Testing Area
    print("\nTESTING\n-------")
    displaymatrix(matrix)
        # print("\nOttawa to Oshawa Dist.")
        # print(returnedgeweight("Ottawa","Kingston", matrix)) 
    print(listcities(matrix))
        # dict = returnpaths("Oshawa", matrix)
        # print(dict)
        # # loc = matrixcityloc("", matrix)
        # # print(loc)
        # # print(matrix[loc][0], matrix[0][loc])
        # input("")


def init():
    while True:
        print("\n" * 50)
        print("Choose a function\n\
            1. Build initial Graph from \"network.txt\"\n\
            2. Change an Edge weight\n\
            3. Remove Edge\n\
            4. Find and Display all shortest paths\n\
            5. Minimum Spanning Tree\n\
            6. Save-all\n\
            7. Quit\n\
            9. Debug")
        try:
            choice = int(input("choice:   "))
        except ValueError: print("You must enter a int value")
        if int(choice) == 1:
            matrix = importdata()
        elif int(choice) == 2:
            changeedge()
        elif int(choice) == 3:
            deleteedge()
        elif int(choice) == 4:
            print(choice)
        elif int(choice) == 5:
            print(choice)
        elif int(choice) == 6:
            save-all()
        elif int(choice) == 7:
            break
        elif int(choice) == 9:
            debug(matrix)
        else: continue
       
       

if __name__ == "__main__":
    init()