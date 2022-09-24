#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import matplotlib.pyplot as plt


# In[2]:


image = plt.imread('C:\\Users\\DELL\\Downloads\\image1.jfif')


# In[3]:


plt.imshow(image)


# In[4]:


addimage = image + 50
plt.imshow(addimage)


# In[5]:


subimage = image - 50
plt.imshow(subimage)


# In[7]:


divimage = image / 2
plt.imshow(divimage.astype('uint8'))


# In[8]:


divimage = image // 2
plt.imshow(divimage)


# In[7]:


mulimage = image * 2
plt.imshow(mulimage)


# In[ ]:




