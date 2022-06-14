from math import factorial
from matplotlib import pyplot as plt, style as st                 #import library


h=int(input('Enter gap value:'))                      #every x values gap
x=list(range(1,9,h))                           
n=(len(x))



# n=int(input('Enter the number of x:'))               {
# x=[0 for i in range(n)]
#                                                        user input x values
# for i in range(0,n):
#     x[i]=float(input('Enter x values: '))

# h=x[1]-x[0]                                           }
                                      

                                      

y = [[0 for i in range(n)]                            # y empty list
        for j in range(n)]




for i in range(0,n):           
    y[i][0]=int(input('Enter y value:'))             #input all y values


print('x        fx             del1            del2            del3           del4             del5')


for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]      #put delta values in y
              
    

for i in range(n):                                   #show table
    print(x[i], end = "\t")
    for j in range(n - i):
        print(round(float(y[i][j]),10), end = "\t\t")
    print(" ")


value=float(input('ENTER VALUE:'))                   #enter value which we want search


for i in range(0,n):                               
    if(value==x[i]):                                 # search value's uppper limit which in table
        print('already exist in table')
        break
    elif(value<x[i]):
        new_value=x[i]
        b=i
        break


p= (value-new_value)/h                              #value of p


print(p)


u = [[1 for i in range(n)]                          # empty list
          for j in range(n)]


for j in range(0,n):                                #u(u-1)(u-2).....(u-(n-1)) values put in every element of list
    u[j][1]=u[j-1][1]*(p+j)
    print(u[j][1])


add=y[b][0]
print(add)                                             #f(x)

                                  
for i in range(0,4):
    if(i==0):                                           
        add=add+(u[i][1]*y[b-(i+1)][i+1])               #udelta f(x)
    
    else:                                               
        add=add+((u[i][1]*y[b-(i+1)][i+1])/factorial(i+1))  #udelta2f(x)/factioal 2   upto n


print(" ")
print('f(',value,')=',add)

t=[]

for i in range(n):
    t.append(y[i][0])                               #y values put in empty list of t for graph


st.use('ggplot')
plt.title('NEWTON BACKWARD INTERPLOATION')          #matplotlib start
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,t,label='x,f(x)')
plt.scatter(value,add,label='f(7.5)')
plt.legend()
plt.show()