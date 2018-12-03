'''
Plotting the data from the 2nd STScI Science Saturday.
This plots the mean scores for each beer.
'''
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##Making fake data to get things started
a = pd.read_csv('../data/SS2_beerScores.csv',index_col='Beer Name')

del a['Beer Letter']

means = df.mean()
stds = df.std()
means.sort_values(inplace=True)

#plotting stuff
matplotlib.style.use('bmh')

means.plot.bar(yerr=stds,figsize=(12,5),color='dodgerblue')
plt.suptitle('What is the best shitty beer?',fontsize='x-large')
plt.ylim(0,5)
plt.xticks(rotation=45,fontsize='large',horizontalalignment='right')
plt.savefig('scores_by_beer.png',bbox_inches='tight')
