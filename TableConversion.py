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

#Removes the first line through slicing
dmslines = dmslines[1:]

#Go through file and split individual values
for line in dmslines:
  values = line.split(',')

  #Chop the line in two to separate lat and lon values
  length = len(values)
  halfway = length / 2
  lat = values[:halfway]
  lon = values[halfway:]

  #Parse latitude into function DMStoDD based on its length
  if length == 6:
    latDD = DMStoDD(lat[0], lat[1], lat[2])
    lonDD = DMStoDD(lon[0], lon[1], lon[2])
  elif length == 4:
    latDD = DMStoDD(lat[0], lat[1])
    lonDD = DMStoDD(lon[0], lon[1])
  elif length == 2:
    latDD = DMStoDD(lat[0])
    lonDD = DMStoDD(lon[0])
  else:
    print 'Sorry, your latitude and longitude need to \
    be of the same precision level! Input is either \
    both DMS, DMS or both DM, DM or both D,D'

  print latDD, lonDD
#print latDD
