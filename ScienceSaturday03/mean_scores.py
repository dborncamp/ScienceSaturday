'''
Script to make figure 1 of Science Saturday 3.
The output is the PNG file
SS02_01.png
'''

#Imports
import matplotlib.pyplot as plt
import matplotlib
from ipywidgets import interact
import pandas as pd

plt.xkcd()

#Reading in the data and cleaning up a little
red = pd.read_csv('../data/SS3_red.csv',index_col='price')
del red['Name']
del red['Averages']
red.sort_index(inplace=True)

wht = pd.read_csv('../data/SS3_white.csv',index_col='price')
del wht['Name']
del wht['Averages']
wht.sort_index(inplace=True)

ax = red.mean(axis=1).plot(yerr=red.std(axis=1),figsize=(12,5),marker='.',markersize=15,color='maroon',label='Red wine')
ax = wht.mean(axis=1).plot(ax=ax,marker='.',yerr=wht.std(axis=1),markersize=15,color='goldenrod',label='White wine')
ax.set_title('Average scores',fontsize='x-large')
ax.set_xlabel('Price [$]',fontsize='medium')
ax.set_ylabel('Rating',fontsize='medium')
ax.set_ylim(0.5,5.5)
ax.legend()
plt.savefig('SS02_01.png',bbox_inches='tight')
