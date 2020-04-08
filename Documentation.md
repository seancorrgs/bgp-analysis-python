# Sean Corrigan - 100693058 
#### INFR2020 Final Project

[GITLAB REPO](https://gitlab.platinumnetworks.ca/imp4ct/infr2820-final/)

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

#### Build initial graph from "network.txt" -

To build an initial graph from a text file you must have a text file in the directory you are running the code from named "network.txt"

The code will then import the file line by line into its internal matricies ignoring any lines that are blank or include a # in that line (useful for commenting out a line for testing)

**it is important to make sure your file is formatted as below**
    
    # Originating Point, Destination Point, Cost
    Ottawa Whitby 1
    Whitby Oshawa 1
    Oshawa Whitby 9

#### Change an edge weight - 

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





### License
##### BSD-0 


Copyright (C) 2020 by Sean Corrigan sean.corrigan1@uoit.net

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.