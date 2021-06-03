#!/usr/bin/env python
# coding: utf-8

# In[28]:


data_directory = data_directory = '/badc/cmip6/data/CMIP6/CMIP/MOHC/UKESM1-0-LL/'


# In[29]:


get_ipython().system('ls {data_directory}')


# In[30]:


from itertools import chain
from glob import glob

import matplotlib.pyplot as plt
import xarray as xr

# Set some plotting defaults
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100


# In[31]:


dataset = xr.open_mfdataset(data_directory + 'piControl/r1i1p1f2/Omon/epc100/gn/latest/epc100_Omon_UKESM1-0-LL_piControl_r1i1p1f2_gn_196001-204912.nc')


# In[32]:


dataset


# In[33]:


epc = dataset['epc100']


# In[34]:


epc


# In[35]:


epc.compute()


# In[80]:


select_an_area_latitude = epc.sel(j = slice(20,80))


# In[81]:


select_an_area_longitude = select_an_area_latitude.sel(i = slice(20,80))


# In[82]:


select_an_area_longitude


# In[83]:


area_average = select_an_area_longitude.mean(['j','i'])


# In[84]:


area_average.compute()


# In[85]:


mean_annual_epc = area_average.resample(time="1Y")


# In[86]:


mean_annual_epc_final = mean_annual_epc.mean()


# In[87]:


mean_annual_epc_final


# In[88]:


mean_annual_epc_final.plot()


# In[ ]:




