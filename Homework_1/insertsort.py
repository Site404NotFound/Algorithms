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
** Filename: insertsort.py
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
* Description: prepArrays function
* Function prepares each string from the list by first removing any
* breaklines.  It then converts the strings into arrays.  After it
* captures the first element and uses that as the array length.  Finally
* it removes the first element and sends the arrays to the insertionSort
* function to be sorted.
*************************************************************************/
"""

def prepArrays(lists):
    lists.rstrip('\r\n')                                                        # Stip off the tailing break lines included from the file
    numberList = map(int, lists.split(' '))                                     # convert the strings to arrays by splitting each element by spaces
    numLength = numberList[0]                                                   # Assign the leading array element as the array size.
    numberList.pop(0)                                                           # Remove integer size from the array.  Leading element (0)
    return insertionSort (numberList, numLength)                                # Return the sorted list returned from the insertionSort() function

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
    fileInfo = open('insert.out', 'w')                                          # Open file insert.out and prepare for writing
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
    print("Insertion Sort Complete!")                                           # Let the user know the program has completed
    print("Sorted Arrays have been written to the insert.out file")             # Also let the user know the filename where the sorted arrays were stored.
