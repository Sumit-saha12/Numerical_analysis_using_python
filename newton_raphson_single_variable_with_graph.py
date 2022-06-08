#SUMIT SAHA
#M.SC IN DATA SCIENCE
#NEWTON RAPHSON SINGLE VARIABLE WITH GRAPH


import numpy as np
import matplotlib.pyplot as plt

from logging import root


def equation(x):                    #x**3-9x+1(equation)
    a = (x * x * x) - (9 * x) + 1
    return a

def dequation(x):                  #3x**2-9(derivitive of equ.)
    a = 3*x*x - 9
    return a

x= int(input('ENTER LOWER LIMIT: '))   
y= int(input('ENTER UPPER LIMIT: '))
root = []                           #empty list
print('LOWER LIMIT',x)
print('UPPER LIMIT',y)

l = 1
       #initial_value

delta = 1

print('steps         x            fx1           fx2                h               xn')
while delta >= 0.00000000000000001:            #upto decimal value
    
    fx1 = equation(x)
    fx2 = dequation(x)  
    h= -(fx1/fx2)
    xn=h+x
    root.append(xn)
    print(" ",round(l,2),"     ",format(x,".5f"),"    ", format(fx1,".5f"),"       ",format(fx2,".5f"),"       ", format(h,".5f"),"        ",format(xn,".5f"))
    
    delta = abs(xn - x)
    l = l + 1
    x = xn
print('the root is xn1=', xn)


plt.title('NEWTON RAPHSON SINGLE VARIABLE')         #matplotlib start
plt.ylabel('$y$')
plt.xlabel('$x$')
plt.plot(root)
plt.show()
