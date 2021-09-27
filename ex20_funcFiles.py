#Using Functions and files:
#Note: Each time you do f.seek(0) you’re moving to the start of the file. 
#Each time you do f.readline() you’re reading a line from the file & moving the read head to right after the \n that ends that line.


from sys import argv

script, input_file = argv

#defining a function that reads the file we assign to the argv variable input_file
def print_all(f):
    print(f.read())

#opens the file with the read/write pointer at position 0 (start of the file)
def rewind(f):
    f.seek(0)

#This function checks the current line number & reads that line then prints it. This is set to 0 with f.seek(0)
def print_a_line(line_count, f):
    print(line_count, f.readline())

#Opens the input give given to argv by the user.
current_file = open(input_file)

print("First let's print the whole file: \n")

#prints the whole file
print_all(current_file)

print("Now let's rewind, kind of llike a tape:")

rewind(current_file)

print("let's print 3 lines:")

#here we specify the current line with a variable and the current file then call the print_a_line() function with these 2 variables
#current_line refers to line count in the print_a_line(0) func & current_file is f & has the readline() func called on it to read the line in the file
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

