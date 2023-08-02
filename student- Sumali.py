#!/usr/bin/env python
# coding: utf-8

# ## Final Project Submission
# 
# Please fill out:
# * Student name:Sumali Wickramarachchi 
# * Student pace: part time
# * Scheduled project review date/time: 12th August 2023
# * Instructor name: Rajive Islam
# * Blog post URL:
# 

# In[9]:


#importing standard packages 
import pandas as pd
import numpy as np
import seaborn as sns


# In[24]:


#file paths 
data_extract1= r"C:\Users\Sumali\Documents\dsc-phase-1-project\zippedData\imdb.title.basics.csv.gz"
data_extract2= r"C:\Users\Sumali\Documents\dsc-phase-1-project\zippedData\imdb.title.ratings.csv.gz"
data_extract3= r"C:\Users\Sumali\Documents\dsc-phase-1-project\zippedData\bom.movie_gross.csv.gz"
data_extract4= r"C:\Users\Sumali\Documents\dsc-phase-1-project\zippedData\imdb.title.principals.csv.gz"


# In[31]:


# read CSV files into Dataframes
df1=pd.read_csv(data_extract1, compression='gzip')
df2=pd.read_csv(data_extract2, compression='gzip')
df3=pd.read_csv(data_extract3, compression='gzip')
df4=pd.read_csv(data_extract4, compression='gzip')


# In[19]:


#Undertanding raw data for imdb titles  
df1.head(10)


# In[20]:


#Undertanding raw data for Imdb ratings
df2.head(10)


# In[32]:


#Undertanding raw data for BOM- Box office Mojo gross 
df3.head(10)


# In[33]:


#Undertanding raw data for title principals 
df4.head(10)


# In[13]:


from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.random.rand(20)
plt.plot(x, '*-', color='red', markersize=10)

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




