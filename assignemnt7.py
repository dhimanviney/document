#DICTIONARIES

#question1
dict1={}
for i in range(1,5):
    a = input("Enter the key: ")
    b = input("Enter the value: ")
    dict1[a] = b
print(dict1)


#question2
dict1={}
dict2={}
for i in range(1,3):
    dict2={}
    name = input("Enter name ")
    for j in range(1,3):
              sub=input("enter subject")
              marks=int(input("enter marks"))
              dict2[sub]=marks
    dict1[name]=dict2
print(dict1)
student=input("enter the student's name whose marks u want to see")
print(dict1[student])
