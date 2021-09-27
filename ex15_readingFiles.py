#Learning to read from a file:

#We are going to open a txt file and print out its contents:
#Instead of ahrdcoding a file name, we will use argv or input() to ask the user the file to open.
#Note:- You have to give the name of the file you want to open as input to argv on the terminal

#imports the arguement variable argv module:
from sys import argv

#unpacks and assigns the variables held by argv:
script, filename = argv

#opens the file:
txt = open(filename)

#prints out the contents of the file:
print(f"Here's your file {filename}:")

#reads the contents of the file:
print(txt.read())

#close the file after reading. Always do this.
txt.close()
print("File closed")

# #Reading from a second file:
# print("Type the filename again:")
# #takes the name of a file you want to open as input:
# file_again = input("> ")

# #opens the new file:
# txt_again = open(file_again)

# #reads the contents of the new file:
# print(txt_again.read())

# txt_again.close()
# print("File closed")

