import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('bmh')

cols = ['maroon','goldenrod']
plt.figure(figsize=(12,5))
for i,filename in enumerate(['red','white']):

    a = pd.read_csv('../data/SS3_'+filename+'.csv',index_col='price')

    winenames = a['Name']
    del a['Name']
    del a['Averages']

    a.sort_index(inplace=True)
    a = a.T

    means = a.mean()
    stds = a.std()
    stderr = stds/np.sqrt(a.count())

    plt.errorbar(np.array(means.index),means,yerr=stderr,fmt='o',color=cols[i],label=filename)

plt.xlabel('Price')
plt.ylabel('Mean score')
plt.legend(loc=3)
plt.suptitle('Is more expensive wine better?',fontsize='x-large')
plt.savefig('score_vs_price.png')
