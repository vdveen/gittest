#-----------------------------------------------------
#Name of script: Lab Assignment 3
#Author: Andrew van der Veen, ID 10166883
#Created: October 7th, 2014
#Purpose: To convert coordinates in a csv file from DMS
#         to the DD format and store it in a new file.
#-----------------------------------------------------

#Opens csv file.
cfile = open("/Users/asvdveen/Documents/Github/gittest/dmscoords2.csv", 'r')

#Puts all lines in a single list
coords = cfile.readlines()

#Separates coords per line
lines = str(coords).split('\\r')

#Imports converter function from module.
from G567modules import DMStoDD

#Go through list and convert
for line in lines:
  print line
#humm
