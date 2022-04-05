#!/usr/bin/env python
# coding: utf-8

# In[56]:


import requests
import json


response = requests.post('https://ies-midterm.soulution.rocks/login', data='{"cuni":"78225623"}')
print(response.text)


# In[57]:


ids = json.loads(response.text)['data']['dataset_ids']
for id in ids:
  response = requests.get(f'https://ies-midterm.soulution.rocks/data/{id}')
  print(response.text)
  time.sleep(10)


# In[65]:


import pandas as pd

ids = pd.DataFrame.groupby([["date", "company", "shares_traded"]]) #(ids, values="company", index="date")

ids = pd.DataFrame(ids)

print (ids)


# In[ ]:


import numpy as np

date_limitations = date["2019-01-02":"2020-11-20"]
sharestraded_max = shares_traded.npmax()
monthly_returns = shares_traded.npsum()/12

