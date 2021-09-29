#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv('merc.csv')


# In[4]:


print(df.head(10))


# In[47]:


print(df.head())


# In[48]:


print(df.tail()) 


# In[49]:


print(df.info()) 


# In[50]:


#refer to the row index:
print(df.loc[0])


# In[54]:


print(df.loc[[3, 9]])


# In[44]:


print(df.loc[2])


# In[28]:


#use a list of indexes:
print(df.loc[[0, 1]])


# In[29]:


#identifying duplicates
print(df.duplicated())


# In[31]:


#removing duplicates
df.drop_duplicates(inplace = True)
print(df.head())


# In[32]:


#Dealing with null values

#(1) Remove all null values
nona_df = df.dropna()

print(nona_df.to_string())


# In[34]:


#(2) Replace NULL values with the number 200
checknull = df.fillna(200, inplace = True)
print(checknull)

#df.fillna(130, inplace = True)
#print(df)


# In[36]:


# (3) eplace null values Using Mean, Median, or Mode
x = df["price"].mean()

df["price"].fillna(x, inplace = True)

print(df.head())


# In[19]:


data = {
  "mileage": [240000, 130000, 20000],
  "years": [2003, 2017, 2021]
}

newdf = pd.DataFrame(data, index = ["car1", "car2", "car3"])

print(newdf) 


# In[20]:


#refer to the named index:
print(newdf.loc["car2"])


# In[4]:


name_dict = {
            'Name': ['a','b','c','d'],
            'Score': [90,80,95,20]
          }

df = pd.DataFrame(name_dict)

df.to_csv('file_name.csv')


# In[64]:


test1 = [1, 2, 3, 4, 5]
print(type(test1))


# In[65]:


print(test1[-2])


# In[66]:


test2 = (1, 2, 3, 4, 5)
print(type(test2))


# In[67]:


test1[-2] = 6


# In[68]:


print(test1[-2])


# In[69]:


test2[-2] = 6


# In[70]:


test3 = {1, 2, 3, 4, 5}
print(type(test3))


# In[72]:


test4 = {
    "Fruit": ["apple", "orange", "watermelon"],
    "Weight": [5, 10, 15]
}


# In[73]:


print(test4["Fruit"])


# In[74]:


x = test4.keys()
print(x)


# In[75]:


x = test4.items()
print(x)


# In[ ]:




