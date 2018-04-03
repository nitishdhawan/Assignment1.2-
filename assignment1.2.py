
# coding: utf-8

# In[15]:


numbers=filter(lambda x: x%7==0 and x%5!=0, range(2000,3201))


# In[16]:


numbers_1=[]
for k in numbers:
    numbers_1.append(k)
print(numbers_1)

