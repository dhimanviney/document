
#Ques.1
a=['1','2','3','4','5','6','7','8','9']
print(a[::-1])




#Ques.2.Print all uppercase letter from a string...
# Read input from the user.
inputStr = input("Enter a string: ")

# Find and display the uppercase letters.
for ch in inputStr :
   if ch >= "A" and ch <= "Z" :
      print(ch, end="")

print()

##Ques.3
##It is not covered in class i will do it by tommorow...

#Ques4.Check For palindrome
string=input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")


##Ques.5
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
##Shallow copy###
##A shallow copy means constructing a new collection object and then populating it with references
##to the child objects found in the original. In essence, a shallow copy is only one level deep.
##The copying process does not recurse and therefore won’t create copies of the child objects themselves.
##DEEP COPY##
##A deep copy makes the copying process recursive. It means first constructing a new collection object and
##then recursively populating it with copies of the child objects found in the original. Copying an object
##this way walks the whole object tree to create a fully independent clone of the original object and all of its children.

