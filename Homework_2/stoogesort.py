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
** Filename: stoogesort.py
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
    return dataArray                                                            # Return the sorted array information to the calling function (prepArrays)

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
    return dataArray                                                            # Return the sorted array information to the calling function (stooge)

"""
/************************************************************************
* Description: prepArrays function
* Function prepares each string from the list by first removing any
* breaklines.  It then converts the strings into arrays.  After it
* captures the first element and uses that as the array length.  Finally
* it removes the first element and sends the arrays to the stoogeSort
* function to be sorted.
*************************************************************************/
"""

def prepArrays(lists):
    lists.rstrip('\r\n')                                                        # Stip off the tailing break lines included from the file
    numberList = map(int, lists.split(' '))                                     # convert the strings to arrays by splitting each element by spaces
    numLength = numberList[0]                                                   # Assign the leading array element as the array size.
    numberList.pop(0)                                                           # Remove integer size from the array.  Leading element (0)
    return stooge(numberList, numLength)                                        # Return the sorted list returned from the stoogeSort() function

"""
/************************************************************************
* Description: convertStringAndWrite function
* This function converts the list of array objects back into strings
* and then writes those strings to the stooge.out file.  Receives
* the list of arrays from main.  No returns
*************************************************************************/
"""

def convertStringAndWrite(lists):
    for count in range (0, len(lists)):                                         # Loop through the list of strings returned from reading the file
        sortedArrays = prepArrays(lists[count])                                 # Call the function that takes the list of strings into a list of arrays
        sortedArrays = " ".join(map(str, sortedArrays))                         # Convert the list of arrays back into string with each element separated by a space
        sortedArrays += "\n"                                                    # Append a break line to all string except the last
        writeFile(fileInfo, sortedArrays)                                       # Call the writeFile function to write each string
"""
/************************************************************************
* Description: readFile function
* Opens the data.txt file and reads in each line as a string in a list.
* Returns the list of strings to main.  No received variable information.
*************************************************************************/
"""

def readFile():
    with open("data.txt", "r") as dataFile:                                     # Use the open function to return a file object for data.txt.  Using read mode
        lists = dataFile.readlines()                                            # Load the entire file into the object
    return lists                                                                # Return list of string from file to main function

"""
/************************************************************************
* Description: openFile function
* Program opens a file for writing and return the file object
* information to the calling function.
*************************************************************************/
"""

def openFile():
    fileInfo = open('stooge.out', 'w')                                          # Open file insert.out and prepare for writing
    return fileInfo                                                             # Return the file object to the calling functions (main)

"""
/************************************************************************
* Description: writeFile function
* Function received file object information and strings from main to
* write data to a file.  Returns nothing.
*************************************************************************/
"""

def writeFile(fileInfo, lists):
    fileInfo.write(lists)                                                       # Write the passed string information to the passed file object

"""
/************************************************************************
* Description: closeFile function
* Close the writing file once the program has finished storing
* all sorted arrays.  Returns nothing and received the open file
* object information.
*************************************************************************/
"""

def closeFile(fileInfo):
    fileInfo.close()                                                            # Close the open thread to file object.

"""
/************************************************************************
* Description: finished function
* Function does absolutely nothing but print a message to the console
* letting the user know that stooge sort is complete and the name
* of the output file where the sorted arrays were written. Receives
* nothing and returns nothing
*************************************************************************/
"""

def finished():
    print("Stooge Sort Complete!")                                              # Let the user know the program has completed
    print("Sorted Arrays have been written to the stooge.out file")             # Also let the user know the filename where the sorted arrays were stored.

"""
/************************************************************************
* Description: main function
* Program starts here and calls functions as necessary
* Calls the mergesort function that completes most of the program's
* functionality.
*************************************************************************/
"""

if __name__ == "__main__":
    lists = readFile()                                                          # Call function to read data from file and assign to variable
    fileInfo = openFile()                                                       # Call function to open file where data will be written and store object variable.
    convertStringAndWrite(lists)                                                # Call function to convert list of arrays back to strings and write to file
    closeFile(fileInfo)                                                         # Call the function to close the writeFile
    finished()                                                                  # Call function that outputs a completion message to the monitor
