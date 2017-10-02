
# coding: utf-8

# In[20]:

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib

import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')

import numpy as np

import pandas as pd


# In[21]:

#reading the WHO data used previously in this course
#regions are Africa, Europe, Americas, Eastern Mediterranean, South-East Asia, Western Pacific
who_df = pd.read_csv('../data/WHO.csv')


# In[22]:

#Parsing the dataset down into the relevant columns 
who_df= who_df[['Region','Country','Population']]


# In[23]:

#Setting Region as the index as that is how I am sorting them
who_df=who_df.set_index('Region')


# In[29]:

print ("Please enter a region.")
print ("Africa, Europe, Americas, Eastern Mediterranean, South-East Asia, or Western Pacific are your choices.")


# In[24]:

#returning the data for the entered region
who_df=who_df.loc[input(), : ]


# In[25]:

#print bar graph using data for the inputed region
who_df.plot.bar(x='Country',y='Population',title='Region Population Comparison',legend=False)

