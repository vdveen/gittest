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
