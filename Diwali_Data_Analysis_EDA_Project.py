#!/usr/bin/env python
# coding: utf-8

# # Diwali Data Analysis Project

# # Data Cleaning

# importing libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns 


# importing data through pandas library

# In[4]:


df = pd.read_csv("Diwali Sales Data.csv" , encoding = "unicode_escape")


# In[3]:


df.shape


# In[5]:


df.head(10)


# In[6]:


df.info()


# In[7]:


df.drop(["Status" , "unnamed1"] , axis = 1 , inplace = True) 


# In[8]:


df.info()


# In[9]:


pd.isnull(df)


# Checking for null values in data

# In[10]:


pd.isnull(df).sum()


# Deleting null values from data 

# In[14]:


df.dropna(inplace = True )


# In[15]:


pd.isnull(df).sum()


# In[16]:


df['Amount'] = df['Amount'].astype('int')


# In[17]:


df.dtypes


# In[18]:


df.columns


# In[19]:


df.describe()


# In[20]:


df[["Age" , "Orders" , "Amount"]].describe()


# # Exploratory Data Analysis 

# ### Gender

# In[22]:


x = sns.countplot(x  = "Gender" , data = df , palette = "rocket")
sns.set(rc = {'figure.figsize' :(6,3)})
plt.show()


# In[24]:


z = df.groupby(["Gender"],as_index = False)["Amount"].sum().sort_values(by = "Amount" , ascending = False)
sns.barplot(x = "Gender" , y ="Amount" , data  = z)
sns.set(rc = {'figure.figsize' :(6,3)})
plt.show()


# ##### Interpretation : From the above plot we can analyse that most of the buyers are Female and the purchasing power of the female is more as compared to male 

# ### Age

# In[25]:


y = sns.countplot(x = "Age Group" , data = df , hue = "Gender" , palette="rocket")


# In[26]:


# Age group and Amount spent
sales_age = df.groupby(['Age Group'] , as_index = False )['Amount'].sum().sort_values(by = "Amount" , ascending = False )
sns.barplot(x = "Age Group" , y ="Amount" , data  = sales_age)
plt.show()


# ##### Interpretation : From the above plot we can analyse that most of the buyers are from age group 26-35 and female

# ### State

# In[37]:


# Total number of Orders from Top-10 States

sales_state = df.groupby(["State"] , as_index = False ) ["Orders"].sum().sort_values(by = "Orders" , ascending = False ).head(10)
sns.set(rc ={"figure.figsize":(17,5)})
sns.barplot(x = "State" , y = "Orders" , data = sales_state)
plt.show()


# In[38]:


# Total Amount/Sales from Top-10 States

sales_state1 = df.groupby(['State'] , as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False ).head(10)
sns.set(rc = { 'figure.figsize' :(17, 5)})
sns.barplot(x = "State"  , y = "Amount" , data = sales_state1)
plt.show()


# ##### Interpretation : From above plot we can see that most of the orders as well as amount/sales are from Uttarpradesh , Maharashtra and Karnataka States

# ### Marital Status

# In[41]:


a = sns.countplot(x = "Marital_Status" , hue = "Gender", data = df)
sns.set(rc = {"figure.figsize" :(2,3)})


# In[43]:


sales = df.groupby(["Marital_Status" , "Gender"] , as_index= False)["Amount"].sum().sort_values(by = "Amount" , ascending = False )
sns.barplot(x = "Marital_Status" , y = "Amount" , hue = "Gender", data = sales)
plt.show()


# ##### Interpretation : From above graph we can analyse that most of the buyers are Married(Female) and they have high purchasing power

# ### Occupation

# In[45]:


a = sns.countplot(x = "Occupation" , data = df)
sns.set(rc = {"figure.figsize" :(20,5)})


# In[46]:


sales = df.groupby(["Occupation"] , as_index = False)["Amount"].sum().sort_values("Amount" , ascending = False)
sns.barplot(x = "Occupation"  , y = "Amount"   , data = sales ) 
plt.show()


# ##### Interpretaion : From the above graphs we can analyse that most of the buyers are working in IT , Healthcare , Aviation sector

# ### Product Category

# In[52]:


a = sns.countplot(x = "Product_Category", data = df)
sns.set(rc = {'figure.figsize' :(25,10)})
plt.show()


# In[53]:


sales = df.groupby(["Product_Category"] , as_index=False)["Amount"].sum().sort_values(by = "Amount" , ascending = False).head(10)
sns.barplot(x = "Product_Category" , y = "Amount" , data = sales) 
sns.set(rc = {'figure.figsize' :(20,12)})
plt.show()


# In[54]:


sales = df.groupby(["Product_Category"] , as_index = False)["Orders"].sum().sort_values("Orders" , ascending = False).head(10)
sns.barplot(x = "Product_Category" , y = "Orders" , data = sales )
plt.show()


# ##### Interpretation : From the above graphs we can analyse that most orders are from Clothing & Apparel and amount/sales are from food category

# #### CONCLUSION : Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




