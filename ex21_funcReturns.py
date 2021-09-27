#Using return() to set variables to be a value from a function.

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

#Creating the age variable and assigning it the add function.
age = add(30, 5)
#Creating the height variable and assigning it the subtract function.
height = subtract(78, 4)
#Creating a weight variable and assigning it the multiply variable
weight = multiply(90, 2)
#Creating an iq variable and assigning it the divide function
iq = divide(100, 2)

print(f"AGE: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzle for the extra credit, type it in anyway:
print("Here is a puzzle:")

#Starts executing the brackets from vision i.e. the innermost bracket first.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")


