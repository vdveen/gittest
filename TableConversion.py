#-----------------------------------------------------
#Name of script: Lab Assignment 3
#Author: Andrew van der Veen, ID 10166883
#Created: October 7th, 2014
#Purpose: To convert coordinates in a csv file from DMS
#         to the DD format and store it in a new file.
#-----------------------------------------------------

#Create function
def DMStoDD(d,m = 0,s = 0):
  #The conversation
  d = float(d)
  m = float(m) / 60
  if s <> 0:
    s = float(s) / 60

  #Checking if the coordinate is negative or positive
  #and changing the outcome to reflect that
  if d <= 0:
    dms = (d - m - s)
  else:
    dms = (d + m + s)
  return dms


#Request pathnames from user
print 'Please make sure the input file is \
 in the same folder as the script and the module.'
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
  if count % 1000 == 0:
    print str(count) + ' coordinates converted'



#Show the user how many coordinates have been converted
print 'A total of ' + str(count) + \
      ' coordinates have been succesfully converted.'


#Close the in- and output files.
ddfile.close()
dmsfile.close()
