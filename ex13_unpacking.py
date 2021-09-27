#passing variables to a script using the command line:

#import the arguement variable module argv. 
from sys import argv

#This line unpacks argv and assigns it 4 variables.
script, first, second, third = argv

fourth = input("Enter your fourth variable: ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
