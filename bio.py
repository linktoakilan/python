#!/usr/bin/env python3.7
print("Hello World!")

name = input("what is your name? ")
color = input("favourite color? ")
age = int(input("How old are you today? "))
# end command to remove new line
#print(name, end=" ")
#print ("is "+str(age) + " years old" + " and loves " + color+" color")
print(name+" is "+str(age) + " years old" + " and loves " + color+" color", sep=", ")
