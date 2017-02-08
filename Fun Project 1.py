
# coding: utf-8

# # Fun Project 1 - Rand Terrorism Database
# 

# In[12]:

import pandas as pd
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
plotly.tools.set_credentials_file(username='cneves4', api_key='YI7E2Dxy7g63cjKdD3Tk')


# # Data Wrangling

# In[37]:

#import rand dataset 
#source: RAND Database of Worldwide Terrorism Incidents
data = pd.read_excel('rand.xls')
data.head()


# In[38]:

data = data[['Date', 'City','Country', 'Perpetrator', 'Weapon', 'Injuries', 'Fatalities']]
data.head()


# # Plotting

# 1) # of Attacks in US Soil by Year

# In[39]:

#separate dates
#test set
data['Year'] = data['Date'].apply(lambda x: x.strftime('%Y'))     
data['Month'] = data['Date'].apply(lambda x: x.strftime('%m'))     
data['Day'] = data['Date'].apply(lambda x: x.strftime('%d'))     
data.head()


# In[9]:

data_us = data[data['Country'] == 'United States']
data_us.head()


# In[14]:

data_us['Total Injuries'] = data_us.groupby('Year')['Injuries'].transform(np.sum)
data_us['Total Fatalities'] = data_us.groupby('Year')['Fatalities'].transform(np.sum)

data_us.head()


# In[15]:

data_us = data_us.drop_duplicates(['Year'], keep = 'first')
data_us.head()


# In[19]:

trace0 = go.Scatter(
    x = data_us['Year'],
    y = data_us['Total Fatalities'],
    mode = 'lines',
    name = 'Fatalities',
    textfont=dict(size=7)
)

trace1 = go.Scatter(
    x = data_us['Year'],
    y = data_us['Total Injuries'],
    mode = 'lines',
    name = 'Injuries',
    textfont=dict(size=7)
)

layout = go.Layout(
    title ='Number of Injuries and Fatalities from Terror Attacks in US Soil by Year',
    titlefont = dict(size=12),
    showlegend=True,
    xaxis=dict(
        title= 'Year',
        titlefont=dict(size=0),
    ),
    yaxis=dict(
        title= '#',
        titlefont=dict(size=10),
    )
)

data = [trace0, trace1]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Terror Attacks on US Soil')


# 2) # of Attacks in Turkish Soil by Year

# In[40]:

data_tr = data[data['Country'] == 'Turkey']
data_tr.head()


# In[41]:

data_tr['Total Injuries'] = data_tr.groupby('Year')['Injuries'].transform(np.sum)
data_tr['Total Fatalities'] = data_tr.groupby('Year')['Fatalities'].transform(np.sum)

data_tr.head()


# In[42]:

data_tr = data_tr.drop_duplicates(['Year'], keep = 'first')
data_tr.head()


# In[43]:

trace0 = go.Scatter(
    x = data_tr['Year'],
    y = data_tr['Total Fatalities'],
    mode = 'lines',
    name = 'Fatalities',
    textfont=dict(size=7)
)

trace1 = go.Scatter(
    x = data_tr['Year'],
    y = data_tr['Total Injuries'],
    mode = 'lines',
    name = 'Injuries',
    textfont=dict(size=7)
)

layout = go.Layout(
    title ='Number of Injuries and Fatalities from Terror Attacks in Turkish Soil by Year',
    titlefont = dict(size=12),
    showlegend=True,
    xaxis=dict(
        title= 'Year',
        titlefont=dict(size=0),
    ),
    yaxis=dict(
        title= '#',
        titlefont=dict(size=10),
    )
)

data = [trace0, trace1]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Terror Attacks on Turkish Soil')


# Now looking by perpetrator...

# In[44]:

data_tr_perp = data_tr.groupby(['Year', 'Perpetrator']).size().unstack(fill_value=0)

data_tr_perp.head()


# In[49]:

data_tr_perp['Year'] = data_tr_perp.index
data_tr_perp = data_tr_perp.reset_index(drop=True)
data_tr_perp.head()


# In[51]:

trace0 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Abu Nidal Organization (ANO)'],
    mode = 'lines',
    name = 'Abu Nidal Organization (ANO)',
    textfont=dict(size=7)
)

trace1 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Amal'],
    mode = 'lines',
    name = 'Amal',
    textfont=dict(size=7)
)

trace2 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Armenian Revolutionary Army'],
    mode = 'lines',
    name = 'Armenian Revolutionary Army',
    textfont=dict(size=7)
)

trace3 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Black September'],
    mode = 'lines',
    name = 'Black September',
    textfont=dict(size=7)
)

trace4 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Dev Sol'],
    mode = 'lines',
    name = 'Dev Sol',
    textfont=dict(size=7)
)

trace5 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Great Eastern Islamic Raiders Front (IBDA-C)'],
    mode = 'lines',
    name = 'Great Eastern Islamic Raiders Front (IBDA-C)',
    textfont=dict(size=7)
)

trace6 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Hizballah'],
    mode = 'lines',
    name = 'Hizballah',
    textfont=dict(size=7)
)

trace7 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Justice Commandos for the Armenian Genocide'],
    mode = 'lines',
    name = 'Justice Commandos for the Armenian Genocide',
    textfont=dict(size=7)
)

trace8 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Kurdish Workers Party'],
    mode = 'lines',
    name = 'Kurdish Workers Party',
    textfont=dict(size=7)
)

trace9 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Kurdish Workers Party (PKK)'],
    mode = 'lines',
    name = 'Kurdish Workers Party (PKK)',
    textfont=dict(size=7)
)

trace10 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Mahir Cayan Suicide Group'],
    mode = 'lines',
    name = 'Mahir Cayan Suicide Group',
    textfont=dict(size=7)
)

trace11 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Other'],
    mode = 'lines',
    name = 'Other',
    textfont=dict(size=7)
)


trace12 = go.Scatter(
    x = data_tr_perp['Year'],
    y = data_tr_perp['Unknown'],
    mode = 'lines',
    name = 'Unknown',
    textfont=dict(size=7)
)
                
layout = go.Layout(
    title ='Number of  Terror Attacks in Turkish Soil by Year and Perpetrator',
    titlefont = dict(size=12),
    showlegend=True,
    xaxis=dict(
        title= 'Year',
        titlefont=dict(size=0),
    ),
    yaxis=dict(
        title= '#',
        titlefont=dict(size=10),
    )
)

data = [trace0, trace1, trace2, trace3,trace4,trace5,trace6,trace7,trace8,trace9,trace10,trace11,trace12]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Terror Attacks on Turkish Soil by Perp')


# In[ ]:



