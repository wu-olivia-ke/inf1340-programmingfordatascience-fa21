#!/usr/bin/env python
# coding: utf-8

# In[1]:


#if conditionals
a = 33
b = 200
if b > a:
  print("b is greater than a")


# In[2]:


#elif conditionals
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# In[3]:


#else conditionals
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# In[4]:


#and conditionals
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# In[5]:


#or conditionals
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


# In[6]:





# In[7]:


list = [1, 2, 3, 4, 5]
print(len(list))


# In[1]:


fruits = ["apple", "orange", "dragonfruit", "watermelon", "lychee"]
if len(fruits) > 4:
    print("over 4")


print(len(fruits))


# In[2]:


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# In[4]:


a = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

if a[-7] == "apple":
    print("exists")
elif a[5] == "pineapple":
    print("not found")
    


# In[19]:


a = 40
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


# In[27]:


a = 30
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is True")
else:
    print("None of the conditions are True")


# In[ ]:




