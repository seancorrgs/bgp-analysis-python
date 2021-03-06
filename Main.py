##########################
# Sean Corrigan 2020
# 100693058
# sean.corrigan1@ontariotechu.net
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
    for x in matrix:
        if x[0] == "------": continue ## Ignore invalid matricies
        print("\n\n{} Available Paths".format(x[0]))
        for i in range(len(x)):
            if i == 0: continue
            try:
                print("Dest: {}  | Cost: {}".format(matrix[0][i],x[i]))
            except:
                continue
    input("\nPress Return to go back to the main menu")


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

def deletenodeselect(): # Delete entire node function including asking for what node || Will call the deletenode() API
    global matrix
    ## Choose a city to view the edges on it
    availcities = listcities(matrix)
    print("-- List of Nodes --")
    for i in range(len(availcities)):
        print("{}. {}".format(i, availcities[i]))
    try:
        choicecity1 = int(input("\nEnter to Return\nChoose a node to delete..\n#   "))
    except ValueError: print("You must enter a int value"); return
    if choicecity1 == "": return
    deletenode(choicecity1)

def deletenode(nodetodelete): ## Loop through each 'row' in the matrix deleting a certain matrix index IF IT IS AVAILABLE
    global matrix
    matrix[0][nodetodelete+1] = "------" # Delete node reference in the main table
    matrix[nodetodelete + 1] = ["------"] # Delete any reference to the user 
    for x in matrix: # for each node pathway list | Delete the nodes path to the node we are deleting
        try:
            x[nodetodelete + 1] = "------" # Replace all occasions of that node in other paths.
        except IndexError: # if there was never a reference to a node path at that list
            pass # move on to next item in list

def bellmanford(startingnode, startingindex): ## Called from shortest path function for simplicity
    global matrix
    pathsfornode = dict(returnpaths(startingnode))    # This is the current direct paths we have
    pathstocompute = listcities(matrix)               # This is all the destinations we need to get to

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

            ## Setup some vars before the nexthop comparisons
            tempdistance = weight # set the current hop distance
            temppathweights = dict(returnpaths(dest)) # get the list of destinations from this node 

            ## CHECK THE LENGTHS OF THE LIST AGAINST THE CURRENT HOP LIST
            counter = 0 # init counter
            for nexthop, nextweight in temppathweights.items(): # pull nexthop and the cost from current node
                tempdistance = float(weight) # set the current hop distance
                if nexthop == startingnode: continue ## ignore node if its the source of the hop
                if nextweight == '------': continue  ## ignore if no hop available
                if pathsfornode[nexthop] == '------':  ## if theere is no nexthop/path for the current path
                    pathsfornode[nexthop] = float(nextweight) + float(tempdistance) # Set path to our current path + current next hop amount
                    nexthoplist[nexthop] = dest     # Set the next hop as the hop it 
                    continue # start loop again
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

def deleteallcontent(tmatrix): ## Delete all the weights to create a blank table
    newmatrix = []
    for i in tmatrix: # for each list of edges
        newSubMatrix = [] # create temp matrix 
        for x in i: # for each individual edge
            try:
                float(x)
                newSubMatrix.append("------")
            except:
                newSubMatrix.append(x)
        newmatrix.append(newSubMatrix)
    return newmatrix

def convertabp(matrix): ## Convert to a list of src, dest, path for easier MST calculation
    newmat = []
    for x in matrix:
        if x[0] == "------": continue ## Ignore invalid matricies
        for i in range(len(x)):
            if i == 0: continue
            if x[i] == "------": continue
            try:
                newmat.append([x[0],matrix[0][i],x[i]])
            except:
                continue
    return newmat

def NodeVisited(mst, point):
    for x in range(len(mst)):
        if mst[x][1] == point or mst[x][0] == point: # if the src or destination is in the graph
            return True
        
    return False

def returngroupafill(lettergroups, node): # Return the gang affiliation of a letter
    for x in lettergroups:
        if x[0] == node:
            return x[1]
    return False

def gangtakeover(letterG, win, lose): ## When 2 forests need to be combined rename all of forest 2
    for x in range(len(letterG)):
        if letterG[x][1] == lose: # if it is in losing forest
            letterG[x][1] = win # set to new forest id 
    return letterG

def minimumspanningTree(mat):
    ## Set up some temporary matricies to work with in this algorithim
    listOweights = convertabp(mat);    # Create a list for the order of weights 
    listOweights = sorted(listOweights, key=lambda x: x[2])
    MST = []
    lettergroups = [] # ["A", 1]

    ## Lets get adding
    affiliation = 1
    for x in listOweights: # ALGO FOR MST
        # if NodeVisited(MST, x[1]): 
        src = returngroupafill(lettergroups, x[0])
        dest = returngroupafill(lettergroups, x[1])
        if src == False and dest == False: # If neither have an affiliation | ie. new forest
            MST.append([x[0],x[1],x[2]]) 
            # Append new affiliations for src and dest
            lettergroups.append([x[0], affiliation])
            lettergroups.append([x[1], affiliation])
            affiliation += 1 # We created a new forest
        elif src == False or dest == False: # if one have an affiliation
            if src == False:
                MST.append([x[0],x[1],x[2]])
                lettergroups.append([x[0], dest])
                lettergroups.append([x[1], dest])
            elif dest == False:
                MST.append([x[0],x[1],x[2]])
                lettergroups.append([x[0], src])
                lettergroups.append([x[1], src])
        elif src == dest: 
            continue
        elif src and dest:
            if src > dest:
                lettergroups = gangtakeover(lettergroups, dest, src)
                lettergroups.append([x[0], dest])
                lettergroups.append([x[1], dest])
            if dest > src:
                lettergroups = gangtakeover(lettergroups, src, dest)
                MST.append([x[0],x[1],x[2]])
                lettergroups.append([x[0], src])
                lettergroups.append([x[1], src])
    print(lettergroups)
    print(MST)


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
    return

def saveall(matrix): # Save the updated matrix
    print("Forcing save...")
    abp = convertabp(matrix)
    with open("network.txt","w") as file:
        for x in abp:
            file.write("{} {} {}\n".format(x[0], x[1], x[2]))

def debug(matrix):
     # Testing Area
    print("\nTESTING\n-------")
    displaymatrix(matrix)
    print(listcities(matrix))


def init():
    global matrix
    matrix = []
    while True:
        choice = 0
        print("\n" * 50)
        print("Choose a function\n\
            1. Build initial Graph from \"network.txt\"\n\
            2. Change an Edge weight\n\
            3. Remove Edge\n\
            4. Delete Entire Node\n\
            5. Find and Display all shortest paths from node __\n\
            6. Minimum Spanning Tree\n\
            7. Save-all\n\
            8. Quit\n\
            9. Display Current Graph")
        try:
            choice = int(input("choice:   "))
        except ValueError: print("You must enter a int value")
        if int(choice) == 1:
            importdata()
        elif matrix == []:
            input("No network.txt has been imported \npress return to load one from current directoy")
            importdata()
        elif int(choice) == 2:
            changeedge()
        elif int(choice) == 3:
            deleteedge()
        elif int(choice) == 4:
            deletenodeselect()
        elif int(choice) == 5:
            shortestpath()
        elif int(choice) == 6:
            saveall(matrix)
            minimumspanningTree(matrix)
            importdata()
        elif int(choice) == 7:
            saveall(matrix)
            # importdata()
        elif int(choice) == 8:
            return
        elif int(choice) == 9:
            displaymatrix(matrix)
        elif int(choice) == 10:
            print(convertabp(matrix))

        else:
            continue
       
       

if __name__ == "__main__":
    init()