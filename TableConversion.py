#-----------------------------------------------------
#Name of script: Lab Assignment 3
#Author: Andrew van der Veen, ID 10166883
#Created: October 7th, 2014
#Purpose: To convert coordinates in a csv file from DMS
#         to the DD format and store it in a new file.
#-----------------------------------------------------

#Imports converter function from module.
from G567modules import DMStoDD

#Request pathnames from user
print 'Please put the file in the same folder as the script.'
inputfile = raw_input('Enter the input file name: ')
outputfile = raw_input('Enter the output file name: ')

#Create new output file and add header
ddfile = open( outputfile, 'w')
ddfile.write('Longitude, Latitude')

#Opens and reads csv file.
dmsfile = open(inputfile)
dmsinfo = dmsfile.read()

#Splits info from file per line and puts into a list
dmslines = dmsinfo.split('\r')

#Removes the header line and last line through slicing
dmslines = dmslines[1:]
dmslines = dmslines[:-1]

#Counting how many lines have been succesfully converted.
count = 0

#Go through lines and convert to DD
for line in dmslines:

  #Split each line into its 6 values
  values = line.split(',')

  #Check if there are 6 values after the split
  #and parse them as arguments to function DMStoDD.
  length = len(values)
  if length == 6:

    #Chop the line in two to separate lat and lon values.
    lat = values[:3]
    lon = values[3:]

    #Parse the lon and lat into the function
    latDD = DMStoDD(lat[0], lat[1], lat[2])
    lonDD = DMStoDD(lon[0], lon[1], lon[2])

    #Write them in a new line in the output file
    coords = '\n' + str(latDD) + ',' + str(lonDD)
    ddfile.write(coords)

    #Increase count of succesful conversions by one
    count = count + 1

    #Print every ten succesful conversions
    if count % 100 == 0:
      print str(count) + ' coordinates converted'

  else:
    #If there isn't enough values given
    print 'One of your coordinates is only', length,'values long.'
    print 'Sorry, you need to have all 6 values filled in.\n' \
    'If your coordinate doesn\'t have minutes or seconds values, \n' \
    'please put the value 0 in.'

#Show the user how many coordinates have been converted
print 'A total of ' + str(count) + \
      ' coordinates have been succesfully converted.'

#Close the in- and output files.
ddfile.close()
dmsfile.close()
