######ASSIGNMENT-3######
###List Question##
#Ques.1
a=[]#CREATING a empty list
b=0
x=int(input("enter total no. of element in list="))
for i in range(0,x):
    b=input("enter the element= ")#GIVING INPUT
    a.append(b) #NOW THE INPUTS ARE ADDED TO THE LIST
print(a)
#Ques.2
z=[]#CREATING empty list
a=['google','apple','facebook','microsoft','tesla']#Predefined List
z.append(1)
z.append(2)
z.append(3)
z.append(4)
z.append(5)
z.append(a)
print(z)
#Ques.3 
f=[]#CREATING empty list
g=0
x=int(input("enter total no of element in list"))
for i in range(0,x):
    g=input("enter the element to add in list ")#Giving input
    f.append(g) #adding the input in list
print(f)
m=input("enter the element to find in the list")
cont=f.count(m)
if(cont>0):
    print("total no of element occuring the in list is ",cont)
else:
    print("No element found")
    
#Ques.4 
f=[]#CREATING empty list
g=0
x=int(input("enter total no of element in list"))
for i in range(0,x):
    g=int(input("enter element to add in list "))
    f.append(g) #adding the input in list
    f.sort()
print(f)
 #Ques.5 
i=[1,2,3,4,5,6]
j=[5,6,7,8,9,10]
c=[]
c=i+j# adding two list
c.sort()#sorting
print(c)
#Ques.6 
a=[]
b=0
counteven=0
countodd=0
x=int(input("enter total no of element in list"))
for i in range(0,x):
    b=int(input("enter element to add in list "))
    a.append(b) #adding the input in the list
    a.sort()
for i in range(0,len(a)):
    if a[i]%2==0:
        counteven=counteven+1
    else:
        countodd=countodd+1
print("total even element in the list is ",counteven)
print("total odd element in the list is ",countodd)
 #TUPLE Questions!!!###
#Ques.1

tupo=('aa','bb')
tup=tupo[::-1]
print(tup)
#Ques.2
tupe=(1,2,3,4,5)
h=max(tup)
j=min(tup)
print(" max no in tuple is ",h)
print(" min no in tuple is ",j)
 #string QuestIons!!!###
#Ques.1
strr='hello world'
print(strr.upper())#function to cahnge lower case to upper case
#Ques.2
strr='156465365'
print(bool(strr.isdigit()))#function to print whether it is digit or not!!
#Ques.3 
stp='hello world'
t=stp.replace('world','Viney')
print(t)
