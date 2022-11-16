#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("./chronickidneydisease.csv")


# In[3]:


print(df)


# In[4]:


from pandas_profiling import ProfileReport


# In[5]:


profile = ProfileReport(df)


# In[6]:


profile.to_file(output_file="./chronickidneydisease.csv")


# In[ ]:




