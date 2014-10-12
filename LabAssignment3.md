Lab Assignment 3
==

1. Defining the Problem
The problem is to create a function to easily convert DMS values in
comma-separated-values files (.csv) to DD and to output them in a file.

2. Design a solution
Flowchart:
See attatchment.

Pseudocode:

Create a function DMStoDD to convert both to DMS to DD:
	Convert first and second number to float
	Take first and second number and divide by 60
	If there is a third number, divide it also by 60
	Return DD value


Open csv file as input file
Create new output file
Create header for output file

Read input file
Remove first line from imput file

For each line in the file
	Split line into two and put into list
	Pass list as argument to DMStoDD
	Output latitude in latitude column in the output file
	Output longitude in longitude column in the output file

Close the input and output file

3. Write the code
See LabAssignment3.py

4. Debugging


5. Documentation
