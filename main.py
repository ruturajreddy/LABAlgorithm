import numpy as np
import matplotlib.pyplot as plt

from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import sin
from numpy import e
from numpy import pi
import math

def assign(sets, indi, dim):
  global di
  global se
  global ind
  global tot

  di = dim
  se = sets
  ind = indi
  total = sets*indi
  tot = total

  global all_variables

  all_variables = []

  all_variables = all_var(tot)

  all_variables.sort(key=lambda x:x[dim])

  global leaders
  leaders = all_variables[:sets]
  del all_variables[:sets]

  global advocates
  advocates = all_variables[:sets]
  del all_variables[:sets]
  
  global believers
  believers = all_variables

  for x in range(1, se+1):
    globals()['S%s' % x] = []
    globals()['S%s' % x].insert(0, leaders[0])
    del leaders[0]
    globals()['S%s' % x].insert(1, advocates[0])
    del advocates[0]

    for k in range(2,indi):
      globals()['S%s' % x].insert(k, believers[0])
      del believers[0]
    
  iters(100, S1, S2, S3, S4)


def weights(num):
  global w
  w = []
  w = np.random.random(num)
  if num > 1 :
    w /= w.sum()
    w.sort()
    w = w[::-1]


def iters(iters, S1, S2, S3, S4):

  for i in range(1,ind+1):
    globals()['x%s' % i] = []

  for iter in range(iters):
  
    for x in range(1,se+1):
      lead = []
      for i in range(di):  
        sum = 0

        for k in range(2,ind):
          sum = globals()['S%s' % x][k][i] + sum
        top = 0
        r = 0
        weights(3)
        top = S1[0][i]*w[0] + globals()['S%s' % x][1][i]*w[1]
        lead.append(top + sum/(ind-2)*w[2])

      ad = []
      for a in range(di):
        sum = 0
        for k in range(2,ind):
          sum = globals()['S%s' % x][k][a] + sum
        weights(2)
        ad.append(globals()['S%s' % x][0][a]*w[0] + (sum/(ind-2))*w[1])

      bb = []
      for jj in range(2,ind):
        ap = []
        for i in range(di):
          B = 0
          weights(2)
          r = 0
          for j in range(2):
            B = globals()['S%s' % x][j][i]*w[r] + B
            r += 1
          ap.append(B)
        bb.append(ap)
      globals()['S%s' % x] = []

      globals()['S%s' % x].append(lead)
      globals()['S%s' % x].append(ad)
      for i in range(len(bb)):
        globals()['S%s' % x].append(bb[i])

      for i in range(ind):
        sum = indis(globals()['S%s' % x][i])

        globals()['S%s' % x][i].append(sum)
        globals()['x%s' % x].append(sum)
      globals()['S%s' % x].sort(key=lambda x:x[di])

      
    tmp = 0
    for x in range(1,se+1):
      if (S1[0][di]) > (globals()['S%s' % x][0][di]):
        tmp = S1
        S1 = globals()['S%s' % x]
        globals()['S%s' % x] = tmp

  plott(x1,x2,x3,x4, iters,ind)

count = []
