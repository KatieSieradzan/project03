#!/usr/bin/env python
# coding: utf-8

# In[15]:


data_directory = data_directory = '/badc/cmip6/data/CMIP6/CMIP/MOHC/UKESM1-0-LL/'


# In[16]:


get_ipython().system('ls {data_directory}')


# In[17]:


from itertools import chain
from glob import glob

import matplotlib.pyplot as plt
import xarray as xr

# Set some plotting defaults
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100


# In[18]:


dataset = xr.open_mfdataset(data_directory + 'piControl/r1i1p1f2/Omon/epc100/gn/latest/epc100_Omon_UKESM1-0-LL_piControl_r1i1p1f2_gn_196001-204912.nc')


# In[19]:


dataset


# In[20]:


epc = dataset['epc100']


# In[21]:


epc


# In[22]:


epc.compute()


# In[23]:


epc_1960 = epc.sel(time=slice("1960-01","1960-12")) 


# In[24]:


epc_1960


# In[25]:


epc_1960_mean = epc_1960.mean('time')


# In[26]:


epc_1960_mean


# In[51]:


epc_global_av = epc.mean(['j','i'])


# In[52]:


epc_global_av.depth


# In[53]:


mean_annual_epc = epc_global_av.resample(time="1Y")


# In[59]:


mean_annual_epc_final = mean_annual_epc.mean()


# In[60]:


mean_annual_epc_final


# In[61]:


mean_annual_epc_final.plot()


# In[ ]:




