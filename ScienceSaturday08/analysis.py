'''
Code to do some analysis on the Octoberfest data.
'''

#Global
import pandas as pd
import matplotlib.pyplot as plt

#YES, we will use the xkcd style.  
plt.xkcd()

def overall():

    a = pd.read_csv('../data/SS8_octoberfest.csv')

    b = pd.DataFrame(list(zip(a.groupby('Beer')['Rating'].mean().array,a.groupby('Beer')['Rating'].std().array)),
                     index=a['Beer'].unique(),columns=['mean','std'])

    b.sort_values(by='mean',inplace=True)

    fig,ax = plt.subplots(1,1,figsize=(12,5))

    b.plot(kind='bar',y='mean',yerr='std',legend=False,
           ylabel='Score',xlabel='Brand',title='Oktoberfest',
          fig=fig,ax=ax)

    ax.set_xticklabels(ax.get_xticklabels(),rotation=60, ha='right')

    plt.savefig('oktoberfest.png',bbox_inches='tight')


if __name__ == "__main__":

    overall()

