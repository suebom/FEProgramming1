'''
import random

N = 1000000
s = 0
for i in range(N):
    x = random.random() *2
    y = random.random() *2
    if (x-1)**2 + (y-1)**2<=1:
        s+=1

Prob = s/N
pi = Prob * 4
print(pi)
'''
#%%
import random
import numpy as np

N = 100000
count = 0
r = np.random.random((N,2))
#x: min value
#y: max value
x1 = r.min(axis = 1)
x2 = 1 - r.max(axis=1)
x3 = r.max(axis=1) - r.min(axis=1)
x = np.vstack((x1,x2,x3))
mx = x.max(axis=0)
i = mx < 0.5
print("{0:.4%}".format(i.sum()/N))

p = r[i,0:2]
import matplotlib.pyplot as plt
plt.scatter(p[:,0],p[:,1],marker='.')
plt.show()


'''
for i in range(N):
    x = random.random()
    y = random.random()
    if x>y:
        temp = x
        x = y
        y = temp
        
    length = [x, 1-y, y-x]
    if max(length) < 0.5:
        count += 1

prob = count/N
print(prob)


#%%
import math
number = "02-769-3937"

def calcLength(number):
    d = {0:(3,1)}
    c = 0
    for i in range(3):
        for j in range(3):
            c+=1
            d[c] = (i,j)
    def distance(s,e):
        return math.sqrt((d[s][0]-d[e][0])**2 + (d[s][1]-d[e][1])**2)    
    number1 = number.replace("-","")
    n = [int(x) for x in number1]
    length = 0
    for s,e in zip(n[:-1],n[1:]):
        length += distance(s,e)    
    print(length)

calcLength(number)

for i in range(len(n)-1):
    s = n[i]
    e = n[i+1]
    length += distance(s,e)
'''










