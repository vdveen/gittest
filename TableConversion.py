#-----------------------------------------------------
#Name of script: Lab Assignment 3
#Author: Andrew van der Veen, ID 10166883
#Created: October 7th, 2014
#Purpose: To convert coordinates in a csv file from DMS
#         to the DD format and store it in a new file.
#-----------------------------------------------------

cfile = open("/Users/asvdveen/Documents/Github/gittest/dmscoords.csv", 'r')
print cfile
print type(cfile)
coords = cfile.readline()
print type(coords)
values = coords.split(',')
print values
