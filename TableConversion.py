#-----------------------------------------------------
#Name of script: Lab Assignment 3
#Author: Andrew van der Veen, ID 10166883
#Created: October 7th, 2014
#Purpose: To convert coordinates in a csv file from DMS
#         to the DD format and store it in a new file.
#-----------------------------------------------------

#Imports converter function from module.
from G567modules import DMStoDD

#Create new output file and add header
ddfile = open('ddcoords2.csv', 'w')
ddfile.write('Longitude, Latitude')

#Opens and reads csv file.
dmsfile = open('dmscoords2.csv')
dmsfile = dmsfile.read()

#Splits info from file per line and puts into a list
dmslines = dmsfile.split('\r')

#Removes the header line and last line through slicing
dmslines = dmslines[1:]
dmslines = dmslines[:-1]

#Go through file and split individual values
for line in dmslines:
  values = line.split(',')

  #Chop the line in two to separate lat and lon values.
  length = len(values)
  halfway = length / 2
  lat = values[:halfway]
  lon = values[halfway:]

  #Parse coordinates into function DMStoDD.
  if length == 6:
    #This converts line input to DD if degrees,
    #minutes and seconds are given.
    latDD = DMStoDD(lat[0], lat[1], lat[2])
    lonDD = DMStoDD(lon[0], lon[1], lon[2])
    print latDD, lonDD

  elif length == 4:
    #This converts line input to DD if degrees & minutes are given
    latDD = DMStoDD(lat[0], lat[1])
    lonDD = DMStoDD(lon[0], lon[1])
    print latDD, lonDD

  elif length == 2:
    #This converts line input to DD if only degrees are given
    latDD = float(lat[0])
    lonDD = float(lon[0])
    print latDD, lonDD

  else:
    #The only downside to chopping lists in half is that
    #you can't have lat as DMS and lon as DM, for example.
    #Hence why the above if statement uses multiples of 2.
    print 'Your coordinate is only', length,'value long.'
    print 'Sorry, the lat. and lon. need to have\n' \
    'the same amount of values for this to \n' \
    'work.'
