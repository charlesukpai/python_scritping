
# Avoid multiple inheritances and use compositons where possible instead of inheritance.
# inheritance indicates that a class will get some or all of its features from a parent class.
# Example class Foo(Bar) is saying create a class Foo that inherits from another class Bar.
# Note:-
# Actions on the child imply an action on the parent.
# Actions on the child override the action on the parent.
# Actions on the child alter the action on the parent.

# When you use pass under a function defining a class, it tells python that it has no new arguements defined but will inherit from the main class.
# if you put functions in a base class (i.e., Parent), then all subclasses (i.e., Child) will automatically get
# those features. Very handy for repetitive code you need in many classes.

# When you use "pass" under a function defining a class, it tells python that it has no new arguements defined but will inherit from the main class.
#The Child class inherits and uses the functions in the Parent class.

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")
    

class Child(Parent):
# sometimes you want the child to behave differently. In this case you want to override the function in the child, effectively replacing the functionality. 
# To do this, just define a function with the same name in Child. Here’s an example:
    def override(self):
        print("CHILD override()")

#Sometimes you also want the child to behave different either before or after the Parent version runs, 
# you do the override using a python function called super to get the parent version to call:
    def altered(self):
        print("CHILD BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()