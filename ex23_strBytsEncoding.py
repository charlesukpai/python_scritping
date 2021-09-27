# Strings, Bytes, and Character Encodings:

# To do this exercise you’ll need to download a text file that I’ve written named languages.txt (https://learnpythonthehardway.org/python3/languages.txt). 
# This file was created with a list of human languages to demonstrate a few interesting concepts:
# 1. How modern computers store human languages for display and processing and how Python 3 calls this strings.
# 2. How you must “encode” and “decode” Python’s strings into a type called bytes.
# 3. How to handle errors in your string and byte handling.
# 4. How to read code and find out what it means even if you’ve never seen it before.
# Note:- The convention for encoding text in Python is called “UTF-8”, which means “Unicode Transformation
# Format 8 Bits.”

#import the system module
import sys

#get argv from the sys module and unpack the variables
script, input_encoding, error = sys.argv

#define the main function here that reads a line from the language file
def main(language_file, encoding, errors):
    line = language_file.readline()
    #if statement checks if our variable line las anything in it and if True, the if statement executes
    if line:
        #Calls the function print_line() to print the line if line exists, if we get to the end and there's no more lines, if statement becomes False so code wont run.
        print_line(line, encoding, errors)
        #We call the main function here after gettinf the line to go back to the top of the code and execute again
        return main(language_file, encoding, errors)

#Function to print the line read in the main() function.
#this function also handles the encoding of each line. The strip() strips off any new line characters (\n) on the line string.
def print_line(line, encoding, errors):
    next_lang =line.strip()
    #encode() encodes a string into bytes so python can work with it. Gets the raw bytes from the next_lang variable.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #decode() gets the raw bytes and decodes them into strings.
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<======>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
