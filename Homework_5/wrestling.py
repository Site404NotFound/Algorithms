#!/usr/bin/python

"""
/*********************************************************************
** Author: James Hippler (HipplerJ)
** Oregon State University
** CS 325-400 (Spring 2018)
** Analysis of Algorithms
**
** Description: Homework #5 (Problem 5)
** Due: Sunday, May 13, 2018
**
** Filename: wrestling.py
**
** Objectives:
** Suppose there are two types of professional wrestlers:
** "Babyfaces" ("good guys") and "Heels" ("bad guys"). Between any pair of
** professional wrestlers, there may or may not be a rivalry. Suppose we
** have n wrestlers and we have a list of r pairs of rivalries.
**
** a) Give pseudocode for an efficient algorithm that determines whether
** it is possible to designate some of the wrestlers as Babyfaces and the
** remainder as Heels such that each rivalry is between a Babyface and a
** Heel. If it is possible to perform such a designation, your algorithm
** should produce it.
** b) What is the running time of your algorithm?
** c) Implement: Babyfaces vs Heels.
**
** Input: Input is read in from a file specified in the command line
** at run time. The file contains the number of wrestlers, n, followed by their
** names, the number of rivalries r and rivalries listed in pairs.
** Note: The file only contains one list of rivalries
**
** Output: Results are outputted to the terminal.
** - Yes, if possible followed by a list of the Babyface wrestlers and a
** list of the Heels.
** - No, if impossible.
**
** Sample Input file:
** 5
** Ace
** Duke
** Jax
** Biggs
** Stone
** 6
** Ace Duke
** Ace Biggs
** Jax Duke
** Stone Biggs
** Stone Duke
** Biggs Jax
**
** Sample Output:
** Yes
** Babyfaces: Ace Jax Stone
** Heels: Biggs Duke
**
** Submit a copy of your files including a README file that explains
** how to compile and run your code in a ZIP file to TEACH
**
** EXTERNAL RESOURCES:
** - https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
** - https://stackoverflow.com/questions/46383493/python-implement-
**	 breadth-first-search?utm_medium=organic&utm_source=google_rich_qa&utm_
**	 campaign=google_rich_qa
*********************************************************************/
"""

import sys
import os
from collections import defaultdict												# Import the library to create a dictionary with default formatting

"""
/************************************************************************
* Description: Rivalries class
* Initializes a default dictionary and creates a graph of connections
* between each wrestler and their matches.  Uses a Breadth-First
* Search (BFS) to traverse through each node in the graph.
*************************************************************************/
"""

class Rivalries:
    def __init__(self):
        self.graph = defaultdict(list)											# Initialize the graph structure that will hold our wrestlers and their connections
        self.babyfaces = []														# Initialize a list to store the babyface wrestlers
    	self.heels = []															# Initialize a list to store the heel wrestlers
    	self.visited = []														# Initialize a list to store the vertices that have been visited

    def add_connection(self, wrestler1, wrestler2):
        self.graph[wrestler1].append(wrestler2)									# Class function to build the connections (edges)

    def BFS(self, start):
    	distance = 0															# Create a variable to track edge distance from starting node
    	self.babyfaces.append(start)											# Append the starting wrestler as a babyface
    	explored = []															# Initialize an empty list
    	queue = [start]															# Create a queue and place the first node in element zero
    	self.visited.append(start)												# Add the first element to the visited list
    	while queue:
    		distance += 1
    		node = queue.pop(0)
    		explored.append(node)
    		neighbors = self.graph[node]
    		for neighbor in neighbors:
    			if neighbor not in self.visited:
    				queue.append(neighbor)
    				self.visited.append(neighbor)
    				if distance % 2 == 0:										# If the edge distance is even then assign the wrestler as a babyface
    					self.babyfaces.append(neighbor)
    				else:														# Else assign the wrestler as a heel
    					self.heels.append(neighbor)

"""
/************************************************************************
* Description: check_arguments function
* Function confirms that that user input the appropriate number of
* arguments when executing the program from the command line.  Prints
* error message if too many or too few arguments are received.
*************************************************************************/
"""

def check_arguments():
    if len(sys.argv) != 2:                                                      # If the user does not provide the correct number of arguments
    	print("Incorrent number of arguments!")                                 # Output an error message to the user
    	print("Please specify a file (only one) to read")
    	exit()                                                                  # Exit the program after presenting the error message

"""
/************************************************************************
* Description: read_file function
* Program opens a file for reading and grabs all lines to store as
* strings in a list.  If the file doesn't exist then an error is printed
* to the screen and the program exits safely.
*************************************************************************/
"""

def read_file():
	try:																		# See if the specified file exists
		with open(sys.argv[1], 'r') as file_info:								# Try opening the file for reading.  Use the second argument provided on the command line
			wrestlers = file_info.read().splitlines()							# Take each line from the file and add it to a list as a string
			return wrestlers 													# Return the list of string back to the main function
	except IOError:																# If the file doesn't exist
		print("File {} not found.  Please try again!".format(sys.argv[1]))		# Print an error message to the screen letting the user know
		exit()                                                                 	# Exit the program after presenting the error message

"""
/************************************************************************
* Description: get_roster_size function
* Function gets the amount of wrestlers that are present in the file and
* returns the value as an integer to main.
*************************************************************************/
"""

def get_roster_size(wrestlers):
    return (int(wrestlers[0]))													# Assign the integer value from the first line in the text file as the number of wrestlers

"""
/************************************************************************
* Description: get_match_total function
* Function gets the amount of matches that are present in the file and
* returns the value as an integer to main.
*************************************************************************/
"""

def get_match_total(wrestlers, roster_size):
    return (int(wrestlers[roster_size + 1]))                                     # Grab the amounts value and store in array as an integer

"""
/************************************************************************
* Description: get_wrestlers function
* Function returns a list of the wrestler names that are present in
* the file.  Each line is store in a list as a string.
*************************************************************************/
"""

def get_wrestlers(wrestlers, roster_size):
    return (wrestlers[(1) : (1 + roster_size)])                                 # Grab sections of the list based on amounts and append to the activities array

"""
/************************************************************************
* Description: get_matches function
* Function gets the lists of matches that occurs and stores both
* wrestlers as a string in a list of strings.
*************************************************************************/
"""

def get_matches(wrestlers, roster_size, match_total):
    matches = []																# Create an array that stores match information
    for x in range(match_total):												# Loop through all available matches
        fight = (wrestlers[(roster_size + 2 + x) : (2 + roster_size + x + 1)])	# Take the first and second wrestler name
        matches.append(fight[0].split())										# Store the information to an array
    return matches 																# Return the complete array back to the main function

"""
/************************************************************************
* Description: build_graph function
* Function takes the wrestling match information and send that data to
* the rivalries class to create the appropriate connections on the graph
*************************************************************************/
"""

def build_graph(cage_match, matches):
    for x in range(len(matches)):                                           	# Iterate through all the scheduled fights
        cage_match.add_connection(matches[x][0], matches[x][1])                 # Add the two fighter names as connections on the graph
       	cage_match.add_connection(matches[x][1], matches[x][0])

"""
/************************************************************************
* Description: trace_graph function
*************************************************************************/
"""

def trace_graph(cage_match, wrestlers_names):
	startingval = 0																# Initialize the starting value to zero
	visited = [False] * (len(wrestlers_names))
	while False in visited:														# Continue running the function until all vertices are accounted for
		for x in range(len(visited)):											# Search through the visited list of bool values for false
			if visited[x] == False:												# If FALSE is encountered then that element becomes the new staring point
				startingval = x
				break
		cage_match.BFS(wrestlers_names[x])
		for x in range(len(wrestlers_names)):
			if wrestlers_names[x] in cage_match.visited:
				visited[x] = True

"""
/************************************************************************
* Description: rivalries_possible function
*************************************************************************/
"""

def rivalries_possible(cage_match):
	print("GRAPH LAYOUT: {}".format(cage_match.graph))
	print("VISITED VERTICES: {}".format(cage_match.visited))
	print("BABYFACES: {}".format(cage_match.babyfaces))
	print("HEELS: {}".format(cage_match.heels))

"""
/************************************************************************
* Description: main function
* Program starts here and calls functions as necessary
* Calls the make_change function that completes most of the program's
* functionality.  Also manages the functions that read & write data
* from files.
*************************************************************************/
"""

if __name__ == "__main__":
	start = 0
	cage_match = Rivalries()
	check_arguments()															# Call function to confirm that the user input the appropriate number of arguments
	wrestlers = read_file()														# Read the file specified by the user and return list with strings of each line
	roster_size = get_roster_size(wrestlers)									# Get the amount of wrestlers participating in the matches
	match_total = get_match_total(wrestlers, roster_size)						# Get the amount of matches that will occur
	wrestlers_names = get_wrestlers(wrestlers, roster_size)						# Grab each individual wrestler's name
	matches = get_matches(wrestlers, roster_size, match_total)					# Grab the names of the wrestlers involved in each match
	build_graph(cage_match, matches)
	trace_graph(cage_match, wrestlers_names)
	rivalries_possible(cage_match)
