def optimalBST(p, n):
 e=[[0 for x in range(n)] for x in range(n)] 
 w=[[0 for x in range(n)] for x in range(n)] 
 root=[[0 for x in range(n)] for x in range(n)] 
 for i in range(0, n-1):
   e[i+1][i] = 0
   e[i][i] = p[i]
   root[i][i] = i # like a diagonal
   w[i][i] = p[i]
 e[n-1][n-1] = p[n-1]
 w[n-1][n-1] = p[n-1] 
 root[n-1][n-1] = n-1 #e is the expected count 
 for i in range(2, n+1): # diaglonal count 
   for l in range(0, n-i+1):
     j = i + l - 1
     minval = 99999 # a high minimum value 
     w[l][j] = w[l][j-1] + p[j] 
     for r in range(l+1, j):
       t = e[l][r - 1] + e[r + 1][j] + w[l][j]
       if (t < minval):
         minval = t
         rmin = r
     if(e[l+1][j] + w[l][j] < minval):
      minval = e[l+1][j] + w[l][j]
      rmin = l
     if(e[l][j-1] + w[l][j] < minval):
      minval = e[l][j-1] + w[l][j]
      rmin = j
     root[l][j] = rmin
     e[l][j] = minval
 return(root)
 #print e
 #print w
 #print root
'''
def constructBST(root):
  i = 0
  r = root[i][n-1]
  print root[i][n-1]
  print root[i][r-1]
  r2 = root[r][n-1]
  print root[r][n-1]
  print root[r2][n-1]
  print[r+1][r2]
'''
def constructrcrs(root, i, j):
  if (j - i) <= 0:
    return root[i][j]
  
  r = root[i][j-1]
  left = constructrcrs(root, i, r-1)
  right = constructrcrs(root, r+1, j)

  print "Root: {} | Left:{} | Right:{}".format(r, left, right)
  return r



p = [.25, .2, .05, .2, .3]
n = 5

root = optimalBST(p, n)
#constructBST(root)
#print root[2][4]
constructrcrs(root, 0, n-1)