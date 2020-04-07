##########################
# Sean Corrigan 2020
# 100693058
# 
# https://gitlab.platinumnetworks.ca/imp4ct/infr2820-final/ < GIT History | private until day after assignment is submitted 
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
    print(matrix)

def listcities(matrix): ## Return a list of the cities in the array
    citylist = []
    for i in range(len(matrix[0])):
        if i == 0: continue # Dont Index Placeholder
        citylist.append(matrix[0][i])
    return citylist

def returnpaths(city1): ## Return a dictionary of each path and weight from a point
    global matrix
    loc = matrixcityloc(city1, matrix) # find the xy of city
    cityweight = list(matrix[loc]) # pick the weights froms the matrix
    cityweight.pop(0) # RM name of the path
    pathdict = dict() # init Dictionary
    for i in range(len(cityweight)):
        # if cityweight[i] == "------": continue we need to keep the structure of the matrix to be able to convert back
        try:
            pathdict[matrix[0][i+1]] = cityweight[i]
        except IndexError:
            return pathdict
    return pathdict
    ### Ref
    # Provice city name | Matrix must be global from requesting function
    # Paths will be returned as a DICT

def changeedge():   ## Change a specific path in the graph
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
    availpaths = returnpaths(availcities[choicecity1]) # Get all paths for the chosen city
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
        newfloat = int(input("New weight (hit enter to cancel modification):   "))
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
    availpaths = returnpaths(availcities[choicecity1]) # Get all paths for the chosen city
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

def deletenode(): ## Delete an entire node from the graph including all referances
    global matrix
    ## Loop through each 'row' in the matrix deleting a certain matrix index IF IT IS AVAILABLE

def bellmanford(startingnode, startingindex): ## Called from shortest path function for simplicity
    global matrix
    pathsfornode = dict(returnpaths(startingnode))    # This is the current direct paths we have
    pathstocompute = listcities(matrix)         # This is all the destinations we need to get to

    ## Bring the pathsfornode DICT up to speed on total not just computed paths
    # for x, y in pathsfornode.items: # Change '--
    #     if y == '------':
    #         pathsfornode[x] = 0
    ## Check if city is in dict / if not then set to ------
    currentcities = [] ## INIT LIST
    nexthop = dict()
    for x,y in pathsfornode.items():
        nexthop[x] = "*"
        currentcities.append(x)
    for target in pathstocompute: # for each overall destination
        if target in currentcities: continue
        else:
            pathsfornode[target] = '------'
    ## Now we have a dict with current shortest paths (in order) and also ------ for paths with no route yet ##
    # We need to recurvively find new routes using pathsfornodes #
    nexthoplist = dict(pathsfornode) # set a next hop list of the path for node DICT
    for x,y in nexthoplist.items(): ## For each city
        nexthoplist[x] = x # Set all next hops to self '
    # print(pathsfornode)
    # input(nexthoplist)
    
    iterations = len(pathsfornode) - 1 # Max iteration, we will use this later
    while iterations > 0: 
        for dest, weight in pathsfornode.items(): # {'Ottawa': '------', 'Montreal': '199', 'Kingston': '196', 'Oshawa': '------', 'Whitby': '------', 'Toronto': '------'}
            ## GET SOME TEMP INFO FOR THIS HOP
            if dest == startingnode: continue ## if nexthop is current node ignore
            if weight == '------': continue # no route to host, dont compute
            # input(str(dest) + str(weight))

            ## Setup some vars
            tempdistance = weight # set the current hop distance
            temppathweights = dict(returnpaths(dest)) # get the list of destinations from this node 

            ## CHECK THE LENGTHS OF THE LIST AGAINST THE CURRENT HOP LIST
            counter = 0 # init counter
            for nexthop, nextweight in temppathweights.items(): # pull nexthop and the cost from current node
                tempdistance = float(weight) # set the current hop distance
                if nexthop == startingnode: continue 
                if nextweight == '------': continue 
                if pathsfornode[nexthop] == '------': pathsfornode[nexthop] = float(nextweight) + float(tempdistance); nexthoplist[nexthop] = dest; continue
                if float(pathsfornode[nexthop]) > float(nextweight) + float(tempdistance): pathsfornode[nexthop] = float(nextweight) + float(tempdistance); nexthoplist[nexthop] = dest; continue
        iterations -= 1 # Increment Counter Down
    return nexthoplist, pathsfornode

def shortestpath(): ## Compute the shortest path from one vertex to the rest of the verticies
    global matrix
    ## Choose a city to view the edges on it
    availcities = listcities(matrix)
    print("-- Please choose starting node --")
    for i in range(len(availcities)):
        print("{}. {}".format(i, availcities[i]))
    try:
        choicecity1 = int(input("choose node to compute shortest path with Bellman-Ford:\n#   "))
    except ValueError: print("You must enter a int value"); return
    choicename = availcities[choicecity1]
    nexthops, pathsfornode = bellmanford(choicename, choicecity1)
    counter = 0
    for x,y in nexthops.items():
        print("{}  | Next Hop -> {} |  Total Cost: {}".format(x,y, pathsfornode[x])) 
    input("\n\nPress Enter to return to main menu")


def importdata():
    global matrix
    matrix = [["------"]]
    with open("network.txt","r") as file:
        while True:
            line = file.readline()
            if line == "": break 
            if "#" in line: continue
            if ":" in line: continue
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
        choice = 0
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
            shortestpath()
        elif int(choice) == 5:
            print(choice)
        elif int(choice) == 6:
            saveall()
        elif int(choice) == 7:
            break
        elif int(choice) == 9:
            debug(matrix)
        else: continue
       
       

if __name__ == "__main__":
    init()