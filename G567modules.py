def DMStoDD(d,m = 0,s = 0):
  d = float(d)
  if s <> 0:
    m = float(m) / 60
  if s <> 0:
    s = float(s) / 60
  dms = (d + m + s)
  return dms
