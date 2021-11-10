#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#------------------------------------------------------------
#------------------------For Loops---------------------------
#------------------------------------------------------------


# In[ ]:


#looping through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#looping through a string
for x in "banana":
  print(x)


# In[4]:


#Working with dictionaries (this is the typical format for working with JSON)
cars = {
    "colour":
    [
        "blue",
        "yellow",
        "orange"
    ],
    
    "size":
    [
        "sedan",
        "suv",
        "van"
    ]
}

#looking through keys:
for x in cars["size"][0]:
    for i in x:
        print(i)


# In[25]:


#looping through values
for x in cars["colour"]:
    print(x)


# In[5]:


#looping through characters within values
for value in cars["size"][1][0]:
    for letter in value:
        print(letter)


# In[ ]:


#Else with For loops


# In[9]:


for x in range(6):
  print(x)
else:
  print("Finally finished!")


# In[ ]:


#Nested For loops


# In[8]:


colours = ["red", "yellow", "green"]
fruits = ["apple", "banana", "guava"]

for x in colours:
    for y in fruits:
        print (x,y)


# In[ ]:


#------------------------------------------------------------
#------------------------While Loops-------------------------
#------------------------------------------------------------


# In[9]:


i = 1
while i < 6:
  print(i)
  i += 1


# In[14]:


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# In[ ]:


#------------------------------------------------------------
#------------------------Break-------------------------------
#------------------------------------------------------------


# In[10]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "as":
    break


# In[ ]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# In[12]:


i = 0
while i < 6:
  i += 1
  if i == 3:
    break
  print(i)


# In[13]:


cars2 = {
    "colour":
    [
        "blue",
        "yellow",
        "orange"
    ],
    
    "size":
    [
        "sedan",
        "suv",
        "van"
    ]
}

len(cars)

for x in cars2:
    for j in x:
        if j == "s":
            break
        print(j)


# In[ ]:




