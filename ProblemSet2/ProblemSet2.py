#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 2

# In[1]:


## The Standard Library


# In[2]:


## Question 1


# In[3]:


def listL(x = []):
    return [min(x), max(x), sum(x) / len(x)]

listL([1, 2, 3, 4, 5, 6, 500])


# In[4]:


## Question 2


# In[5]:


my_int = 1
my_int2 = my_int
my_int2 = 45
my_int2 == my_int
# The function returns false, so int is an immutable type 


# In[6]:


my_str = 'Paul'
my_str2 = my_str
my_str2 = 'Freed'
my_str2 ==  my_str
# The function returns false, so str is an immutable type 


# In[7]:


my_list = [1, 2, 3]
my_list2 = my_list
my_list2[2] = 500
my_list2==my_list
# The function returns true, so list must be a mutable type 


# In[8]:


my_tuple = (1, 2, 3)
my_tuple2 = my_tuple
my_tuple2[2] = 17
my_tuple2==my_tuple
# The fuction does not return true, so it must be immutable 


# In[9]:


my_set = {7,8,9}
my_set2 = my_set
my_set2[2] = 1 
my_set2 == my_set
# The fuction does not return true, so it must be immutable 


# In[10]:


# Question 3


# In[8]:


import PS2_calculatorR2 as calc 
import math as math

def hypotenusefinder(a,b):
    if a > 0:
        csquared = calc.sum_calc(calc.prod_calc(a,a), calc.prod_calc(b,b))
        hypo = math.sqrt(csquared)
        return(hypo)
    else:
        print("Something went wrong")
        
hypotenusefinder(2,3)


# In[12]:


# NUMPY INTRO


# In[13]:


# Question 1


# In[15]:


import numpy as np
A = np.array( [[3,-1,4],[1,5,-9]] )
B = np.array([[2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3]])
print(np.dot(A, B))


# In[16]:


# Question 2 


# In[17]:


A = np.array([[3,1,4],[1,5,9],[-5,3,1]])
print( (np.dot(A, A, A)*-1) + (9*np.dot(A,A)) - (15*A) )


# In[19]:


# Problem 5


# In[20]:


A = np.array([[0,2,4],[1,3,5]])
B = np.array([[3,0,0],[3,3,0],[3,3,3]])
C = np.array([[-2,0,0],[0,-2,0],[0,0,-2]])
A1 = np.vstack((np.zeros((3, 3)), A, B))
B1 = np.vstack((np.transpose(A), np.zeros((2, 2)), np.zeros((3, 2))))
C1 = np.vstack((np.eye(3), np.zeros((2, 3)), C))
FullBlock = np.hstack((A1, B1, C1))
print(FullBlock)


# In[1]:


##Part 3


# In[2]:


##Question 1 


# In[6]:


######Testing the Backpack
##See object_oriented_PS2

from object_oriented_PS2 import Backpack 
my_backpack = Backpack("Paul", "Blue")
type(my_backpack)

print(my_backpack.name, my_backpack.color)

my_backpack.name = "Fred"
print(my_backpack.name)


# In[7]:


##Question 2 


# In[ ]:


##See object_oriented_PS2

