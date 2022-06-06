import numpy as np

def sum_total():
  n = int(raw_input())
  l = []

  for i in range(0,n):
    print i
    l.append(int(raw_input()))

  print len(np.unique(l))
sum_total()