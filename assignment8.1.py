##QUES.1
class circle:
    def __init__(self):
        self.radius=10
    def getArea(self):
        self.area=3.14*(self.radius**2)
        print(self.area)
    def getcircumference(self):
        print(2*3.14*self.radius)

a=circle()
a.getArea()
a.getcircumference()



##Ques. 2
class student:
    def __init__(self):
        self.name=input("Enter Name")
        self.rollno=int(input("Enter Rollno"))
        self.age=0
        self.marks=0
    def display(self):
        print("Student Info")
        print(self.name,self.rollno,self.age,self.marks)
    def setAge(self):
        self.age=int(input("Enter Age"))
    def setmarks(self):
        self.marks=int(input("Enter Marks"))

x=student()
x.setAge()
x.setmarks()
x.display()

##Ques.3"
class temprature():
    def __init__(self,celsius):
        self.celsius=radius
    def __init__(self,farenheit):
        self.farenhiet=farenheit 
    def celsius(self):
        return (c*1.8)+32
    def farenheit(self):
        return (f-32)/1.8
c=float(input("Enter the temperature in celsius="))
f=float(input("Enter the temperature in farenheit="))
obj1=temprature(c)
obj2=temprature(f)
print("Temprature changed farenheit=",obj1.celsius())
print("Temprature changed celsius=",obj2.farenheit())



##Ques.4"
class MovieDetails:
    def Display(self):
        print("Movie Details:")
        print("Artist Name:-",self.artist_name,"\nYear Of Release:-",self.year,"\nRating:-",self.rating)
    def Add(self):
        self.artist_name=input("Artist Name:- ")
        self.year=int(input("Year Of release:- "))
        self.rating=float(input("Rating"))
x=MovieDetails()
x.Add()
x.Display()

##Ques. 5
class animal:
    def info_(self):
        print("Class Animal")
class animal_attribute():
    def attribute(self):
        print("Class Animal_Attributes")
class tiger(animal,animal_attribute):
    def tiger_(self):
        print(" Class Tiger")

x=animal()
y=animal_attribute()
z=tiger()
z.info_()
z.attribute()

##Ques.6
print("""OUTPUT:A B""")

##Ques.. 7
class shape:
    def methodarea(self):
        self.l=int(input("enter the length"))
        self.b=int(input("enter the breadth"))
class rectangle(shape):
    def methodarea(self):
        self.l=int(input("enter the length of rectangle"))
        self.b=int(input("enter The breadth of rectangle"))
class square(shape):
    def methodarea(self):
        self.l=int(input("enter the length of sides of square"))
x=shape()
y=rectangle()
z=square()
y.methodarea()
z.methodarea()

