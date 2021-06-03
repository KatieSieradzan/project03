#!/usr/bin/env python
# coding: utf-8

# In[99]:


data_directory = data_directory = '/badc/cmip6/data/CMIP6/CMIP/MOHC/UKESM1-0-LL/'


# In[100]:


get_ipython().system('ls {data_directory}')


# In[101]:


from itertools import chain
from glob import glob
import seaborn as sns
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import xarray as xr

# Set some plotting defaults
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100


# In[102]:


sec_to_yr=60.0*60.0*24.0*365.0 # seconds to year
mol_to_g_C=12.01 # mol to gram for carbon
g_to_Pg=1.0/1.0e15 # grams to Petagrams


# In[103]:


dataset1 = xr.open_mfdataset(data_directory + 'piControl/r1i1p1f2/Omon/epc100/gn/latest/epc100_Omon_UKESM1-0-LL_piControl_r1i1p1f2_gn_196001-204912.nc')
dataset2 = xr.open_mfdataset(data_directory + 'piControl/r1i1p1f2/Omon/epc100/gn/latest/epc100_Omon_UKESM1-0-LL_piControl_r1i1p1f2_gn_205001-214912.nc')
area = xr.open_mfdataset(data_directory + 'piControl/r1i1p1f2/Ofx/areacello/gn/latest/areacello_Ofx_UKESM1-0-LL_piControl_r1i1p1f2_gn.nc')


# In[104]:


epc_control_1 = dataset1['epc100']
epc_control_2 = dataset2['epc100']
area_data = area['areacello']


# In[105]:


epc_control_1_timeseries=((epc_control_1*area_data)*sec_to_yr*mol_to_g_C*g_to_Pg).sum(dim=['i','j'])
epc_control_2_timeseries=((epc_control_2*area_data)*sec_to_yr*mol_to_g_C*g_to_Pg).sum(dim=['i','j'])


# In[133]:


data=xr.concat([epc_control_1_timeseries.rolling(time=12, center=True).mean(),     epc_control_2_timeseries.rolling(time=12, center=True).mean()],dim='time')

data2=xr.concat([epc_control_1, epc_control_2],dim='time')


# calculate yearly averages using rolling function
data=data.rolling(time=12, center=True).mean()

data.plot(color = 'blue')
plt.ylim(8,10.5)
plt.xlabel('Time')
plt.ylabel('Exported Carbon (Pg / Year)')
plt.title('Control Data: 1960 - 2149')


# In[86]:


control_individual_epc = xr.Dataset(dict(epc_1 = epc_control_1_timeseries, epc_2 = epc_control_2_timeseries))
control_individual_epc.to_netcdf("control_epc.nc"[:]) 


# In[87]:


control_concat_epc = xr.Dataset(dict(epc = data))
control_concat_epc.to_netcdf("control_concat_epc.nc"[:]) 


# In[135]:


decadal_average_data = xr.Dataset(dict(epc = data2))
decadal_average_data.to_netcdf("decadal_average.nc"[:]) 


# In[91]:


control_individual_epc


# In[93]:


test = xr.open_mfdataset('/home/users/train047/control_epc.nc')


# In[94]:


test


# In[95]:


epc = test['epc_1']


# In[132]:


data2


# In[97]:


epc.plot()


# In[ ]:




