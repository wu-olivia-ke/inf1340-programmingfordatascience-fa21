#!/usr/bin/env python
# coding: utf-8

# In[2]:


##Example of a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[3]:


#Dictionary items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


# In[4]:


thisdict["model"]


# In[3]:


#Duplicate values not allowed, the key will overwrite the previous
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# In[5]:


#Looping through dictionary values

#Option 1:
for x in thisdict:
  print(thisdict[x])

#Option 2:
for x in thisdict.values():
  print(x)


# In[7]:


#Loop through both keys and values
for x, y in thisdict.items():
  print(x, y)


# In[7]:


for key in thisdict.keys():
  print(key)


# In[8]:


#Get values based on a given key of a dictionary e.g. value of the model key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)


# In[9]:


#Insert an item into a dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)


# In[18]:


#Change a value in a dictionary
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["model"] = "Focus"
car


# In[9]:


#Nested dictionaries
#You will typically see dictionaries in the form of nested dictionaries when
#dealing with any data science task, because of dealing with JSONs



#The following has 3 dictionaries within 1 dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child1"]["name"])


# In[5]:



students = {
    "student1" : {
        "name" : "Charleston",
        "grade" : 90
    },
    "student2" : {
        "name" : "Florence",
        "grade" : 85
    },
    "student3" : {
        "name" : "Linus",
        "grade" : 70
    }
}

print("Charleston" in students.values())


# In[ ]:




