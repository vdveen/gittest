def DMStoDD(d,m,s = 0):
  d = float(d)
  m = float(m) / 60
  if s <> 0:
    s = float(s) / 60
  dms = (d + m + s)
  return dms
