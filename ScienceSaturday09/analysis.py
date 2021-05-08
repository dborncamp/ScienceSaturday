import pandas as pd
import matplotlib.pyplot as plt
from util import get_data
from tabulate import tabulate

plt.xkcd()

tab,cat = get_data()

#Extract a data frame of the Alcoholic guesses.
d = {'True':True,'False':False}
alkyguess = tab.loc[(slice(None),'Alcoholic'),:].copy()
for name in alkyguess.columns:
    alkyguess[name] = alkyguess[name].map(d)

correct = alkyguess.eq(cat['Alcoholic'].values,axis=0)
correct = correct.droplevel('Info')
alk_y = correct.loc[cat[cat['Alcoholic']].index]
alk_n = correct.loc[cat[~cat['Alcoholic']].index]


f1 = open('results.tables','w')

f1.write(f'Overall accuracy: {100*correct.sum().sum()/correct.size:3.1f}%\n')
f1.write(f'\tAlcoholic: {100*alk_y.sum().sum()/alk_y.size:3.1f}%\n')
f1.write(f'\tNon-alcoholic: {100*alk_n.sum().sum()/alk_n.size:3.1f}%\n\n')

f1.close()

resultstab = pd.concat([alk_y,alk_n])
by_drinker = 100*resultstab.sum(axis=0)/20
by_beer = 100*resultstab.sum(axis=1)/6
clist = 10*['dodgerblue']+10*['gold']


#Figure 1 - Accuracy by drinker
fig1,ax = plt.subplots(1,1,figsize=(10,10))

by_beer.plot(kind='barh',color=clist,ax=ax,title='Accuracy by beer')
ax.set_yticklabels(ax.get_yticklabels(),ha='right',fontsize='small')
ax.invert_yaxis()
ax.set_xlabel('Accuracy [%]',fontsize='small')

fig1.tight_layout()
fig1.savefig('accuracy_beer.png',dpi=300)
plt.close(fig1)

#Figure 2 - Accuracy by drinker
fig2,ax = plt.subplots(1,1,figsize=(10,10))

by_drinker.plot(kind='barh',color='k',ax=ax,title='Accuracy by drinker')
ax.set_yticklabels(ax.get_yticklabels(),ha='right')
ax.set_xlabel('Accuracy [%]')

fig2.tight_layout()
fig2.savefig('accuracy_drinkers.png',dpi=300)
plt.close(fig2)


#######################################################################
#In this section we will try to get the rating of the beers.

#Extract the ratings data
ratings = tab.loc[(slice(None),'Rating'),:].copy()
ratings = ratings.droplevel('Info')
alk_y = ratings.loc[cat[cat['Alcoholic']].index]
alk_n = ratings.loc[cat[~cat['Alcoholic']].index]

ratings = pd.concat([alk_y,alk_n])

#Figure 3 - Accuracy by drinker
fig3,ax = plt.subplots(1,1,figsize=(10,10))

ratings.mean(axis=1).plot(xerr=ratings.std(axis=1),kind='barh',color=clist,ax=ax,title='Average ratings')
ax.set_yticklabels(ax.get_yticklabels(),ha='right',fontsize='small')
ax.invert_yaxis()
ax.set_xlabel('Score',fontsize='small')

fig3.tight_layout()
fig3.savefig('beer_ratigs.png',dpi=300)
plt.close(fig3)

