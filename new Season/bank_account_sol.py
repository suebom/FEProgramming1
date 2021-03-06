import numpy as np
import matplotlib.pyplot as plt

def sdf_MC(r0,dr,n,p):
    m = 100000
    x = np.random.random((m,n-1))
    ud = np.where(x<p,dr,-dr)
    R = np.c_[np.zeros((m,1)),ud]
    R = r0 + R.cumsum(axis=1)
    ba = np.exp(-R.sum(axis=1)).mean()
    return ba

def sdf_Tree(r0,dr,n,p):
    x = np.ones(n)
    for i in range(n-1,-1,-1):
        R = np.arange(r0+i*dr,r0-(i+1)*dr,-2*dr)
        df = x * np.exp(-R)
        x = p*df[:-1] + (1-p)*df[1:]
        #p*x[:-1]*exp(-R[:-1]) + (1-p)*x[1:]*exp(-R[1:])
    ba = df[0]
    return ba
    
    
r0 = 0.1
dr = 0.01
p = 0.6
n = 10
    
mc = sdf_MC(r0, dr, n, p)
tree = sdf_Tree(r0, dr, n, p)

print("MC:   E[1/X] = %.6f" % mc)
print("Tree: E[1/X] = %.6f" % tree)
'''
for i in range(1,11):
    df = sdf_Tree(r0,dr,i,p)
    print(-np.log(df)/i)
'''
sdf_Tree_vec = np.vectorize(sdf_Tree)
i = np.arange(1,11)
dfs = sdf_Tree_vec(r0, dr, i, p)
R = -np.log(dfs)/i
Rstr = ["{0:.5%}".format(r) for r in R]
print(Rstr)
plt.plot(i,R,'s-')

b = np.array([100,50]).reshape((2,1))
a1 = [np.exp(0.1+0.11), np.exp(0.1+0.09)]
a1 = np.array(a1).reshape((2,1))

a1 = np.ones((2,1))*np.exp(0.1)*np.exp(
np.array([0.11,0.09])).reshape(2,1)
a2 = np.ones((2,1))*np.exp(R[1]*2)
A = np.hstack([a1,a2])

x = np.linalg.inv(A).dot(b)
price = x.sum()

price2 = (100*np.exp(
-0.11)*0.6 + 50*np.exp(-0.09)*0.4)*np.exp(-0.1)

print(price)
print(price2)










