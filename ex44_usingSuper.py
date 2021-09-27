
#Super is used to help python resolve multiple inheritances.
#The most common use of super() is actually in __init__ functions in base classes. This is usually the only place you need to do
#some things in a child then complete the initialization in the parent.
#Example:

# class Child(Parent):
#     def __init__(self, stuff):
#         self.stuff = stuff
#         super(Child, self).__init__()

#Here variables are first set in the __init__() in the child then initilazed in the parent with Parent.__init__()

##Composition:
##############
#Instead of using inheritance, we can use other classes and modules to achieven the same thing.
#Example:

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")


class Child(object):

    def __init__(self):
        self.other = Other() #This equates self.other to the Parent Class.
    
    def implicit(self):
        self.other.implicit()#This runs to give you the implicit in the Parent class since self.other = Other()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD AFTER OTHER altered()")

son = Child()

son.implicit()#This will print the parent class value since we initialized self.other to call the parent class Other()
son.override() #will call override in the child class and print that not the parent.
son.altered() #will first print the value from the child class then hit self.other.altered()
