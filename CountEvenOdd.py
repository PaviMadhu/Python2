#!/usr/bin/env python
# coding: utf-8

# In[1]:


series = int(input("Enter your number"))
oddno = 0
evenno = 0
for i in range(1,series+1): #It considers from 1 till user input
        if (i % 2)==0:
            evenno+=1
        else:
            oddno+=1
print("Number of even numbers :",evenno)
print("Number of odd numbers :",oddno)


# In[ ]:




