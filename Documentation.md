# Sean Corrigan - 100693058 
#### INFR2020 Final Project

[GITLAB REPO](https://gitlab.platinumnetworks.ca/imp4ct/infr2820-final/)
##### Dependancies !!!!
    There are no dependencies other than stock python 3.7
         
**This Project assumes a unidirectional link in line with clairification from Dr. Khalil El-Khatib**
    
    Q: "should we be limiting a path to uni-directional links or should a path from toronto-hamilton also go hamilton-toronto at the same weight?"
    
    Dr. El-Khatib -  "you can make any assumption you want about this."

I have assumed the following:

a connection may have one route cost one way and a **different** route cost the other way (eg. longer fiber for TX than RX)


### Main Menu Options

The code will provide options to the user in line with each requirement of the assignment that was asked for.

    Choose a function
            1. Build initial Graph from "network.txt"
            2. Change an Edge weight
            3. Remove Edge
            4. Find and Display all shortest paths
            5. Minimum Spanning Tree
            6. Save-all
            7. Quit
            9. Debug
    choice:   

#### Build initial graph from "network.txt"
###### Menu Option - 

To build an initial graph from a text file you must have a text file in the directory you are running the code from named "network.txt"

**it is important to make sure your file is formatted as below**
    
    # Originating Point, Destination Point, Cost
    Ottawa Whitby 1
    Whitby Oshawa 1
    Oshawa Toronto 9

The code will then import the file line by line into its internal matricies ignoring any lines that are blank or include a # in that line (useful for commenting out a line for testing)

#### Change an edge weight 
###### Menu Option - 

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

#### Remove an Edge
###### Menu Option -

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

#### Removing a Node
###### Menu Option -

    Documentation will be added once the function is added
    
#### Display shortest path from a node
###### Menu Option -

    Documentation will be added shortly

#### Display Minimum Spanning Tree Based on Kruskals Algo
###### Menu Option -

### License
##### BSD-0 
Copyright (C) 2020 by Sean Corrigan sean.corrigan1@uoit.net

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.