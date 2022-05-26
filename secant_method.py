

#Secant method

def equation(x):
    a = (x * x * x) - (9 * x) + 1
    return a


l = 1
Xa=2        #initial value      
Xb = -1     #new value
delta = 1
i=2

while(Xb==-1.0):    #until find root
    
    k = equation(i)
    if(k>0):
      Xb=i
      break
    i=i+1



print('Initial value',Xa)
print('New value',Xb)    



print('steps       Xa           Xb            Xc             f(Xc)\n')
while delta >= 0.01:
    k1=equation(Xa)
    k2=equation(Xb)
    Xc=Xb-((k2*(Xb-Xa))/(k2-k1))   #middle value
    k3 = equation(Xc)
    print(" ",round(l,2),"     ",format(Xa,".5f"),"    ", format(Xb,".5f"),"       ",format(Xc,".5f"),"       ", format(k3,".5f"))
    delta = abs(Xc - Xb)
    l = l + 1
    Xa=Xb
    Xb=Xc

print('the root is Xc=', Xc)

