#!/usr/bin/python

"""
********************************************************************************
** Authors:
** Caitlin Dudley (dudleyca@oregonstate.edu)
** James Hippler (hipplerj@oregonstate.edu)
** Kyle Martinez (martink9@oregonstate.edu)
**
** Oregon State University
** CS 325-400 (Spring 2018)
** Analysis of Algorithms
**
** Project Group 2
** Description: Final Project (Travelling Salesman Problem)
** Due: Friday, June 08, 2018
**
** Filename: CS325_Project_Group2.py
**
** Project Specifications:
** Your group will research at least three different algorithms for solving the
** TSP problem.  Each Group member should research an algorithm and provide
** pseudocode for that algorithm even if it is not implemented. There is much
** literature on methods to "solve" TSP please cite any sources you use. Your
** group will design and implement at least one algorithm for finding the best
** tour you can for the TSP problem. TSP is not a problem for which you will be
** able to easily find optimal solutions. It is difficult. Your goal is to find
** the best solution you can in a certain time frame. Use any programming
** language you want that runs on the engineering servers.
********************************************************************************
"""

import sys                                                                      # Import the library for using sys functionality
import os                                                                       # Import the library for using os functionality
import time                                                                     # Import the library for using system time/clock
from collections import defaultdict												# Import the library to create a dictionary with default formatting
import nearest_neighbor as nn                                                   # Import code from the nearest_neighbor algorithm file
import two_opt                                                                  # Import code from the two opt algorithm file

"""
********************************************************************************
* Description: check_arguments function
********************************************************************************
"""

def check_arguments():
    if len(sys.argv) != 3:                                                      # If the user does not provide the correct number of arguments
        print("Incorrent number of arguments!")                                 # Output an error message to the user
        print("USAGE: CS325_Final_Group2.py <input_file> <mode_switch>")        # Output message demonstrating correct usage
        print("EXAMPLE: CS325_Final_Group2.py test-input-1.txt -t")
        exit()                                                                  # Exit the program after presenting the error message

"""
********************************************************************************
* Description: check_execution_flag function
********************************************************************************
"""

def check_execution_flag():
    if sys.argv[2] != "-t" and sys.argv[2] != "-c":
        print("Incorrect Usage Flag {}".format(sys.argv[2]))
        print("-c: Used for competition mode (Adheres to 3 minute timer)")
        print("-t: Used for testing mode (More accurate but runs longer")
        exit()
    elif sys.argv[2] == "-c":
        competition_mode = True
    else:
        competition_mode = False
    return competition_mode

"""
********************************************************************************
* Description: read_file function
********************************************************************************
"""

def read_file():
    try:																		# See if the specified file exists
        with open(sys.argv[1], 'r') as file_info:								# Try opening the file for reading.  Use the second argument provided on the command line
            routes = file_info.read().splitlines()			                    # Take each line from the file and add it to a list as a string
            return routes 													    # Return the list of string back to the main function
    except IOError:																# If the file doesn't exist
        print("File {} not found.  Please try again!".format(sys.argv[1]))		# Print an error message to the screen letting the user know
        exit()                                                                 	# Exit the program after presenting the error message

"""
********************************************************************************
* Description: get_city_information function
********************************************************************************
"""

def get_city_information(index, routes):
    data = ' '.join(routes.split(" ")).split()                                                    # Split each element in routes into sub elements split by space " "
    city = int(data[0])                                                         # Assign the first element to city
    coordinates = data[1:]                                                      # Assign the last two elements to coordinates
    return(city, coordinates)                                                   # Return the city and the coordinates

"""
********************************************************************************
* Description: build_dict_list function
********************************************************************************
"""

def build_dict_list(dict_list, city, coordinates):
    keys = ['id', 'x', 'y']
    city_info = [city, int(coordinates[0]), int(coordinates[1])]
    dict_list.append(dict(zip(keys, city_info)))

"""
********************************************************************************
* Description: write_file function
********************************************************************************
"""

def write_file(routes):
    with open(sys.argv[1]+".tour", 'w') as file_info:					        # Try opening the file for reading.  Use the second argument provided on the command line
        file_info.write(str(routes[len(routes) - 1]) + '\n')                           # Write length as first line
        for x in range(0, len(routes[0])):                                      # Loop through each line of the routes object
            file_info.write(str(routes[0][x]['id']) + '\n')			                # Take each line from the file and add it to a list as a string
    print("Results written to \"{}\"".format(sys.argv[1] + ".tour"))

"""
********************************************************************************
* Description: start_clock function
********************************************************************************
"""

def start_clock():
    return time.time()                                                          # Collect the current clock time for the system

"""
********************************************************************************
* Description: end_clock function
********************************************************************************
"""

def end_clock(start_time):
    print("Time to Complete: {} seconds".format(time.time() - start_time))      # Output the time to complete the program.

"""
********************************************************************************
* Description: main function
********************************************************************************
"""

def main():
    dict_list = []
    start_time = start_clock()                                                  # Call Function to record the system clock and start the timer
    check_arguments()															# Call function to confirm that the user input the appropriate number of arguments
    mode = check_execution_flag()
    routes = read_file()														# Read the file specified by the user and return list with strings of each line
    for x in range(len(routes)):                                                # Loop through each line in the routes list
        cities, coordinates = get_city_information(x, routes[x].lstrip())       # Collect the city and coordinate information
        build_dict_list(dict_list, cities, coordinates)                         # Call function to build a list of dicts to act as a hash table

    best_tour = nn.nearest_neighbor(dict_list)                                  # Generate an initial tour
    best_tour = two_opt.two_opt(best_tour[0], start_time, mode)                 # Use two_opt to make the tour better

    write_file(best_tour)                                                       # Call function to write results to the appropriate file name
    end_clock(start_time)                                                       # Call function to end the timer and display the running time

if __name__ == "__main__":
    main()                                                                      # Call the main function and start the program
