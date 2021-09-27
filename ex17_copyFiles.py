#Python script to copy one file to another.
from sys import argv
#this returns True if a file exists and False if it does not.
from os.path import exists

#unpacking variables from argv for the file to copy from and the one to copy to so we need 2 command line argeuments.
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

#Opens the file and reads it.
indata = open(from_file).read()

#The len(indata) reads the length of the string we got from reading the file and returns its integer value.
print(f"The input file is {len(indata)} bytes long")

#exists() function checks to see if the file exists and returns True if it does and False if it doesnt.
print(f"Does the output file exist? {exists(to_file)}")

# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# #The input here takes your keyboard response for either RETURN or CTRL-C
# input()

out_file = open(to_file, 'w').write(indata)
# out_file.write(indata)

print("Alright, all done")




