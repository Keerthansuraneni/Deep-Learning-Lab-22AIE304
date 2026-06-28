import numpy as np

X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([0,0,0,1])
w=np.zeros(2); b=0; lr=0.1
def step(z): return 1 if z>=0 else 0
for _ in range(10):
    for i in range(len(X)):
        pred=step(np.dot(X[i],w)+b)
        err=y[i]-pred
        w+=lr*err*X[i]
        b+=lr*err
print("Weights:",w,"Bias:",b)
