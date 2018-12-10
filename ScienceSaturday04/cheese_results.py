import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('bmh')

f1  = pd.read_excel('cheese_results.xlsx',header=0,usecols='C:K')

pizzas = ['Pappa John\'s','Pizza Boli\'s','Digiorno','Little Caesar\'s','Dominos','Pizza Hut','Pizza Hut Stuffed Crust']
categories = ['Sauce','Cheese','Greasiness','Crust','Overall','Chain Guess']
arrays = [list(np.repeat(pizzas,6)),categories*7]
tuples = list(zip(*arrays))
mux = pd.MultiIndex.from_tuples(tuples, names = ['Brand','category'])

tab1 = pd.DataFrame(f1.values,index=mux,columns=f1.columns.values)

scores = tab1.xs('Overall',level='category').mean(axis=1)
scores = scores.sort_values()
errs = tab1.xs('Overall',level='category').std(axis=1)

plt.figure(figsize=(12,5))
scores.plot(kind='bar',
            ylim=[0,5.1],
            yerr=errs,
            color='dodgerblue',
            rot=45.,
            title='Cheese pizza overall scores'
            )
   
plt.savefig('SS4_cheese_overall_scores.png',bbox_inches='tight')


