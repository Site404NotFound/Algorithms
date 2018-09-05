# CS325_FinalProject_Group2
CS 325 Analysis of Algorithms Final Project

Authors:
* Caitlin Dudley (dudleyca@oregonstate.edu)
* James Hippler (hipplerj@oregonstate.edu)
* Kyle Martinez (martink9@oregonstate.edu)

Oregon State University
CS 325-400 (Spring 2018)
Analysis of Algorithms

Project Group 2
Description: Final Project (Travelling Salesman Problem)
Due: Friday, June 08, 2018

- For Example 1 (tsp_example_1.txt) please use -t option
- For Example 2 & 3 (tsp_example_2.txt & tsp_example_3.txt) please use -c option
- For All competition files please use -c option.

Program takes three arguments.
1. Argument 1 is the name of the program (CS325_Project_Group2.py)
2. Argument 2 is the name of the file with the TSP information
3. Argument 3 is the mode in which the program will operate.  There is a testing
mode and a competition mode.  Both modes are explained below.

There are two mode for this program.
-c: Used for competition.  Program will work toward optimal solution but will
    terminate after 3 minutes and return the current best solution.  The
    responses in this mode are less accurate but adhere to the time limit for
    the competition.

-t: Used for testing.  Program will work toward optimal solution.  This mode
    does not adhere to the three minute timer, but will return more accurate
    solutions.  This option will take considerable time to generate results.

EXECUTION INSTRUCTION
$ python CS325_Project_Group2.py <file_name> <mode_switch>

EXAMPLE
$ python CS325_Project_Group2.py tsp_example_1.txt -t

alternatively you can make the program executable and run as follows..
$ chmod +x CS325_Project_Group2.py
$ ./CS325_Project_Group2.py <file_name> <mode_switch>
