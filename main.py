import numpy as np
import matplotlib.pyplot as plt

from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import sin
from numpy import e
from numpy import pi
import math

def plott(x1,x2,x3,x4, iters,ind):

  f11 = []; f12 = []; f13 = []; f14 = [];f15 = [];

  for i in np.arange(0, iters*ind, ind):
    f11.append(x1[i])

  for i in np.arange(1, iters*ind, ind):
    f12.append(x1[i])

  for i in np.arange(2, iters*ind, ind):
    f13.append(x1[i])

  for i in np.arange(3, iters*ind, ind):
    f14.append(x1[i])

  for i in np.arange(4, iters*ind, ind):
    f15.append(x1[i])

  f21 = []; f22 = []; f23 = []; f24 = [];f25 = [];

  for i in np.arange(0, iters*ind, ind):
    f21.append(x2[i])

  for i in np.arange(1, iters*ind, ind):
    f22.append(x2[i])

  for i in np.arange(2, iters*ind, ind):
    f23.append(x2[i])

  for i in np.arange(3, iters*ind, ind):
    f24.append(x2[i])

  for i in np.arange(4, iters*ind, ind):
    f25.append(x2[i])

  f31 = []; f32 = []; f33 = []; f34 = [];f35 = [];

  for i in np.arange(0, iters*ind, ind):
    f31.append(x3[i])

  for i in np.arange(1, iters*ind, ind):
    f32.append(x3[i])

  for i in np.arange(2, iters*ind, ind):
    f33.append(x3[i])

  for i in np.arange(3, iters*ind, ind):
    f34.append(x3[i])

  for i in np.arange(4, iters*ind, ind):
    f35.append(x3[i])

  f41 = []; f42 = []; f43 = []; f44 = [];f45 = [];

  for i in np.arange(0, iters*ind, ind):
    f41.append(x4[i])

  for i in np.arange(1, iters*ind, ind):
    f42.append(x4[i])

  for i in np.arange(2, iters*ind, ind):
    f43.append(x4[i])

  for i in np.arange(3, iters*ind, ind):
    f44.append(x4[i])

  for i in np.arange(4, iters*ind, ind):
    f45.append(x4[i])

  y = []
  for i in range(len(f11)):
    y.append(i)

  fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(1, 4, figsize=(27,10))

  # fig.suptitle('All 50 Iterations')

  ax1.set_title('Leader 1')
  ax1.plot(y, f11,linewidth=1)
  ax1.scatter(y, f11, s=20,  marker='*')

  ax1.plot(y, f12, 'tab:orange')
  ax1.scatter(y, f12, s=10, color='orange', marker='^')

  ax1.plot(y, f13, 'tab:green')
  ax1.scatter(y, f13, s=10, color='green')

  ax1.plot(y, f14, 'tab:red')
  ax1.scatter(y, f14, s=10, color='red')

  ax1.plot(y, f15, 'tab:purple')
  ax1.scatter(y, f15, s=10, color='purple')
  ax1.grid()


  ax2.set_title('Leader 2')
  ax2.plot(y, f21,linewidth=1)
  ax2.scatter(y, f21, s=10,  marker='*')

  ax2.plot(y, f22, 'tab:orange')
  ax2.scatter(y, f22, s=10, color='orange',  marker='^')

  ax2.plot(y, f23, 'tab:green')
  ax2.scatter(y, f23, s=10, color='green')

  ax2.plot(y, f24, 'tab:red')
  ax2.scatter(y, f24, s=10, color='red')

  ax2.plot(y, f25, 'tab:purple')
  ax2.scatter(y, f25, s=10, color='purple')
  ax2.grid()


  ax3.set_title('Leader 3')
  ax3.plot(y, f31,linewidth=1)
  ax3.scatter(y, f31, s=10,  marker='*')

  ax3.plot(y, f32, 'tab:orange')
  ax3.scatter(y, f32, s=10, color='orange',  marker='^')

  ax3.plot(y, f33, 'tab:green')
  ax3.scatter(y, f33, s=10, color='green')

  ax3.plot(y, f34, 'tab:red')
  ax3.scatter(y, f34, s=10, color='red')

  ax3.plot(y, f35, 'tab:purple')
  ax3.scatter(y, f35, s=10, color='purple')
  ax3.grid()


  ax4.set_title('Leader 4')
  ax4.plot(y, f41,linewidth=1)
  ax4.scatter(y, f41, s=10,  marker='*')

  ax4.plot(y, f42, 'tab:orange')
  ax4.scatter(y, f42, s=10, color='orange',  marker='^')

  ax4.plot(y, f43, 'tab:green')
  ax4.scatter(y, f43, s=10, color='green')

  ax4.plot(y, f44, 'tab:red')
  ax4.scatter(y, f44, s=10, color='red')

  ax4.plot(y, f45, 'tab:purple')
  ax4.scatter(y, f45, s=10, color='purple')
  ax4.grid()

  plott.f11 = f11
  plott.f21 = f21
  plott.f31 = f31
  plott.f41 = f41

  plott.f12 = f12
  plott.f13 = f13
  plott.f14 = f14
  plott.f15 = f15

  return  plt.show()

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
