bas.py

for kk in range(30):
  def all_var(tot):

    for i in range(tot):
      x1 = np.random.uniform(200, 300)
      x2 = np.random.uniform(0.1, 0.2)
      x3 = np.random.uniform(60, 90)

      sum = 0

      sum = -202.01471 + 1.28250*x1 + 3225*x2 - 0.74167*x3 - 9.4*x1*x2
      
      x1 = np.append(x1,(x2,x3, sum))
      all_variables.insert(i, x1)

    return all_variables

  def indis(S):
    sum = 0

    sum = -202.01471 + 1.28250*S[0] + 3225*S[1] - 0.74167*S[2] - 9.4*S[0]*S[1]

    return sum

  assign(4,5,3) 
  res.append(plott.f11[-1])