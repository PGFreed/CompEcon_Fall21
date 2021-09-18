#!/usr/bin/env python
# coding: utf-8

# # Problem Set 3
# #### Paul Freed
# #### Python Visualizations

# In[2]:


# A number of imports are required
import numpy as np
import pandas as pd
import plotly.express as px #This is required for all three visualizations 
import plotly.io as pio
import matplotlib.pyplot as plt
from urllib.request import urlopen
import kaleido #To write the figures to images 


# In[3]:


import json # This is nessecary in order to get json, which is how I can visualize the maps 
with urlopen('https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_500k.json') as response:
    state_map_data = json.load(response)
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


# In[4]:


SocialCapital = pd.read_excel(r'\Users\MSB\Desktop\IdeaTesting\StateLevelSC.xlsx') # This is for the broad state-level perspective
PPPdata = pd.read_excel (r'\Users\MSB\Desktop\IdeaTesting\CountyPPP.xls', dtype={"fips": str}) #FIPS must be entered as a string or else several states will be dropped


# #### Visualization 1: Social Capital in the USA

# In[5]:


fig_State = px.choropleth_mapbox(SocialCapital, geojson=state_map_data,
                           locations="State",  # Column name showing location
                           featureidkey="properties.NAME",   # This is the corresponding location in the JSON file
                           color='State-Level Index', # Higher values represent more social capital
                           color_continuous_scale="Viridis", #This is color scale 
                           mapbox_style="carto-positron",
                           zoom=2, center = {"lat": 39.50, "lon": -98.35}, #I googled the exact center of the US
                           opacity=1,
                           title='Social Capital Across America: States'
                          )
fig_State.show()


# In[6]:


fig_County = px.choropleth(PPPdata, geojson=counties, locations='fips', color='CountyLevelIndex', #Same as the state index but uses counties 
                           color_continuous_scale="Viridis", #Same color scale as states 
                           range_color=(-1, 1),
                           scope="usa",
                           title='Social Capital Across America: Counties'
                          )

fig_County.show()


# In[7]:


plotdata = PPPdata
figDens = px.histogram(plotdata['Forgiveness'], #Plots the distribution of PPP loan forgiveness rates by county
             title='Distribution of PPP Loan Forgiveness Rates',
             opacity=1)
figDens.show()


# In[12]:


figSC = px.scatter(plotdata, x='Forgiveness', y='CountyLevelIndex', #Forgiveness is the percentage of total PPP loans in a county that are forgiven
           title="Social Capital and Loan Forgiveness",
           opacity=0.7, trendline = 'ols', color = 'CommunityBanking') #The higher the color the greater the proportion of community banks to large banks in a county
figSC.show() #This shows the plot in the script


# In[17]:


figHHI = px.scatter(plotdata, x='Forgiveness', y='HHI', #The Herfindahl-Hirschman index is a proxy for the competitiveness of the banking market
           title="HHI and Loan Forgiveness",
           opacity=0.7, trendline = 'ols', color = 'CommunityBanking') #The higher the color the greater the proportion of community banks to large banks in a county
figHHI.show() #This shows the plot in the script


# In[ ]:


cd "\Users\MSB\Desktop\IdeaTesting" #This is the folder I want these to be sent to


# In[18]:


fig_County.write_html('CountyMap.html') #These first two lines write to HTML
fig_State.write_html('StateMap.html')
fig_County.write_image('CountyMap.png')# The remaining lines write the figures to PNG files in the folder I want 
fig_State.write_image('StateMap.png')
figDens.write_image('figDens.png')
figSC.write_image('figSC.png')
figHHI.write_image('figHHI.png')


# In[10]:





# In[ ]:





# In[ ]:





# In[ ]:




