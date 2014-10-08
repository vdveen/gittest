#-----------------------------------------------------
#Name of script: Lab Assignment 3
#Author: Andrew van der Veen, ID 10166883
#Created: October 7th, 2014
#Purpose: To convert coordinates in a csv file from DMS
#         to the DD format and store it in a new file.
#-----------------------------------------------------

#Imports converter function from module.
from G567modules import DMStoDD

#Opens csv file.
dmsfile = open('dmscoords2.csv')
#ddfile = open('ddcoords2.csv')

#Reads information from file
dmsfile = dmsfile.read()

#Splits info from file into lines and puts into a list
dmslines = dmsfile.split('\r')
print dmslines
print len(dmslines)
print dmslines[3]

#Go through file and split individual values
for line in dmslines:
  values = line.split(',')
  print values

#for values in line:
#  values = line.split(',')
