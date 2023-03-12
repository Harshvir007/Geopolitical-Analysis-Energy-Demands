#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import matplotlib.pyplot as plt


# In[4]:


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')) # is a basemap provided with geopandas


# In[5]:


world.head(20)


# In[8]:


world.shape #it shows the rows and columns of the datasets


# In[10]:


type(world)


# In[11]:


#it is not dataframe it is geo data frame


# In[13]:


world.loc[18,"geometry"] #this is the polygon


# In[ ]:





# In[27]:


world.query("  continent == 'Asia' ")


# In[26]:


fig, gax = plt.subplots(figsize=(10,10))
world.query("continent == 'Asia'").plot(ax=gax, edgecolor = 'black', color = 'red')

gax.set_xlabel('longitude')
gax.set_ylabel('latitude')
gax.set_title('Asia')

gax.spines['top'].set_visible(False)
gax.spines['right'].set_visible(False)


# In[29]:


world.plot('pop_est', legend=True, figsize=(15,14), cmap='magma')
plt.title('World Population')


# In[32]:


world.boundary.plot(figsize=(12,8))


# In[ ]:




