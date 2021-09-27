#Learning how to read and write files:
#Write - takes a string you want to write to a file and writes it to the file.
#readline - reads one line only of a text file
#truncate - empties out the contents of a file
#seek(0) - moves the read/write location to the begining of the file.

#imports the arguement variable module
from sys import argv

#unpacks the variables in argv
script, filename = argv

print(f"We are going to erase {filename}.")
print("If we dont want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#takes your input for CTRL_C or Return:
input("?")

print("Opening the file.......")
#opens the file we specify:
target = open(filename, 'w')

print("Truncating the file. Goodbye..!!")
#Truncates the file i.e deletes the contents of the file.
target.truncate()

print("Now I'm going to ask you for three lines....")
#takes input from the user to enter 3 lines of strings text:
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to a file........")
#writes the user's input to a file line by line
#doing the write with just one target.write() instead of the repetition:
target.write("%s \n %s \n %s" %(line1, line2, line3))

#we can also use:
# target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')


print("And finally we close it.")
#closes the file:
target.close()

print("Checking that we wrote to the file correctly........")
test = open(filename)
print(test.read())
test.close()
