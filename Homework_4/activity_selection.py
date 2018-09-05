#!/usr/bin/python

"""
/*********************************************************************
** Author: James Hippler (HipplerJ)
** Oregon State University
** CS 325-400 (Spring 2018)
** Analysis of Algorithms
**
** Description: Homework #4 (Problem 5)
** Due: Sunday, April 29, 2018
**
** Filename: activity_selection.py
**
** Objectives:
** You may use any language you choose to implement the activity selection
** last-to-start algorithm described in problem 4. Include a verbal description
** of your algorithm, pseudocode and analysis of the theoretical running time.
** You do not need to collected experimental running times. The program should
** read input from a file named "act.txt". The file contains lists of activity
** sets with number of activities in the set in the first line followed by lines
** containing the activity number, start time & finish time.
**
** Example act.txt:
** 11
** 1 1 4
** 2 3 5
** 3 0 6
** 4 5 7
** 5 3 9
** 6 5 9
** 7 6 10
** 8 8 11
** 9 8 12
** 10 2 14
** 11 12 16
** 3
** 3 6 8
** 1 7 9
** 2 1 2
**
** In the above example the first activity set contains 11 activities with
** activity 1 starting at time 1 and finishing at time 4, activity 2 starting at
** time 3 and finishing at time 5, etc.. The second activity set contains 3
** activities with activity 3 starting at time 6 and finishing at time 8 etc.
** The activities in the file are not in any sorted order.
**
** Your results including the number of activities selected and their order
** should be outputted to the terminal. For the above example the results are:
**
** Set 1
** Number of activities selected = 4
** Activities: 2 4 9 11
**
** Set 2
** Number of activities selected = 2
** Activities: 2 1
**
** Note: There is an alternative optimal solution for Set 1. Since activities
** 8 and 9 have the same start time of 8, a2 a4 a8 a11 would be an alternative
** solution. Your program only needs to find one of the optimal solution.
** For either solution the activities differ from the solution presented in the
** text which uses the earliest-finish time criteria.
*********************************************************************/
"""

"""
/************************************************************************
* Description: activity_sort function
* Functions receives a list of arrays from main and performs a merge sort
* to place the numbers in descending order based on start time.  The function
* takes and array and recursively devides until it reaches array sizes of one.
* It passes data to a merge function that combines the elements in
* decending order into the original array
*************************************************************************/
"""

def activity_sort (amounts, activities):

    if amounts < 1:                                                             # If Array Size is less than 1, this is invalid
        print("Array Size {} is invalid".format(arraySize))                     # print an error to the console
    elif amounts == 1:                                                          # If the array size is one it's already sorted
        return activities                                                       # Return the array as is without performing any work
    else:                                                                       # If the array is greater than size one (less than one and already sorted)
        first = activities[:(amounts // 2)]                                     # Split the array and assign the left (bottom) half to variable (Use Floor Division)
        last = activities[(amounts // 2):]                                      # Split the array and assign the right (top) half to variable (Use Floor Division)
        firstArray = activity_sort(len(first), first)                           # Recursively call the mergeSort function and send the first half of the array
        secondArray = activity_sort(len(last), last)                            # Recursively call the mergeSort function and send the second half of the array
    return merge (activities, firstArray, secondArray)

"""
/************************************************************************
* Description: merge function
* Called by the mergeSort function to evaluate and merge the split array
* elements back into a single sorted array.  Receives the original array
* the split right and left arrays and their respective lengths.  Returns
* a sorted integer array to mergerSort
*************************************************************************/
"""

def merge (dataArray, first, second):
    firstcount = secondcount = originalcount = 0                                # create three counter variables and initialize to zero
    while firstcount < len(first) and secondcount < len(second):                # while both the left and right counters are less than their array lengths
        if first[firstcount][1] > second[secondcount][1]:                       # If the left array is less than the right
            dataArray[originalcount] = first[firstcount]                        # Assign it to the current element in the original array
            firstcount += 1                                                     # Increment left array counter by one (hate that python can't just do ++)
        else:                                                                   # otherwise if the right array element is smaller
            dataArray[originalcount] = second[secondcount]                      # Assign it to the current element in the original array
            secondcount += 1                                                    # Increment Right array counter by one
        originalcount += 1                                                      # Increment original array counter by one
    while firstcount < len(first):                                              # If the first count is still less than the left array length
        dataArray[originalcount] = first[firstcount]                            # assign the current element from the left array to the current element in the original array
        firstcount += 1                                                         # Increment counter by one
        originalcount += 1                                                      # Increment counter by one
    while secondcount < len(second):                                            # While the left count is still less than the right array length
        dataArray[originalcount] = second[secondcount]                          # Assign it's value to the current element in the original array
        secondcount += 1                                                        # Increment counter by one
        originalcount += 1                                                      # Increment counter by one
    return dataArray                                                            # Return the sorted array to the main function for writing.

"""
/************************************************************************
* Description: activity_selection function
* This is my greedy sort algorithm used for selecting tasks based on
* those with the latest start times.  It receives amounts and activities
* arrays from main and compares the start and finish times to find an
* optimal solution.  Returns the selection array back to main in reverse
* order (this was the only way that I could figure out how to match the example
* answers provided in the homework)
*************************************************************************/
"""

def activity_selection(amounts, activities):
    selections = []                                                             # Create an empty array that will hold our selections
    compare = 0                                                                 # Create a variable for comparison that will initially hold the first element
    selections.append(activities[compare][0])                                   # Append the first element in the array to the selections array
    for x in range (1, amounts):                                                # Loop through each element in the array start at the second element (1)
        if activities[compare][1] >= activities[x][2]:                          # If the start time in position compare is greater than the finish time of position x
            selections.insert(0, activities[x][0])                              # insert the current activity to the selections array at the beginning
            compare = x                                                         # Move variable i up to variable x's current location
    return selections                                                           # Return the selection array to main

"""
/************************************************************************
* Description: make_integers function
*************************************************************************/
"""

def make_integers(activities):
    for x in range(len(activities)):                                            # Loop through each internal list in the activities list
        for y in range (len(activities[x])):                                    # Loop through each internal list in the activities list
            activities[x][y] = map(int, activities[x][y].split(' '))            # Convert the string values into integers in the activities array

"""
/************************************************************************
* Description: readFile function
* Opens the act.txt file and reads in each line as a string in a list.
* Returns the list of strings to main.  No received variable information.
*************************************************************************/
"""

def readFile():
    with open("act.txt", "r") as dataFile:                                      # Use the open function to return a file object for act.txt.  Using read mode
        lists = dataFile.read().splitlines()                                    # Load the entire file into the object and split by lines (remove break lines)
    return lists                                                                # Return list of string from file to main function

"""
/************************************************************************
* Description: getAmounts function
* Function grabs the amounts informations from the list and stores to
* an array for later use.  Receive lists from main and returns the
* amounts arrays.
*************************************************************************/
"""

def getAmounts(lists):
    amounts = []                                                                # Create an array to store the amounts for each list of activities
    count = 0                                                                   # Create a counter variable and Initialize to 0
    while count < len(lists):                                                   # Create a while loop to navigate the lists
        amounts.append(int(lists[count]))                                       # Grab the amounts value and store in array as an integer
        count += (int(lists[count]) + 1)                                        # Increment the count varaiable by the previous amount found plus 1
    return amounts                                                              # Return the amounts array to main

"""
/************************************************************************
* Description: getActivities function
* Function uses the amounts array to gather cooresponding activities
* and stores in a list into a separate array that will eventually be
* sorted.  Receives amounts and lists array from main and returns the
* list of activities to main.
*************************************************************************/
"""

def getActivities (lists, amounts):
    activities = []                                                             # Create an array to store the lists of activities for each amount
    count = 1                                                                   # create a counter variable and Initialize to 1
    for x in range(len(amounts)):                                               # Loop through the different activity amount
        activities.append(lists[(count) : (count + amounts[x])])                # Grab sections of the list based on amounts and append to the activities array
        count += (amounts[x] + 1)                                               # Increment the counter to the next chunk of activities to be processed
    return activities                                                           # Return the activities array to main

"""
/************************************************************************
* Description: displayResults function
* Function simply displays the results from the selection array that
* was generated in the greedy selection algorithm.
*************************************************************************/
"""

def displayResults(count, selections):
    print("Set {}".format(count + 1))                                           # Display the current set number (incremented by one everytime)
    print("Number of Activities selected = {}".format(len(selections)))         # Display the total amount of activities that were selected through the greedy algorithm
    print("Activities: {}\n".format(" ".join(map(str, selections))))            # Display the activity numbers that were selected (converted from integer to string)

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
    lists = readFile()                                                          # Call function to read data from file and assign return to variable
    amounts = getAmounts(lists)                                                 # Call function to select the amount lines from the list and append to new array
    activities = getActivities(lists, amounts)                                  # Call function to select the activity lines from the list and append to new array
    make_integers(activities)
    for x in range(len(amounts)):                                               # Loop through each activity section of both arrays
        sortedList = activity_sort(amounts[x], activities[x])                   # Call function to perform sort from latest start time to earliest (in descending order)
        selections = activity_selection(amounts[x], sortedList)                 # Call function to perform selections and send the current amount and activities
        displayResults(x, selections)                                           # Call function that outputs the results to the monitor
