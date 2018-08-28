##Functions##
##Ques.1 
import math
def sphere(radius):
    sa =  4 * math.pi * radius * radius
    print(" The Surface area of a Sphere = %.2f" %sa)
    
radius=float(input("Enter the radius="))
sphere(radius)
##Ques.2
def perfect(num):
    s=0
    for i in range(1,int(num)):
        if(num%i==0):
            s=s+i
    if(s==num):
            print(num)
a=1000
for j in range(1,a):
    perfect(j)

##Ques.3
def multi(n):
    for i in range(1,11):
        b=n*i
        print(n,'x',i,'=',b)
n=int(input("Enter the value="))
multi(n)
##Ques.4
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))

