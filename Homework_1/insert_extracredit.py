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
** Filename: insert_extracredit.py
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
import random                                                                   # Import the random number generator library

"""
/************************************************************************
* Description: insertionSort function
* Functions receives a number array from main and performs an insertion
* sort to place the numbers in ascending order.  Starts with the second
* value in the array and compares to values on the left.  With each
* iteration of the loop the counter is moved forward one place in the
* array
*************************************************************************/
"""

def insertionSort (dataArray, arraySize):
    # Start loop at the second element (1) rather than the first (0)
    for count in range(1, arraySize):                                           # Increment through the array one element at a time using the array's length
        key = dataArray[count]                                                  # Set the current index to the loop counter (counter starts at 1)
        compare = count - 1                                                     # Adjusted the comparative number one element left in the array
        while compare >= 0 and key < dataArray[compare]:                        # While compare number is in range and key is less than the compare number
            dataArray[compare + 1] = dataArray[compare]                         # Swap the compare number forward (right) in the array
            compare -= 1                                                        # Move comparitive number to the next element in the array (going left toward 0)
        dataArray[compare + 1] = key                                            # No swap occurs and the key remains in place
    return dataArray                                                            # Return the sorted Array to main function

"""
/************************************************************************
* Description: main function
* Program starts here and calls functions as necessary
* Calls the mergesort function that completes most of the program's
* functionality.
*************************************************************************/
"""

if __name__ == "__main__":
    print("**** Insertion Sort Best Case *****")
    n = 1000                                                                    # Set number of variables that need to be generated
    for count in range(0, 13):
        starttime = time.time()                                                 # Collect the start time at the initial execution of the program
        if count == 1:
            n = 2000
        if count == 2:
            n = 5000
        if count == 3:
            n = 10000
        bestCase = []                                                           # Establish a new array to store the random integers
        for x in range (n):                                                     # Run through a loop for the desired number of random elements
            bestCase.append(x + 1)                                              # Append the random elements to the unsorted Array
        insertionSort(bestCase, n)                                              # Send the array to the sort function to be sorted
        print("Insertion Sort Best Case Array Size: {}".format(n))              # Output the Array size to the screen
        print("Time to Complete: {} seconds".format(time.time() - starttime))   # Output the time to complete the program.
        n += 10000

    print("\n\n**** Insertion Sort Worst Case *****")
    n = 1000                                                                    # Set number of variables that need to be generated
    for count in range(0, 13):
        starttime = time.time()                                                 # Collect the start time at the initial execution of the program
        if count == 1:
            n = 2000
        if count == 2:
            n = 5000
        if count == 3:
            n = 10000
        worstCase = []                                                          # Establish a new array to store the random integers
        arraySize = n;
        for x in range (n):                                                     # Run through a loop for the desired number of random elements
            worstCase.append(arraySize)                                         # Append the random elements to the unsorted Array
            arraySize -= 1
        insertionSort(worstCase, n)                                             # Send the array to the sort function to be sorted
        print("Insertion Sort Worst Case Array Size: {}".format(n))             # Output the Array size to the screen
        print("Time to Complete: {} seconds".format(time.time() - starttime))   # Output the time to complete the program.
        n += 10000
