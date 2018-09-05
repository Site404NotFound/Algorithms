#!/usr/bin/python

"""
/*********************************************************************
** Author: James Hippler (HipplerJ)
** Oregon State University
** CS 325-400 (Spring 2018)
** Analysis of Algorithms
**
** Description: Homework #1 (Extra Credit)
** Due: Sunday, April 08, 2018
**
** Filename: merge_extracredit.py
**
** EXTRA CREDIT:
** A Tale of Two Algorithms: It was the best of times, it was the worst of times...
** Generate best case and worst case inputs for the two algorithms and repeat
** the analysis in parts b) to e) above. To receive credit you must discuss how
** you generated your inputs and your results. Submit your code to TEACH in a zip file with the code from Problem 4.
**
** Merge Sort vs Insertion Sort Running time analysis
** The goal of this problem is to compare the experimental running times of the two sorting algorithms.
**
** a.  Now that you have proven that your code runs correctly using the data.txt input file, you can modify
** the code to collect running time data.  Instead of reading arrays from a file to sort, you will now generate
** arrays of size n containing random integer values from 0 to 10,000 and then time how long it takes to sort the arrays.
** We will not be executing the code that generates the running time data so it does not have to be submitted to
** TEACH or even execute on flip.  Include a "text" copy of the modified code in the written HW submitted in Canvas.
**
** b.  Use the system clock to record the running times of each algorithm for n = 1000, 2000, 5000, 10,000, ... You may need
** to modify the values of n if an algorithm runs too fast or too slow to collect the running time data.   If you program
** in C your algorithm will run faster than if you use python.  You will need at least seven values of t (time) greater
** than 0.  If there is a variability in the times between runs of the same algorithm you may want to take the average
** time of several runs for each value of n.
**
** c.  For each algorithm plot the running time data you collected on an individual graph with n on the x-axis and time on
** the y-axis. You may use Excel, Matlab, R or any other software. Also plot the data from both algorithms together on a
** combined graph. Which graphs represent the data best?
**
** d.  What type of curve best fits each data set? Again, you can use Excel, Matlab, any software or a graphing calculator
** to calculate a regression equation. Give the equation of the curve that best "fits" the data and draw that curve on the
** graphs of created in part c).
**
** e.  How do your experimental running times compare to the theoretical running times of the algorithms? Remember, the
**  experimental running times were "average case" since the input arrays contained random integers.
*********************************************************************/
"""

import time                                                                     # Import the time library to measure time

"""
/************************************************************************
* Description: mergeSort function
* Functions receives a number array from main and performs a merge sort
* to place the numbers in ascending order.  The function takes and array
* and recursively devides until until it reaches array sizes of one.
* It passes data to a merge function that combines the elements in
* ascending order into the original array
*************************************************************************/
"""

def mergeSort (dataArray, arraySize):
    if arraySize < 1:                                                           # If Array Size is less than 1, this is invalid
        print("Array Size {} is invalid".format(arraySize))                     # print an error to the console
    elif arraySize == 1:                                                        # If the array size is one it's already sorted
        return dataArray                                                        # Return the array as is without performing any work
    else:                                                                       # If the array is greater than size one (less than one and already sorted)
        first = dataArray[:(arraySize // 2)]                                    # Split the array and assign the left (bottom) half to variable (Use Floor Division)
        last = dataArray[(arraySize // 2):]                                     # Split the array and assign the right (top) half to variable (Use Floor Division)
        firstLength = len(first)                                                # Get left array length and assign to variable
        lastLength = len(last)                                                  # Get left array length and assign to variable
        firstArray = mergeSort(first, firstLength)                              # Recursively call the mergeSort function and send the first half of the array
        secondArray =mergeSort(last, lastLength)                                # Recursively call the mergeSort function and send the second half of the array
    return merge (dataArray, firstArray, secondArray)


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
        if first[firstcount] < second[secondcount]:                             # If the left array is less than the right
            dataArray[originalcount]=first[firstcount]                          # Assign it to the current element in the original array
            firstcount += 1                                                     # Increment left array counter by one (hate that python can't just do ++)
        else:                                                                   # otherwise if the right array element is smaller
            dataArray[originalcount]=second[secondcount]                        # Assign it to the current element in the original array
            secondcount += 1                                                    # Increment Right array counter by one
        originalcount += 1                                                      # Increment original array counter by one
    while firstcount < len(first):                                              # If the first count is still less than the left array length
        dataArray[originalcount]=first[firstcount]                              # assign the current element from the left array to the current element in the original array
        firstcount += 1                                                         # Increment counter by one
        originalcount += 1                                                      # Increment counter by one
    while secondcount < len(second):                                            # While the left count is still less than the right array length
        dataArray[originalcount]=second[secondcount]                            # Assign it's value to the current element in the original array
        secondcount += 1                                                        # Increment counter by one
        originalcount += 1                                                      # Increment counter by one
    return dataArray                                                            # Return the sorted array to the main function for writing.


"""
/************************************************************************
* Description: bestCase function
* Receives an array size from n and creates a sorted integer array
* (ascending) and calls merge sort to sort.
*************************************************************************/
"""

def bestCase (n):
    bestCase = []                                                               # Establish a new array to store the random integers
    for x in range (n):                                                         # Run through a loop for the desired number of random elements
        bestCase.append(x + 1)                                                  # Append the random elements to the unsorted Array
    mergeSort(bestCase, n)                                                      # Send the array to the sort function to be sorted
    print("Merge Sort Best Case Array Size: {}".format(n))                      # Output the Array size to the screen

"""
/************************************************************************
* Description: worstCase function
* Receives an array size from n and creates a worst case scenario
* for merge sort to process (forces a maximum number of comparisons).
* Accomplishes this assigning odd number to the first half of the array
* and even numbers to the second half
*************************************************************************/
"""

def worstCase(n):
    worstleft = []
    worstright = []                                                             # Establish a new array to store the random integers
    for x in range (n):                                                         # Run through a loop for the desired number of random elements
        if x % 2 == 0:
            worstleft.append(x + 1)
        else:
            worstright.append(x + 1)                                            # Append the random elements to the unsorted Array
    completeWorst = worstleft + worstright
    mergeSort(completeWorst, n)                                                 # Send the array to the sort function to be sorted
    print("Merge Sort Worst Case Array Size: {}".format(n))                     # Output the Array size to the screen

"""
/************************************************************************
* Description: main function
* Program starts here and calls functions as necessary
* Calls the mergesort function that completes most of the program's
* functionality.
*************************************************************************/
"""

if __name__ == "__main__":
    print("**** Merge Sort Best Case *****")
    n = 1000                                                                    # Set number of variables that need to be generated
    for count in range(0, 13):
        starttime = time.time()                                                 # Collect the start time at the initial execution of the program
        if count == 1:
            n = 2000
        if count == 2:
            n = 5000
        if count == 3:
            n = 10000
        bestCase(n)
        print("Time to Complete: {} seconds".format(time.time() - starttime))   # Output the time to complete the program.
        n += 10000

    print("\n\n**** Merge Sort Worst Case *****")
    n = 1000                                                                    # Set number of variables that need to be generated
    for count in range(0, 13):
        starttime = time.time()                                                 # Collect the start time at the initial execution of the program
        if count == 1:
            n = 2000
        if count == 2:
            n = 5000
        if count == 3:
            n = 10000
        worstCase(n)
        print("Time to Complete: {} seconds".format(time.time() - starttime))   # Output the time to complete the program.
        n += 10000
