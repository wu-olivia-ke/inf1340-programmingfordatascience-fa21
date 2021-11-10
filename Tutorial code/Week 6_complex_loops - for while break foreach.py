#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Using For loops with Pandas


# In[2]:


#Printing columns
import pandas as pd
df = pd.read_csv('merc.csv', index_col=0)

for columns in df:
    print(columns)


# In[20]:


for label, row in df.iterrows():
    print(label)
    print(row)


# In[4]:


for label, row in df.iterrows():
    print(label + " : " + row["transmission"])


# In[5]:


df.head()


# In[6]:


x = 0
for x in df["engineSize"]:
    if x > 1:
        print (x)


# In[10]:



# import pandas package as pd
import pandas as pd
  
# Define a dictionary containing students data
data = {'Name': ['Chuck', 'Charles', 'Stacy', 'Bob'],
                'Age': [21, 19, 20, 18],
                'Stream': ['Math', 'Commerce', 'Arts', 'Biology'],
                'Percentage': [88, 92, 95, 70]}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage'])
  
print(df)
  
print("\nIterating over rows using index attribute :\n")
  
# iterate through each row and select 
# 'Name' and 'Stream' column respectively.
for ind in df.index:
     print(df['Name'][ind], df['Stream'][ind])


# In[11]:


# Using the loc function with for loops
import pandas as pd
  
# Define a dictionary containing students data
data = {'Name': ['Chuck', 'Charles', 'Stacy', 'Bob'],
                'Age': [21, 19, 20, 18],
                'Stream': ['Math', 'Commerce', 'Arts', 'Biology'],
                'Percentage': [88, 92, 95, 70]}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage'])
  

  
print("\nIterating over rows using loc function :\n")
  
# iterate through each row and select 
# 'Name' and 'Age' column respectively.
for i in range(len(df)) :
  print(df.loc[i, "Name"], df.loc[i, "Age"])


# In[12]:



# Looping with the iloc function
import pandas as pd
  
  
# Define a dictionary containing students data
data = {'Name': ['Chuck', 'Charles', 'Stacy', 'Bob'],
                'Age': [21, 19, 20, 18],
                'Stream': ['Math', 'Commerce', 'Arts', 'Biology'],
                'Percentage': [88, 92, 95, 70]}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage'])
  

  
print("\nIterating over rows using iloc function :\n")
  
# iterate through each row and select 
# 0th and 2nd index column respectively.
for i in range(len(df)) :
  print(df.iloc[i, 0], df.iloc[i, 2])


# In[17]:


#Updating Pandas dataframes with for loops
# List of Tuples
salaries = [(11, 5, 70000, 1000) ,
           (12, 7, 72200, 1100) ,
           (13, 11, 84999, 1000)
           ]
# Create a DataFrame object
salaryDfObj = pd.DataFrame(salaries, columns=['ID', 'Experience' , 'Salary', 'Bonus'])
salaryDfObj


# In[18]:


#Let’s update each value in column ‘Bonus’ by multiplying it with 2 while iterating over the dataframe row by row i.e.
# iterate over the dataframe row by row
for index_label, row_series in salaryDfObj.iterrows():
   # For each row update the 'Bonus' value to it's double
   salaryDfObj.at[index_label , 'Bonus'] = row_series['Bonus'] * 2


# In[15]:


salaryDfObj


# In[ ]:




