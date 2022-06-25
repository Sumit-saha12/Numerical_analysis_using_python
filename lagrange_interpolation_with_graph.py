from matplotlib import pyplot as plt


x=[]
y=[]
n=int(input('ENTER NUMBER OF DATA: '))

for i in range(n):
    x.append(int(input('Enter x value: ')))
    y.append(float(input('Enter y  value: ')))

xp=int(input('Enter search value: '))
yp=0
for i in range(n):
    p=1
    for j in range(n):
        if(i!=j):
            p=p*((xp-x[j])/(x[i]-x[j]))

    yp=yp+p*y[i] 

print('the value of',xp,'is:',yp)

plt.plot(x,y,label='x,y')
plt.scatter(xp,yp,label='f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('LANGRANGE INTERPOLATION FORMULA')
plt.legend()
plt.show()