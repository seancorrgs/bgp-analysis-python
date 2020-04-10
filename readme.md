# Sean Corrigan - 100693058 
#### INFR2020 Final Project

[GITLAB REPO](https://gitlab.platinumnetworks.ca/imp4ct/infr2820-final/)
##### Dependancies 
    There are no dependencies other than stock python 3.7
         
**This Project assumes a unidirectional link in line with a clairification from Dr. Khalil El-Khatib**
    
    Q: "should we be limiting a path to uni-directional links 
    or should a path from toronto-hamilton also go hamilton-toronto 
    at the same weight?"
    
    Dr. El-Khatib -  "you can make any assumption you want about this."

**I have assumed the following:**

a connection may have one route cost one way and a **different** route cost the other way (eg. longer fiber for TX than RX)
**directed graph**


### Main Menu Options

The code will provide options to the user in line with each requirement of the assignment that was asked for (it has the following sections)

1. [Build initial Graph from "network.txt"](#1-build-initial-graph-from-networktxt)
2. [Change an Edge weight](#2-change-an-edge-weight)
3. [Remove Edge](#3-remove-an-edge)
4. [Remove Node](#4-removing-a-node)
5. [Find and Display all shortest paths](#5-display-shortest-path-from-a-single-root-node)
6. [Minimum Spanning Tree](#6-display-minimum-spanning-tree-based-on-kruskals-algorithim)
7. [Save-all](#7-save-all)
8. [Quit](#8-quit)
9. Display Entire graph
 

#### 1. Build initial graph from "network.txt"


To build an initial graph from a text file you must have a text file in the directory you are running the code from named "network.txt"

**it is important to make sure your file is formatted as below**
    
    # Originating Point, Destination Point, Cost
    Ottawa Whitby 1
    Whitby Oshawa 1
    Oshawa Toronto 9

The code will then import the file line by line into its internal matricies ignoring any lines that are blank or include a # or : in that line (useful for commenting out a line for testing)

#### 2. Change an edge weight 


To change an edge weight the user must provide a src and destination the program will provide an input for both

    -- Please choose starting node --
    0. Ottawa
    1. Montreal
    2. Kingston
    3. Oshawa
    4. Whitby
    5. Toronto
    choice:   

Once a choice is made, in this case 0-5. The program will return a list of connections that node has.

    -- Current Paths --
    
    0. Ottawa - ------km
    1. Montreal - 199km
    2. Kingston - 196km
    3. Oshawa - 10km
    4. Whitby - 1km
    Path to modify (hit enter to return):

You may then choose an edge to edit and put in a new value 

    Path to modify (hit enter to return):   3
    New weight (hit enter to cancel modification):   32

#### 3. Remove an Edge


When choosing 3 on the main menu the user will be presented with the option to present an edge weight via a choice of a src and destination to locate the edge to be deleted
    
    -- Please choose starting node --
    0. Ottawa
    1. Montreal
    2. Kingston
    3. Oshawa
    4. Whitby
    5. Toronto
    choice:   0
    -- Current Paths --
    
    
    0. Ottawa - ------km
    1. Montreal - 199km
    2. Kingston - 196km
    3. Oshawa - 10km
    4. Whitby - 1km
    Path to delete (hit enter to return):   1

Choosing 0 then 1 in this example, removes the edge from Ottawa to Montreal; instead replacing it with the weight of '------' in the Matrix

#### 4. Removing a Node 


If the user would like to remove a node the matrix then they can do so.
The program will then provide the user with a list of all the nodes loaded

    -- List of Nodes --
    0. Ottawa
    1. Montreal
    2. Kingston
    3. Oshawa
    4. Whitby
    5. Toronto

    Enter to Return
    Choose a node to delete..
    #   3  

The code will then delete that node by looping through the entire matrix for any referance to that node, for example if the node has multiple paths to other nodes the program will 'zero-out' that path list so that all values equal '------' which is the programs way to signify a null value.

The **code responsable** for doing this is the deletenode() function.

    matrix[0][nodetodelete+1] = "------" # Delete node reference in the main table
    matrix[nodetodelete + 1] = ["------"] # Delete any reference to the user 
    for x in matrix: # for each node pathway list | Delete the nodes path to the node we are deleting
        try:
            x[nodetodelete + 1] = "------" # Replace all occasions of that node in other paths.
        except IndexError: # if there was never a reference to a node path at that list
            pass # move on to next item in list




#### 5. Display shortest path from a single root node


To display a shortest path calculation from a specific node the program will ask the user which node to run from:

    -- Please choose starting node --
    0. Ottawa
    1. Montreal
    2. Kingston
    3. Oshawa
    4. Whitby
    5. Toronto
    choose node to compute shortest path with Bellman-Ford:
    #   

When the user picks a node to start the Bellman-Ford algorithim the program will return a list of each destination, the next hop and the total cost for that path (including any hops):

example:
    Ottawa    | Next Hop -> Ottawa |  Total Cost: 5
    Montreal  | Next Hop -> Ottawa |  Total Cost: 204.0
    Kingston  | Next Hop -> Ottawa |  Total Cost: 201.0
    Oshawa    | Next Hop -> Oshawa |  Total Cost: ------
    Whitby    | Next Hop -> Ottawa |  Total Cost: 6.0
    Toronto   | Next Hop -> Toronto|  Total Cost: 61


    Press Enter to return to main menu

###### The ALGORITHIM is implemented in the BELLMANFORD() function

The function does a few things to implement the Bellman-Ford algorithim algorithim in Python without the use of **any** external algorithims

1. The Algorithim will create a list of each node with a weight from the current node:

        currentcities = [] ## INIT LIST
        nexthop = dict()

2. The algorithim will then make a list for any next-hops that need to be recorded by the algorithim:

        nexthoplist = dict(pathsfornode) # set a next hop list of the path for node DICT
        for x,y in nexthoplist.items(): ## For each city
            nexthoplist[x] = x # Set all next hops to self '

3.  The algorithim will itterate throughout the list of weights and compare them with the current list that are stored in the functions memory. Then if it finds a path with a shorter path to the destination in that iteration it will then return 

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


#### 6. Display Minimum Spanning Tree Based on Kruskals Algorithim


The minimum spanning tree function must follow some simple rules

Rules of Kruskal:

1. No Loops
2. Add paths in order of smallest to largest 

###### Code implementation

To implement this into my code I decided to use an "affiliation" of each and every Node. Once a node is added to a forest in the graph it is given an affiliation. If it is not connected to any node with a previous affiliation then the program will increment the affiliation number by one and assign that forest a new affiliation ID. example below:

     if src == False and dest == False: # If neither have an affiliation | ie. new forest
            MST.append([x[0],x[1],x[2]]) 
            # Append new affiliations for src and dest
            lettergroups.append([x[0], affiliation])
            lettergroups.append([x[1], affiliation])
            affiliation += 1 # We created a new forest

If a route between two nodes with the same affiliation is found then the program will count that as a loop in a forest and discard that route. 

Loop catch statement:

    elif src == dest: 
            continue


If 2 different forests (affiliations) have a route between them then the program will change the affiliation of all of the highernumbered routes to match the lower numbered forest then complete the route into the MST list. snippet below:
   
    # src = the source node affiliation | dest = the destination node affiliation
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

#### 7. Save All

Saves the current working Matrix and Graph back to the file network.txt

#### 8. Quit

    Exits the program

#### 9. Display current Graph

Displays the current graph with any changes made with options 2-4

### License
##### BSD-0 
Copyright (C) 2020 by Sean Corrigan sean.corrigan1@uoit.net

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.