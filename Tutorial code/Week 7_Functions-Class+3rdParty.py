#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install numpy')


# In[9]:


import pandas as pd
import numpy as np
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])


# In[10]:


print(s)


# In[11]:


#Numpy functions
from numpy import pi
np.linspace(0, 2, 9)   


# In[12]:


x=np.array(dir(np))


# In[16]:


a = np.arange(12).reshape(3, 4)
 
b = np.arange(4).reshape(1, 4)
 
print(a)
print(b)
 
# Broadcasts (a < 5, a, and b * 10)
# of shape (3, 4), (3, 4) and (1, 4)
c = np.where(a < 5, a, b * 10)
 
print(c)


# In[17]:


#Pandas functions


# In[18]:


df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})


# In[19]:


#Pivot table functions
table = pd.pivot_table(df, values='D', index=['A', 'B'],
                    columns=['C'], aggfunc=np.sum)


# In[20]:


table


# In[4]:


def multiply(b,c):
    a = b * c
    return a


print(multiply(10, 2))
    


# In[ ]:




