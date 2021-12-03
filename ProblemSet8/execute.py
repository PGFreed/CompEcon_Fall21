


# In[92]:

#Packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import fminbound
import scipy.optimize as opt
import random
import functions
from functions import bellmanoperator, utility




# In[93]:


beta = 0.95 #Discount 
delta = 0.8525 #Static Natural Ability (Financial Literacy)
phi = 0.95 #Static Information Access 
time = 1 #A function of time


# In[94]:


#Grid Params
lb_f = 0.4 
ub_f = 2.0 
size_f = 200  # Grid Points
f_grid = np.linspace(lb_f, ub_f, size_f)


# In[97]:

VFtol = 1e-5
VFdist = 7.0 
VFmaxiter = 5000 
V = np.zeros(size_f)#The guess at the value fuction
Vstore = np.zeros((size_f, VFmaxiter)) 

'''The following iterates through the value function. 
Here I also apply the defintion of time such that after each iteration
I get a higher value, which has its implications for the utility function.'''
VFiter = 1 
while VFdist > VFtol and VFiter < VFmaxiter:
    Vstore[:, VFiter] = V
    TV, optf = bellmanoperator(V, f_grid, beta)
    VFdist = (np.absolute(V - TV)).max()  #A function to check the distance
    print('ITERATION ', VFiter, ', DISTANCE = ', VFdist)
    V = TV
    VFiter += 1
    time = time + 1 #Here the loop for time, adding one for each period

if VFiter < VFmaxiter:
    print('CONVERGED AFTER:', VFiter)
else:
    print('DID NOT CONVERGE')            


VF = V 




# In[85]:

# VALUE FUNCTION ACROSS ITERATIONS

plt.figure()
fig, ax = plt.subplots()
ax.plot(f_grid, Vstore[:,1], label='1st')
ax.plot(f_grid, Vstore[:,20], label='20th')
ax.plot(f_grid, Vstore[:,50], label='50th')
ax.plot(f_grid, Vstore[:,100], label='100th')
ax.plot(f_grid, Vstore[:,200], label='200th')
ax.plot(f_grid, Vstore[:,VFiter-1], 'k', label='Final')

#Legend Additions
legend = ax.legend(loc='best', shadow=True)
for label in legend.get_texts():
    label.set_fontsize('small')
for label in legend.get_lines():
    label.set_linewidth(2) 
plt.xlabel('Information')
plt.ylabel('Value Function')
plt.title('Investor Decision Making ')
plt.show()


# In[ ]:

#STATIC VALUE FUNCTION
plt.figure()
plt.plot(f_grid[1:], VF[1:])
plt.xlabel('Information')
plt.ylabel('Value Function')
plt.title('Investor Decision Making ')
plt.show()



# In[87]:


optW = f_grid - (optf * beta)


# In[90]:
# POLICY FUNCTION

plt.figure()
fig, ax = plt.subplots()
ax.plot(f_grid[1:], optW[1:], label='Studying')
# Now add the legend with some customizations.
legend = ax.legend(loc='lower right', shadow=True)

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('small')
for label in legend.get_lines():
    label.set_linewidth(2)  # the legend line width
plt.xlabel('Information')
plt.ylabel('Studying Optimization')
plt.title('Policy Function')
plt.show()


# In[ ]:



