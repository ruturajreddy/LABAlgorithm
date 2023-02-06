
  plott.f11 = f11
  plott.f21 = f21
  plott.f31 = f31
  plott.f41 = f41

  plott.f12 = f12
  plott.f13 = f13
  plott.f14 = f14
  plott.f15 = f15

  # return  plt.show()

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
    
  # global S
  # S = []
  # for x in range(1, se+1):
  #   S.insert(x, globals()['S%s' % x])

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

        # for k in range(2,ind):
        #   sum = globals()['S%s' % x][k][i] + sum
        # top = 0
        # r = 0
        # # weights(3)
        # weights(2)
        # top = S1[0][i]*w[0]
        # lead.append(top + sum/(ind-2)*w[1])
        # # lead.append(top)
 
      # ad = []
      # for a in range(di):
      #   sum = 0
      #   for k in range(2,ind):
      #     sum = globals()['S%s' % x][k][a] + sum
      #   weights(2)
      #   ad.append(globals()['S%s' % x][0][a]*w[0] + (sum/(ind-2))*w[1])

      ad = []
      for a in range(di):
        weights(1)
        ad.append(globals()['S%s' % x][0][a]*w[0])

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

    # if iter == 20:
    #   for jjj in range(1, se+1):
    #     for kkk in range(ind):
    #       for iii in range(di):
    #         ran = np.random.uniform(-65.536, 65.536)
    #         globals()['S%s' % jjj][kkk][iii] = globals()['S%s' % jjj][kkk][iii] + ran

    # if iter == 30:
    #   for jjj in range(1, se+1):
    #     for kkk in range(ind):
    #       for iii in range(di):
    #         ran = np.random.uniform(-65.536, 65.536)
    #         globals()['S%s' % jjj][kkk][iii] = globals()['S%s' % jjj][kkk][iii] + ran

    # if iter == 40:
    #   for jjj in range(1, se+1):
    #     for kkk in range(ind):
    #       for iii in range(di):
    #         ran = np.random.uniform(-65.536, 65.536)
    #         globals()['S%s' % jjj][kkk][iii] = globals()['S%s' % jjj][kkk][iii] + ran

    # if iter == 60:
    #   for jjj in range(1, se+1):
    #     for kkk in range(ind):
    #       for iii in range(di):
    #         ran = np.random.uniform(-65.536, 65.536)
    #         globals()['S%s' % jjj][kkk][iii] = globals()['S%s' % jjj][kkk][iii] + ran

    # if iter == 80:
    #   for jjj in range(1, se+1):
    #     for kkk in range(ind):
    #       for iii in range(di):
    #         ran = np.random.uniform(-65.536, 65.536)
    #         globals()['S%s' % jjj][kkk][iii] = globals()['S%s' % jjj][kkk][iii] + ran


  plott(x1,x2,x3,x4, iters,ind)

count = []