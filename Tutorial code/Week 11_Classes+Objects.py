#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#----------Explaining the concept of Classes---------------

#A class is a blueprint for the object.
#We can think of class as a sketch of a parrot with labels. 
#It contains all the details about the name, colors, size etc. 
#Based on these descriptions, we can study about the parrot. 
#Here, a parrot is an object.


#--------Explaining the concept ob an Object----------------
#An object (instance) is an instantiation of a class. When 
#class is defined, only the description for the object is defined. 
#Therefore, no memory or storage is allocated.


# In[16]:


#------------------Classes------------------------------------------#
#The __init__() function is a built-in Python function.
#All classes have a function called __init__(), which is always 
#executed when the class is being initiated.
#In the following example, the __init__() function is used 
#to assign values to object properties, or other operations
#that are necessary to do when the object is being created
#The following class named Person, use the __init__() 
#function to assign values for name and age:


# In[ ]:


#The example for class of parrot can be :
class Parrot:
    pass

#Here, we use the class keyword to define an empty class Parrot.
#From class, we construct instances. 

#An instance is a specific object created from a particular class.


#For example, has anyone heard of the **Class Diagram**?


# In[13]:


#Suppose we have details of parrots. Now, we are going to 
#show how to build the class and objects of parrots.

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
Jamie = Parrot("Jamie", 10)
Murtagh = Parrot("Murtagh", 15)

# access the class attributes
print("Jamie is a {}".format(Jamie.__class__.species))
print("Murtagh is also a {}".format(Murtagh.__class__.species))

# access the instance attributes
print("{} is {} years old".format( Jamie.name, Jamie.age))
print("{} is {} years old".format( Murtagh.name, Murtagh.age))


# In[6]:


#Inheritance with Classes
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


# In[4]:


class Player:
  def __init__(self, name, number, position):
    self.name = name
    self.number = number
    self.position = position

player1 = Player("John", 36, "Striker")

print(player1.name)
print(player1.number)
print(player1.position)


# In[5]:


#Class inheritance

#Any class can be a parent class. 
#In the following example, we will create a class named Person, 
#with firstname and lastname properties, and a printname method


# In[8]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Chuck", "Norris")
x.printname()


# In[5]:


#To create a class that inherits the functionality from 
#another class, in this example we will send the parent class 
#as a parameter when creating the child class


# In[6]:


#Here we will insert a function that prints a greeting
#and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name,"and I am", self.age)

p1 = Person("John", 36)
p1.myfunc()


# In[11]:


#----------Creating an object in Python------------------------
class Person:

    def greet(self):
        print('Hello')

# create a new object of Person class
harry = Person()

# Calling object's greet() method
# Output: Hello
harry.greet()


# In[14]:


class Sales:
    def __init__(self, id):
        self.id = id
        id = 100

val = Sales(123)
print (val.id)

