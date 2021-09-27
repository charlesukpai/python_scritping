#This exercise is about fixing bad code to make it run as it should.
#In this exercise, you will practice dealing with a bad programmer by fixing a bad programmer’s code.
#The point of this exercise isn’t to type it in but to fix an existing file.

from sys import argv

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() #added variable to get height from user.
print("How much do you weigh?", end=' ') #missing closing bracket fixed.
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv #used argv here without first importing it. Added import statement at the top

txt = open(filename) #misspelled the variable name, corrected that

print("Here's your file {filename}:")
print(txt.read()) #missing 't' in txt. added that.

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) #error calling read method by using (_) instead of (.) fixed to txt_again.read()


print("Let's practice everything.") #fixed the quotes here. Using single quotes inside the string so can't use them to close it as well.
print("""You\'d need to know \'bout escapes 
      with \\ that do \n newlines and \t tabs.""") #changed the quotes to """ to allow multi lines in the print() statement.

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")#missing closing quote for string.
print(poem)
print("--------------")#mising opening quote for string


five = 10 - 2 + 3 #fixed missing operator here.
print(f"This should be five: {five}") #fixed missing closing bracket.

def secret_formula(started): #Fixed missing : for function.
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars + 100 #Fixed missing math operator here. Added +
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point) #needs 3 values instead of 2, added crates variable.

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) #syntax error with start_point missing the (_). Added this to correct the error.
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
cats = 30 #Fixed error in variable name here. Should be cats not cates.
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!") #fixed missing brackets for print statement.

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: #fixed missing : for if statement.
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: #fixed missing : for if statement.
    print("People are less than or equal to dogs.") #fixed missing closing quote for print statement.

if people == dogs: #fixed = to == for if statement since = is for variable assignment and == is for equal to.
    print("People are dogs.")