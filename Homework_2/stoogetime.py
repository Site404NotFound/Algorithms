#!/usr/bin/python

"""
/*********************************************************************
** Author: James Hippler (HipplerJ)
** Oregon State University
** CS 325-400 (Spring 2018)
** Analysis of Algorithms
**
** Description: Homework #2 (Problem 4)
** Due: Sunday, April 15, 2018
**
** Filename: stoogetime.py
**
** Objectives:
** Implement STOOGESORT from Problem 4 to sort an array/vector of integers. Implement the
** algorithm in the same language you used for the sorting algorithms in HW 1. Your program
** should be able to read inputs from a file called "data.txt" where the first value of each line is the
** number of integers that need to be sorted, followed by the integers (like in HW 1). The output
** will be written to a file called "stooge.out".
**
** Submit a copy of all your code files and a README file that
** explains how to compile and run your code in a ZIP file to TEACH.
** We will test execution with an input file named data.txt.
*********************************************************************/
"""

from math import ceil                                                           # Math library needed to perform ceil division rounding later in program
import time                                                                     # Import the time library to measure time
import random                                                                   # Import the random number generator library

"""
/************************************************************************
* Description: stoogeSort function
* Function receives a number of arrays from the main function and
* performs a recursive stooge sort (O(nlog 3 / log 1.5 ))
* The running time for this sorting algorithm is slower than both
* Merge and Insertion sort and is generally used as an example of a
* relatively inefficient and simple sort.  The name comes from the Three
* Stooges.
*
* The algorithm is defined as follows:
* - If the value at the start is larger than the value at the end, swap them.
* - If there are 3 or more elements in the list, then:
* - Stooge sort the initial 2/3 of the list
* - Stooge sort the final 2/3 of the list
* - Stooge sort the initial 2/3 of the list again
*
* It is important to get the integer sort size used in the recursive
* calls by rounding the 2/3 upwards, e.g. rounding 2/3 of 5 should
* give 4 rather than 3, as otherwise the sort can fail on certain data.
* However, if the code is written to end on a base case of size 1, rather
* than terminating on either size 1 or size 2, rounding the 2/3 of 2
* upwards gives an infinite number of calls.
*************************************************************************/
"""

def stooge(dataArray, numLength):
    firstIndex = 0                                                              # First index variable initialized to the first element in the array
    lastIndex = numLength - 1                                                   # Last Index variable initialized to the last element in the array
    if numLength <= 1:                                                          # If the array size is one or less then
        return dataArray                                                        # Just return the array since it's already sorted
    stoogeSort(dataArray, firstIndex, lastIndex)                                # Call the function to recursively sort the array segments

def stoogeSort(dataArray, firstIndex, lastIndex):
    # If the first element in the array is larger than or equal to the last element
    # And the value in the fist element is higher than the last element
    if lastIndex - firstIndex + 1 == 2 and dataArray[firstIndex] > dataArray[lastIndex]:
            # Perform the swap operation to exchange the two values in ascending order
            dataArray[lastIndex], dataArray[firstIndex] = dataArray[firstIndex], dataArray[lastIndex]

    elif lastIndex - firstIndex + 1 > 2:                                        # If the array is longer than 2 in length
        split = (int)(ceil((2 * (float)((lastIndex + 1) - firstIndex)) / 3))    # Split the array by dividing the number of elements by three (take ceiling)
        stoogeSort(dataArray, firstIndex, ((firstIndex + split) - 1))           # Sort the first 2/3 elements in the array (Recursive)
        stoogeSort(dataArray, ((lastIndex - split) + 1), lastIndex)             # Sort the last 2/3 elements in the array (Recursive)
        stoogeSort(dataArray, firstIndex, ((firstIndex + split) - 1))           # Confirm by sorting the first 2/3 elements in the array a second time (Recursive)

"""
/************************************************************************
* Description: makeArray function
* Function creates an array of random integers based on an increasing
* array size.  Sends the random array to the stooge sort function to
* be sorted.
*************************************************************************/
"""

def makeArray(n):
    randomArray = []                                                            # Establish a new array to store the random integers
    for x in range (n):                                                         # Run through a loop for the desired number of random elements
        randomArray.append(random.randint (0, 10000))                           # Append the random elements to the unsorted Array
    mergeSort(randomArray, n)                                               # Call the Stooge sort function to sort the new random array

"""
/************************************************************************
* Description: startClock function
* Function starts a clock at the beginning of the program so that we
* can automatically determine run time.  Hands the time details as a
* variable to main.
*************************************************************************/
"""

def startClock():
    startTime = time.time()                                                     # Collect the start time at the initial execution of the program
    return startTime                                                            # Return the startTime to main to be used later

"""
/************************************************************************
* Description: finished function
* Function does absolutely nothing but print a message to the console
* letting the user know that stooge sort is complete and the name
* of the output file where the sorted arrays were written. Receives
* nothing and returns nothing
*************************************************************************/
"""

def finished(startTime):
    print("Array Size: {}".format(n))                                           # Output the Array size to the screen
    print("Time to Complete: {} seconds".format(time.time() - startTime))       # Output the time to complete the program.

"""
/************************************************************************
* Description: main function
* Program starts here and calls functions as necessary
* Calls the mergesort function that completes most of the program's
* functionality.  Had to dramatically reduce the size of the arrays
* as it was taking more time to sort than the current age of our
* galaxy
*************************************************************************/
"""

if __name__ == "__main__":
    print("****** Stooge Sort Running Times ******")                            # Display message to console for what is about to happen
    n = 500                                                                     # Set number of variables that need to be generated
    for count in range(0, 10):                                                  # Run the sort several times with different array sizes
        startTime = startClock()                                                # Record the start time when the program begins execution
        makeArray(n)                                                            # Send the array to the stooge sort function to be sorted
        finished(startTime)                                                     # Display the sort time and array size to the console
        n += 500                                                                # Increment the array size by 1000
