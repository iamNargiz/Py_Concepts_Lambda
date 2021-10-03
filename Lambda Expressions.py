#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Lambda function with single argument
x = lambda a: a*a
print(x(5))


# In[2]:


#Lambda function with more than one argument
y = lambda a, b: a+b
print(y(4,6))


# In[3]:


#Exercise
L1=[-10, -4, 6, 8, -3, 7, 3, -9]
print('Original list: ')
print(L1)
result=sorted(L1, key = lambda i: 0 if i==0 else -1 / i)
print('Rearranged positive and negative numbers of the given list')
print(result)


# In[ ]:




