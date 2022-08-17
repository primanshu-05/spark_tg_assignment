#!/usr/bin/env python
# coding: utf-8

# # Problem 1. The client wants that no customer should wait before their call is attended. So how many minimum agents should be employed so that all customer calls are answered immediately, and no customer waits?

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#reading the data
call_data=pd.read_csv("Calls data (1).csv")
call_data


# In[3]:





# In[4]:


# call_data['duration_of_call_seconds']=call_data['duration_of_call_seconds']/60
# call_data['duration_of_call_seconds']call_data['start_time'] = call_data['time_of_call']
call_data['end_time'] = call_data['time_of_call'] + call_data['duration_of_call_seconds']/60
call_data_new = call_data.convert_dtypes()
call_data_new


# In[11]:


#Data transformation- adding a column for end call time with help of start time and duration of call(in minutes)
call_id_start_end_time = call_data_new.drop(columns=['time_of_call','duration_of_call_seconds'])
call_id_start_end_time


# In[13]:


#trying to find how many calls were engaged at every minute of the day
MyList = []
for idx in call_id_start_end_time.index:
    for i in range(call_id_start_end_time['start_time'][idx], call_id_start_end_time['end_time'][idx]):
        MyList.append(i)


# In[70]:


my_dict= {i:MyList.count(i) for i in MyList}
my_dict


# In[15]:


#fetching out the particular minute at which max calls were engaged.
#O/P says at 685th minute max call were 134 in position.
fin_max = max(my_dict, key=my_dict.get)
print("Maximum value:",fin_max)


# ##A total 134 number of agents are needed so that no customer has to wait at any particular time

# # Problem 2. The client doesn't want the customer to wait more than twenty minutes, so how many minimum agents should be employed so that maximum wait time for a customer is within twenty minutes?

# In[ ]:


#1st free agents to be taken at any particular minute
##free_agents=np.repeat(99,10000)
#time of call and duration of call to be initialize from 1st call
#z- as wait time at any particular minute
#max. wait time at initial call is to be taken as 0
#change the minimum agents (currently as 99) to get maximum wait time with those number of agents.


# In[72]:


free_agents=np.repeat(99,10000)
max_wait_time = 0
for i in call_data.index:
    start_time= call_data['time_of_call'][i]                            
    call_dur= int(call_data['duration_of_call_seconds'][i]/60)                        
    #z- wait time
    z = 0
    flag1 = 0                                         
    #j as minute counter
    for j in range(start_time,1404):                           
        free_agents[j] = free_agents[j]-1                                 
        if free_agents[j]<0 and flag1 == 0:
            z = z+1
            call_dur = call_dur+1

        if free_agents[j]>=0 and flag1 == 0:
            flag1 = 1                                

        if call_dur == 1:
            if z>max_wait_time:
                max_wait_time = z
            break
        j = j+1
        call_dur = call_dur-1


# In[73]:


max_wait_time


# ## it's clear that when agents were taken as 99 maximum wait time is 18 minutes whereas when agents are 98 in number maximum wait time is 21 minutes.
# ## Hence 99 is minimum number of agents should be employed so that maximum wait time for a customer is within twenty minutes

# # Problem 3. Create a time histogram plot with time interval of 15 minutes which plots number of calls that happen in every 15 minutes using Calls data.csv

# In[110]:


#each bin represents 15 minutes
plt.hist(call_data['time_of_call'],bins=96,facecolor='green', edgecolor='black')

plt.xlabel('Time of calls')
plt.ylabel('No. of calls')


# In[ ]:




