##If Else Questions##

##Ques.1
a=int(input("Enter the year="))
if(a%4==0):
    print("Leap Year")
else:
    print("Not a Leap Year")
##Ques.2
l=int(input("Enter the Length"))
b=int(input("Enter the breadth"))
if(l==b):
    print("It is Square")
else:
    print("It is rectangle")
##Ques.3
age1=int(input("Enter the age of 1st person="))
age2=int(input("Enter the age of 2nd person="))
age3=int(input("Enter the age of 3rd person="))
if(age1>age2 and age1>age3):
    print("Person 1 is older nd age is=",age1)
elif(age2>age1 and age2>age3):
    print("Person 2 is older nd age is=",age2)
else:
    print("Person 3 is older nd age is=",age3)
if(age1<age2 and age1<age3):
    print("Person 1 is younger nd age is=",age1)
elif(age2<age1 and age2<age3):
    print("Person 2 is younger nd age is=",age2)
else:
    print("Person 3 is younger nd age is=",age3)
##Ques.4
a=int(input("Enter age="))
b=input("Enter the Sex M or F=")
c=input("Enter the marital Satus Y or N=")
if(b=='F'):
    print("You can work in urban areas")
if(b=='M' and a>=20 and a<40):
    print("You may work anywhere")
elif(b=='M' and a>=40 and a<=60):
    print("You will work in urban areas")
else:
    print("ERROR")
##Ques.5
a=int(input("Enter the quantity="))
b=int(input("Enter the Price="))
c=a*b
if(c>=1000):
    d=c*0.1
    e=c-d
    print("The total price=",e)
else:
    print("The total price=",c)
###Loops Questions###
#Question 1
li=[]
for i in range(10):
    a=int(input("Enter a number"))
    li.append(a)
print(li)

#Question 2

while True:
      print("*")

    
#Question 3
    
a=[]
b=[]
num=int(input("enter number of elements"))
for i in range(num):
    c=int(input("enter number"))
    a.append(c)
for j in a:
    v=j*j
    b.append(v)
print(b)

#Question 4

li1=[]
li2=[]
li3=[]
li4=[]
a=int(input("Enter total number of inputs"))
for i in range(a):
    b=input("Enter elements of list")
    li1.append(b)
for i in li1:
    if(i.isdigit()):
        li2.append(i)
    elif(i.isalpha()):
        li3.append(i)
    else:
        li4.append(i)
print(li2)
print(li3)
print(li4)

#Question 5

p=[]
for i in range(1,101):
    if(i>1):
        flag=False
        for j in range(2,i):
            if(i%j==0):
                flag=True
        if not flag:
            p.append(i)
print(p)

#Question 6

for i in range(5):
    for j in range(i):
        print("*",end='')
    print()


#Question 7


li8=[]
n=int(input("Enter number of elements of list"))
for i in range(n):
    a=int(input("Enter element"))
    li8.append(a)
num=int(input("Enter the number you want to delete from list"))
x=li8.count(num)
for i in range(x):
    y=li8.index(num)
    del(li8[y])
print(li8)
