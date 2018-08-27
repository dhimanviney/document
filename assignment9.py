##Ques.1##
a=3
if a<4:
    try:
        a=a/(a-3)
    except:
        print("denominator cannot be zero!")
print(a)
##Ques.2
l=[1,2,3]
try:
	print(l[3])
except:
	print("Index out of Range")
##Ques.3
##An Exception
##Hi There
##Ques.4
##-5.0
##a/b result in 0

#question-5
#1.IMPORT ERROR
try:
    import maths
except ImportError as message:
    print('Exception:', message)
##2.Value Error
try:
    x = int(input("Please enter a number: ")) 
except ValueError:
    print("Oops!  That was not a valid number.Try again...")
#3.INDEX ERROR
l=[4,5,6,8,9]
try:
    print(l[6]) 
except:
    print("indexes above 5 aren't acceptable.")


