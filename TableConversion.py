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
cfile = open("dmscoords2.csv")

#Go through file and split longitude from latitude
for line in cfile:
  lines = line.split('\r')  #Create list with all lines
  values = line.split(',')
  print lines
  print len(lines)
  print values
  print len(values)
  print type(lines[2])
