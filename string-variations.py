#!/usr/bin/env python3.7
String=input("Enter a String :")
print(String)
print("LowerCase: ",String.lower())
print("UpperCase: ",String.upper())
print("Capitalize: ",String.capitalize())
print("Title Case: ",String.title())

words=String.split()
print(words)


sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])
