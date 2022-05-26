#bisection_method
def equation(x):
    a = (x * x * x) - (9 * x) + 1
    return a
i=int(input('Enter lower limit:'))

l = 1
xn = 0       #initial_value
xn1 = 0      #new_value
delta = 1
a=-1.0      #negative_value
b=-1.0      #positive_value

while(a==-1.0 or b==-1.0):    #until find root
    print(a, b)
    k = equation(i)
    print(k)
    if k< 0.00:
        a = i
    elif k>0.00:
        b=i
    i=i+1

if(a<b):
    print('Lower limit is: ',a)
    print('Upper limit is: ',b)
else:
    print('Lower limit is: ',b)
    print('Upper limit is: ',a)

print('steps         a<0        b>0         xn1=(a+b)/2          f(xn1)\n')
while delta >= 0.001:
    xn = xn1
    xn1 = (a + b) / 2    #middle value
    k = equation(xn1)
    print(" ",round(l,2),"     ",format(a,".5f"),"    ", format(b,".5f"),"       ",format(xn1,".5f"),"       ", format(k,".5f"))
    if k < 0:
        a = xn1
    elif k > 0:
        b = xn1
    delta = abs(xn1 - xn)
    l = l + 1

print('the root is xn1=', xn1)