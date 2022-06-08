#SUMIT SAHA
#M.SC IN DATA SCIENCE
#NEWTON RAPHSON MULTI VARIABLE WITH GRAPH


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as st
import time

def f(x,y):
    return x**3+y**3-10                 #first equation

def g(x,y):                             #second equation
    return x*(y**2)-x**2-3

def fx(x,y):                            #derivitive of first equation by x
    return 3*(x**2)

def fy(x,y):                            #derivitive of first equation by y
    return 3*(y**2)

def gx(x,y):                            #derivitive of second equation by x
    return y**2-2*x 

def gy(x,y):                            #derivitive of second equation by y
    return 2*x*y
n=int(input('ENTER NUMBER OF ITERATION: '))
x0=float(input('ENTER VALUE OF X0: '))
y0=float(input('ENTER VALUE OF Y0: '))
l=1                                      #for step

xroot=[]                                #empty list 1
yroot=[]                                #empty list 2

xroot.append(x0)                        #add initial value of x in first list
yroot.append(y0)                        #add initial value of y in second list


while(l<=n):
    X=np.array([
        [x0],
        [y0]
    ])

    J= np.array([
        [fx(x0,y0),fy(x0,y0)],
        [gx(x0,y0),gy(x0,y0)]
    ] )

    

    print('\n',l,'th jacobian matrix: \n',J)

    Jinv = np.linalg.inv(J)

    print('\n',l,'th inverse jacobian matrix: \n',Jinv)

    F= np.array([
        [f(x0,y0)],
        [g(x0,y0)]
    ])

    result= X - np.dot(Jinv,F)

    
    x0,y0=round(result[0,0],4),round(result[1,0],4)
    l=l+1
    xroot.append(x0)
    yroot.append(y0)
    

print('\nx=',x0)
print('\ny=',y0)
print(xroot)
print(yroot)

plt.title('NEWTON RAPHSON MULTI VARIABLE')          #starting matplotlib
plt.ylabel('$y$')
plt.xlabel('$x$')
plt.plot(xroot,yroot)
plt.show()

print(ending)


