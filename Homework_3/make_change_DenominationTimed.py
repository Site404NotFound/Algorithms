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
** Filename: making_change.py
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

import time                                                                     # Import the time library to measure time

"""
/************************************************************************
* Description: make_change Dynamic Programming function
* Function receives an amount (total), a list of denominations (coins),
* and a length of the list (number of coins) from main.  Returns the
* minimum number of coins required to reach the given amount, as well as,
* the combination of the coins used.  Uses bottom up dynamic programming.
*************************************************************************/
"""

def make_change(amount, denominations):
    # Below is an efficient way of Establishing an array and populating with values
    total = [[0 if count == 0 else float("inf") for count in range(amount + 1)] # Create an array that is length of the amount that contains
        for count in range(len(denominations))]                                 # arrays that are length of the array of denominations.
    # Example: [[0, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf], [0, inf, inf, inf, inf, inf]]

    coins = [[0 for x in range(len(denominations))] for x in range(amount + 1)] # Create an array that will hold the number used for each coin
    # Example: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for dCount in range(len(denominations)):                                    # Increment through each denominations value
        for aCount in range(1, (amount + 1)):                                   # Increment from 1 to the amount value
            if aCount < denominations[dCount]:                                  # If the current amount value is less than the current denominations value
                total[dCount][aCount] = total[dCount - 1][aCount]               # Assign the value from the previous element in the 2D array
            else:                                                               # Otherwise...
                total[dCount][aCount] = min(total[dCount - 1][aCount],          # If we took the current denomination value
                1 + total[dCount][aCount - denominations[dCount]])              # Assign it to the current total array location
                coins[aCount] = coins[aCount - denominations[dCount]][:]        # Copy coins value back to table to store while we continue looping
                coins[aCount][dCount] += 1                                      # Increment the total for the coin that was just used.
    return (total[len(denominations) - 1][amount], coins[amount])               # Return the minimum number of coins and the coin combination

"""
/************************************************************************
* Description: finished function
* Function does absolutely nothing but print a message to the console
* letting the user know that stooge sort is complete and the name
* of the output file where the sorted arrays were written. Receives
* nothing and returns nothing
*************************************************************************/
"""

def finished(startTime, denominations):
    print("Denominations: {}".format(len(denominations)))                       # Output the denominations length to the screen
    print("Time to Complete: {} seconds".format(time.time() - startTime))       # Output the time to complete the program.

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
* Description: main function
* Program starts here and calls functions as necessary
* Calls the make_change function that completes most of the program's
* functionality.  Also manages the functions that read & write data
* from files.
*************************************************************************/
"""

if __name__ == "__main__":
    amounts = 10                                                                # Create array variable for amounts
    n = 10000                                                                   # Set a value to increase the incrementing value of denominations
    for count in range (10):                                                    # Breaks the arrays into pair (one list of denominations and one amount)
        startTime = startClock()                                                # Record the start time when the program begins execution
        denominations = range(n)                                                # Create variable for denominations (used standard USD coins)
        change = []                                                             # Create an array that will hold the values to be written latter (Reset with each loop)
        totalCoins, coins = make_change(amounts, denominations)                 # Call the function to make change, send the denominations and the amounts
        change.append(denominations)                                            # Append the denominations to the change list
        change.append(amounts)                                                  # Append the total amount to the change list
        change.append(coins)                                                    # Append the the list of coin values that were used to the change list
        change.append(totalCoins)                                               # Append the total amount of coins that were used to the change list
        finished(startTime, denominations)                                      # Call function that outputs a completion message to the monitor
        n += 10000                                                              # Increment the amount of denominations
