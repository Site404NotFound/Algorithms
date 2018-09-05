#!/usr/bin/python

"""
/*********************************************************************
** Author: James Hippler (HipplerJ)
** Oregon State University
** CS 325-400 (Spring 2018)
** Analysis of Algorithms
**
** Description: Homework #1 (Problem 4)
** Due: Sunday, April 08, 2018
**
** Filename: mergesort.py
**
** Objectives:
** Implement merge sort and insertion sort to sort an array/vector of
** integers.  You may implement the algorithms in the language of your
** choice, name one program "mergesort" and the other "insertsort".
** Your programs should be able to read inputs from a file called
** "data.txt" where the first value of each line is the number of
** integers that need to be sorted, followed by the integers.
**
** Example values for data.txt:
**  4 19 2 5 11
**  8 1 2 3 4 5 6 12
** The output will be written to files called "merge.out" and
** "insert.out". For the above example the output would be:
**  2 5 11 19
**  1 1 2 2 3 4 5 6
**
** Submit a copy of all your code files and a README file that
** explains how to compile and run your code in a ZIP file to TEACH.
** We will test execution with an input file named data.txt.
*********************************************************************/
"""

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
* Description: prepArrays function
* Function prepares each string from the list by first removing any
* breaklines.  It then converts the strings into arrays.  After it
* captures the first element and uses that as the array length.  Finally
* it removes the first element and sends the arrays to the mergeSort
* function to be sorted.
*************************************************************************/
"""

def prepArrays(lists):
    lists.rstrip('\r\n')                                                        # Stip off the tailing break lines included from the file
    numberList = map(int, lists.split(' '))                                     # convert the strings to arrays by splitting each element by spaces
    numLength = numberList[0]                                                   # Assign the leading array element as the array size.
    numberList.pop(0)                                                           # Remove integer size from the array.  Leading element (0)
    return mergeSort (numberList, numLength)                                    # Return the sorted list returned from the mergeSort() function

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
    fileInfo = open('merge.out', 'w')                                           # Open file insert.out and prepare for writing
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
* Description: main function
* Program starts here and calls functions as necessary
* Calls the mergesort function that completes most of the program's
* functionality.
*************************************************************************/
"""

if __name__ == "__main__":
    lists = readFile()                                                          # Call function to read data from file and assign to variable
    fileInfo = openFile()                                                       # Call function to open file where data will be written and store object variable.
    for count in range (0, len(lists)):                                         # Loop through the list of strings returned from reading the file
        sortedArrays = prepArrays(lists[count])                                 # Call the function that takes the list of strings into a list of arrays
        sortedArrays = " ".join(map(str, sortedArrays))                         # Convert the list of arrays back into string with each element separated by a space
        if count + 1 < len(lists):                                              # If the string is not the last in the list.
            sortedArrays += "\n"                                                # Append a break line to all string except the last
        writeFile(fileInfo, sortedArrays)                                       # Call the writeFile function to write each string
    closeFile(fileInfo)                                                         # Call the function to close the writeFile
    print("Merge Sort Complete!")                                               # Let the user know the program has completed
    print("Sorted Arrays have been written to the merge.out file")              # Also let the user know the filename where the sorted arrays were stored.
