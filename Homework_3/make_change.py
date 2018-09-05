#!/usr/bin/python

"""
/*********************************************************************
** Author: James Hippler (HipplerJ)
** Oregon State University
** CS 325-400 (Spring 2018)
** Analysis of Algorithms
**
** Description: Homework #3 (Problem 5)
** Due: Sunday, April 22, 2018
**
** Filename: make_change.py
**
** Objectives:
** Submit a copy of all your files including the txt files and a README file
** that explains how to compile and run your code in a ZIP file to TEACH. We
** will only test execution with an input file named amount.txt.

** You may use any language you choose to implement your DP change algorithm.
** The program should read input from a file named "amount.txt". The file
** contains lists of denominations (V) followed on the next line by
** the amount A.
**
** Example amount.txt:
** 1 2 5
** 10
** 1 3 7 12
** 29
** 1 2 4 8
** 15
**
** In the above example the first line contains the denominations V=(1, 2, 5)
** and the next line contains the amount A = 10 for which we need change.
** There are three different denomination sets and amounts in the above example.
** A denomination set will be on a single line and will always start with
** the 1 "coin".
**
** The results should be written to a file named change.txt and should contain
** the denomination set, the amount A, the change result array and the minimum
** number of coins used.
**
** Example change.txt:
** 1 2 5
** 10
** 0 0 2
** 2
** 1 3 7 12
** 29
** 0 1 2 1
** 4
** 1 2 4 8
** 15
** 1 1 1 1
** 4
**
** In the above example, to make 29 cents change from the denomination
** set (1, 3, 7, 12) you need 0: 1 cent coin, 1: 3 cent coin, 2: 7 cent coins
** and 1: 12 cent coin for a total of 4 coins.
**
** EXTERNAL RESOURCES:
** 1.) Coin Changing Minimum Coins Dynamic Programming
** https://www.youtube.com/watch?v=NJuKJ8sasGk
** 2.) Change Making Problem - Dynamic Programming
** https://www.youtube.com/watch?v=rdI94aW6IWw
** 3.) Dynamic Programming | Set 7 (Coin Change)
** https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
*********************************************************************/
"""

"""
/************************************************************************
* Description: make_change function (Dynamic Programming)
* Function receives an amount (total), a list of denominations (coins),
* and a length of the list (number of coins) from main.  Returns the
* minimum number of coins required to reach the given amount, as well as,
* the combination of the coins used.  Uses bottom up dynamic programming.
* Requires two 2D arrays to capture the minimum number of coins and the
* the amount of the coins.
*************************************************************************/
"""

def make_change(amount, denominations):
    # Below is an efficient way of Establishing an array and populating with values
    # Initialize the first element of each internal array to zero and everything else to infinity (used for comparisons)
    total = [[0 if count == 0 else float("inf") for count in range(amount + 1)] # Create an array that is length of the amount that contains
        for count in range(len(denominations))]                                 # arrays that are length of the array of denominations.
    # Example: [[0, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf]]
    #

    # Need an array of arrays in order to capture each coin change and comparison made when evaluating the total array.
    coins = [[0 for count in range(len(denominations))] for count in range(amount + 1)] # Create a 2D array that will hold the number used for each coin
    # Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for dCount in range(len(denominations)):                                    # Increment through each denominations value
        for aCount in range(1, (amount + 1)):                                   # Increment from 1 to the amount value
            if aCount < denominations[dCount]:                                  # If the current amount value is less than the current denominations value
                total[dCount][aCount] = total[dCount - 1][aCount]               # Assign the value from the previous denomination in the 2D array
            else:                                                               # Otherwise...
                total[dCount][aCount] = min(total[dCount - 1][aCount],          # If we took the current denomination value
                1 + total[dCount][aCount - denominations[dCount]])              # Assign it to the current total array location
                coins[aCount] = coins[aCount - denominations[dCount]][:]        # Captures the coins as they are processed and adds them to our coins array
                coins[aCount][dCount] += 1                                      # Increment current coin value in the array based on where we are in the loop
    return (total[len(denominations) - 1][amount], coins[amount])               # Return the minimum number of coins and the coin combination

"""
/************************************************************************
* Description: getDenominations function
* Function grabs the data from every other line (odd lines).  Starts at
* element 0 in the array and increments by two.  This collects the lines
* from the amount.txt file that contain the lists of denominations.  Each
* list is appended to an array and then returned to main.
*************************************************************************/
"""

def getDenominations(lists):
    denominations = []                                                          # Establish an empty array for denominations
    for count in range (0, len(lists), 2):                                      # Work through all odd lines in the file list (Start at 0 and increments by 2)
        denominations.append(map(int, lists[count].split(' ')))                 # Convert the strings to arrays by splitting each element by spaces and append to array
    return denominations                                                        # Return the array of denominations to main

"""
/************************************************************************
* Description: getAmounts function
* Function grabs the data from every other line (even lines).  Starts at
* element 1 in the array and increments by two.  This collects the lines
* from the amount.txt file that contain the Amounts.  Each amount is
* appended to an array and then returned to main.
*************************************************************************/
"""

def getAmounts(lists):
    amounts = []                                                                # Establish an empty array for amounts
    for count in range (1, len(lists), 2):                                      # Work through all even lines in the file list (starts at one and increments by 2)
        amounts.append(int(lists[count]))                                       # Typecast element as integer and append to array
    return amounts                                                              # Return the array of amounts to main

"""
/************************************************************************
* Description: readFile function
* Opens the data.txt file and reads in each line as a string in a list.
* Returns the list of strings to main.  No received variable information.
*************************************************************************/
"""

def readFile():
    with open("amount.txt", "r") as dataFile:                                   # Use the open function to return a file object for amount.txt.  Using read mode
        lists = dataFile.readlines()                                            # Load the entire file into the object
        for count in range (0, len(lists)):
            lists[count].rstrip('\r\n')                                         # Strip off the tailing break lines included from the file
    return lists                                                                # Return list of string from file to main function

"""
/************************************************************************
* Description: openFile function
* Program opens a file for writing and return the file object
* information to the calling function.
*************************************************************************/
"""

def openFile():
    fileInfo = open('change.txt', 'w')                                          # Open file change.txt and prepare for writing
    return fileInfo                                                             # Return the file object to the calling functions (main)

"""
/************************************************************************
* Description: writeFile function
* Function received file object information and strings from main to
* write data to a file.  Returns nothing.
*************************************************************************/
"""

def writeFile(fileInfo, change):
    for count in range (0, len(change)):                                        # Loop that works through each element of the change list and write to file
        if count % 2 == 0:                                                      # If it's the first element in the change list
            convertStrings = " ".join(map(str, change[count]))                  # Convert the list of arrays back into string with each element separated by a space
        else:                                                                   # Otherwise, if it's the next two elements in the change list
            convertStrings = str(change[count])                                 # Convert the integer to a string and assin to a variable
        convertStrings += "\n"                                                  # Append a break line to all string except the last
        fileInfo.write(convertStrings)                                          # Write the passed string information to the passed file object

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
    print("Finished Making Change!")                                            # Let the user know the program has completed
    print("Change values have been written to the change.txt file")             # Also let the user know the filename where their change has been stored.

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
    lists = readFile()                                                          # Call function to read data from file and assign to variable
    fileInfo = openFile()                                                       # Call function to open file where data will be written and store object variable.
    denominations = getDenominations(lists)                                     # Call the function to grab the denominations infor an return as array
    amounts = getAmounts(lists)                                                 # Call the function to grab the amount info and return as array
    for count in range (0, len(amounts)):                                       # Breaks the arrays into pair (one list of denominations and one amount)
        change = []                                                             # Create an array that will hold the values to be written latter (Reset with each loop)
        totalCoins, coins = make_change(amounts[count], denominations[count])   # Call the function to make change, send the denominations and the amounts
        change.append(denominations[count])                                     # Append the denominations to the change list
        change.append(amounts[count])                                           # Append the total amount to the change list
        change.append(coins)                                                    # Append the the list of coin values that were used to the change list
        change.append(totalCoins)                                               # Append the total amount of coins that were used to the change list
        writeFile(fileInfo, change)                                             # Call function to write results to the "change.txt" file
    closeFile(fileInfo)                                                         # Call the function to close the writeFile
    finished()                                                                  # Call function that outputs a completion message to the monitor
