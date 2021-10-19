#!/usr/bin/env python
# coding: utf-8

# In[112]:


import pandas as pd
import numpy as np
import scipy.optimize as opt 
from scipy.optimize import minimize 
from scipy.optimize import differential_evolution #I couldn't get this to work
from geopy.distance import geodesic #This is to calculate distance 


# In[2]:


PS5=pd.read_csv(r'\Users\MSB\Downloads\radio_merger_data.csv')

PS5['Price'] = np.log(1+PS5['price']) #To enhance interpretability I log transform the variables accounting for possible zeros
PS5['Population'] = np.log(1+PS5['population_target']) 

market1 = len(PS5[(PS5['year']<2008)]) #Here I calculate the size of each market in order to iterate through one and then start on the other 
market2 = len(PS5[(PS5['year']>2007)])


# In[3]:


#


# In[4]:


#


# #### I tried making a multiple different arrays for each f(b,t) set, but that didn't work so I made the big array with all the factors combined

# In[105]:


"""b is the characteristics of the of the radio station buyer (number of stations and indicator)
t is the characteristics of the target market (population)

b'=b+1, t'=t+1

I will need the distance, the number of stations owned by the parent company, 
the population in the market, and the indicator for ownership for the first analysis,
then HHI and price for the second

f(b,t) = (number)*(population) + (indicator)*(population) + (buyer location and target location) 
f(b',t) = (number')*(population) + (indicator')*(population) + (buyer location' and target location)
f(b,t') = (number)*(population') + (indicator)*(population') + (buyer location and target location') 
f(b',t') = (number')*(population') + (indicator')*(population') + (buyer location' and target location') 

I also have price and HHI
Here I generate each component, adding one for the primes

In the end, I could never get the right number of observed matches and counterfactuals"""


market = market1 
year = 2007  #only two years
r1 = 1 #start with first obs 

fbt = np.empty((0, 16))

#the conditional loops
for year in range(2007,2009):
    for bt in range(1,market): #I want to stop once I hit the length of the yearly market
        if r1 <= market:
            r2 = 1 
            for r2 in range(1, market): #Stop once the market length is hit
                if r2 <= market - r1:

                    numpop1 = PS5.iloc[r1-1, 9] * PS5.iloc[r1-1, 12]         #0  (number)*(population)
                    numpop2 = PS5.iloc[r1+r2-1, 9] * PS5.iloc[r1+r2-1, 12]   #1  (number')*(population')
                    numpop3 = PS5.iloc[r1-1, 9] * PS5.iloc[r1+r2-1, 12]      #2  (number)*(population')
                    numpop4 = PS5.iloc[r1+r2-1, 9] * PS5.iloc[r1-1, 12]      #3  (number')*(population)
                    
                    corpop1 = PS5.iloc[r1-1, 11] * PS5.iloc[r1-1, 12]        #4  (indicator)*(population) 
                    corpop2 = PS5.iloc[r1+r2-1, 11] * PS5.iloc[r1+r2-1, 12]  #5  (indicator')*(population')
                    corpop3 = PS5.iloc[r1-1, 11] * PS5.iloc[r1+r2-1, 12]     #6  (indicator)*(population')
                    corpop4 = PS5.iloc[r1+r2-1, 11] * PS5.iloc[r1-1, 12]     #7  (indicator')*(population)
                    
                    geo1 = (PS5.iloc[r1-1, 3], PS5.iloc[r1-1, 4]) 
                    geo2 = (PS5.iloc[r1-1, 5], PS5.iloc[r1-1, 6])
                    geo3 = (PS5.iloc[r1+r2-1, 3], PS5.iloc[r1+r2-1, 4])
                    geo4 = (PS5.iloc[r1+r2-1, 5], PS5.iloc[r1+r2-1, 6])
                    
                    distance1 = geodesic(geo1, geo2).miles                   #8  (buyer location and target location)
                    distance2 = geodesic(geo3, geo4).miles                   #9  (buyer location' and target location') 
                    distance3 = geodesic(geo1, geo4).miles                   #10  (buyer location' and target location)
                    distance4 = geodesic(geo2, geo3).miles                   #11  (buyer location and target location')
                    
                    price1 = PS5.iloc[r1-1, 13]                              #12 (Price) 
                    price2 = PS5.iloc[r1+r2-1, 13]                           #13 (Price')
                    
                    HHI1 = PS5.iloc[r1-1, 8]                                 #14  (HHI)
                    HHI2 = PS5.iloc[r1+r2-1, 8]                              #15  (HHI')
                    

                    actualdata = np.array([numpop1, numpop2, numpop3, numpop4, corpop1, corpop2, corpop3, corpop4, distance1,  distance2,  distance3,  distance4, price1, price2, HHI1, HHI2])
                    fbt = np.append(fbt, [actualdata], axis=0)
                    r2 = r2 + 1 #next obs 

            r1 = r1 + 1 #next observation
    market = market + market2 
    year = year + 1 #from 2007 to 2008

print(fbt)


# In[107]:


#


# In[10]:


#


# In[11]:


#


# In[12]:





# In[108]:


def estimator(params, fbt):
    
    Beta0 = params[0] 
    Beta1 = params[1]

    sum = 0
    r3 = 0 #first obs
    for r3 in range(0,len(fbt)-1): #stop after all the obs 
        
        
        #The first side of the inequality of Equation 10 of the notes
        
        
        fbtform = fbt[r3, 0] + Beta0 * fbt[r3, 4] + Beta1 * fbt[r3, 8] + fbt[r3, 1] + Beta0 * fbt[r3, 5] + Beta1 * fbt[r3, 9]
        
        
        #The second side of the inequality of Equation 10 of the notes
        
        
        fprimesform = fbt[r3, 3] + Beta0 * fbt[r3, 7] + Beta1 * fbt[r3, 11] + fbt[r3, 2] + Beta0 * fbt[r3, 6] + Beta1 * fbt[r3, 10]
        
        
    
        if fbtform > fprimesform :
            
            sum = sum - 1

        r3 = r3 + 1
        
        print(sum)
    return sum

guess = [1, 1] 
answers = opt.minimize(estimator, guess, fbt, method = 'Nelder-Mead')
print(answers)


# In[35]:


#


# In[115]:


def estimator2(params, fbt):
    
    Beta0 = params[0]
    Beta1 = params[1]
    Beta2 = params[2] 
    Beta3 = params[3]

    
    
    sum = 0
    r4 = 0 #First obs 
    while(r4 <= len(fbt)-1):  #stop after all the obs 
        
        
        #The first side of the inequality of Equation 11 of the notes, but I try to account for price and HHI 

        fbtform = Beta3 * fbt[r4, 0] + Beta0 * fbt[r4, 4] + Beta1 * fbt[r4, 8] + fbt[r4, 1] + Beta0 * fbt[r4, 5] + Beta1 * fbt[r4, 9] + Beta2 * fbt[r4, 14] - fbt[r4, 12] + fbt[r4, 13]                                                                           
        
        #The first side of the inequality of Equation 11 of the notes, but I try to account for price and HHI
        
        fprimesform = Beta3 * fbt[r4, 3] + Beta0 * fbt[r4, 7] + Beta1 * fbt[r4, 11] + fbt[r4, 2] + Beta0 * fbt[r4, 6] + Beta1 * fbt[r4, 10] + Beta2 * fbt[r4, 15] - fbt[r4, 12] + fbt[r4, 13]
        
        
        if fbtform > fprimesform:
            
            sum = sum - 1

        r4 = r4 + 1
        
        
        print(sum)
    return sum

guess = [1, 1, 1, 1]
answers = opt.minimize(estimator2, guess, fbt, method = 'Nelder-Mead')
print(answers)


# In[ ]:




