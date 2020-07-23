import pandas as pd
import matplotlib.pyplot as plt

plt.xkcd()

tab = pd.read_csv('../data/SS7_skittles.csv',index_col=0)
colors = ['g','darkorange','purple','r','gold']

#Plot distribution of entire sample
dist = tab.groupby(['guesser','truth'])['truth'].count().unstack() 
dist.sum().plot.bar(color=colors,
                    rot=70,
                    legend=None,
                    title='Skittles color distribution',
                    figsize=(7,5)
                    )
plt.ylabel('Number')
plt.savefig('skittles_sample_dist.png',bbox_inches='tight')
plt.close()

#Figure out the fraction correct by color.
correct_frac_A = (tab.groupby(['guesser','truth'])['correct'].sum().unstack())/\
               (tab.groupby(['guesser','truth'])['truth'].count().unstack())

correct_frac_A.plot.bar(color=colors,
                        rot=70,
                        legend=None,
                        title='Skittles - Correct by color',
                        figsize=(10,5)
                        )
plt.ylabel('Fraction')
plt.savefig('skittles_correct_by_color_A.png',bbox_inches='tight')
plt.close()

#Figure out the fraction correct by color.
correct_frac_B = (tab.groupby(['truth','guesser'])['correct'].sum().unstack())/\
               (tab.groupby(['truth','guesser'])['truth'].count().unstack())

correct_frac_B.plot.bar(cmap='tab20',
                        rot=70,
                        title='Skittles - Correct by color',
                        figsize=(10,5)
                        )
plt.legend(loc=2,fontsize='xx-small')
plt.ylabel('Fraction')
plt.savefig('skittles_correct_by_color_B.png',bbox_inches='tight')
plt.close()

#Which color did people guess for each color.
color_color = tab.groupby(['truth','guess'])['truth'].count().unstack().div(dist.sum(),axis=0)
color_color.plot.bar(color=colors,
                     rot=70,
                     legend=None,
                     title='Skittles - Color guessed, by color',
                     figsize=(7,5)
                     )
plt.ylabel('Fraction')
plt.savefig('skittles_colorbycolor.png',bbox_inches='tight')
plt.close()
