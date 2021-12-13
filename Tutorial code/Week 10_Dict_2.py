#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json


# In[3]:


#Open your JSON file
file = open('json_sample1.json')


# In[4]:


#return JSON object as a dictionary
data = json.load(file)
data


# In[5]:


print(data['type'])


# In[6]:


#Iterate through a json list:
for i in data['image']:
    print(i)

file.close()


# In[7]:


# JSON string
a = '{"name": "Bob", "languages": "English"}'
 
# deserializes into dict
# and returns dict.
y = json.loads(a)
 
print(y)


# In[22]:


###############Example #1 ########################
# JSON file
f = open ('json_sample1.json', "r")
 
# Reading from file
data = json.loads(f.read())
 
# Iterating through the json
# list
for i in data['image']:
    print(i)
 
#Closing file
f.close()


# In[10]:


###############Example #2 ########################
# JSON file
f = open ('json_sample2.json', "r")
 
# Reading from file
data = json.loads(f.read())

data


# In[11]:


print(json.dumps(data, indent = 4, sort_keys=True))


# In[72]:


#Formatting your JSON in a more read-able/digestible format
print(json.dumps(data[2], indent = 4, sort_keys=True))


# In[84]:


#Why won't this work?
#print(data['batters'])








#The correct method
print(data[0]["batters"]['batter'][1])


# In[83]:


#Practical uses out of parsing JSONs
#How can we get the types of toppings (i.e. flavours) that are available with
#the Old Fashioned donut?

print("The Old Fashioned donut comes in the following topping types: ",
      (data[2]["topping"][0]["type"],
       data[2]["topping"][1]["type"],
       data[2]["topping"][2]["type"],
       data[2]["topping"][3]["type"],
      
      ))


# In[21]:


print("The Raised donut comes in the following batter types: ",
      (data[1]["batters"]['batter'][0]['type']      
          
       
      
      ))


# In[39]:


#Converting a dict to JSON string
person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(type(person_json))


# In[40]:


#Writing JSON to a file

person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)


# In[46]:


#Printing your JSON data in a more readable/digestible format i.e. Prettyprint

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string 
print(json.dumps(person_dict, indent = 4, sort_keys=True))


# In[ ]:




