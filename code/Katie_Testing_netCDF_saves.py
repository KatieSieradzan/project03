#!/usr/bin/env python
# coding: utf-8

# In[32]:


from itertools import chain
from glob import glob

import matplotlib.pyplot as plt
import xarray as xr
import numpy as np

# Set some plotting defaults
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100


# In[36]:


test1 = xr.open_mfdataset('/home/users/train047/control_epc.nc')
test2 = xr.open_mfdataset('/home/users/train047/control_concat_epc.nc')
test3 = xr.open_mfdataset('/home/users/train047/control__individual_epc.nc')
test4 = xr.open_mfdataset('/home/users/train047/decadal_average.nc')


# In[37]:


test4


# In[30]:


test1_epc_1 = test1['epc_1']
test1_epc_1.plot()


# In[31]:


test1_epc_2 = test1['epc_2']
test1_epc_2.plot()


# In[29]:


test2_epc = test2['epc']
test2_epc.plot()


# In[ ]:




