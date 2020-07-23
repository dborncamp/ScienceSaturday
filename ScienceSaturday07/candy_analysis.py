'''
Code to generate some analysis about the various candy tests.
'''

#Global
import pandas as pd
import matplotlib.pyplot as plt
import argparse

#YES, we will use the xkcd style.  
plt.xkcd()

def plot_candy(candy,colors):
    ''' 
    This function produces the analysis plots for a candy.
    '''

    tab = pd.read_csv(f'../data/SS7_{candy}.csv',index_col=0)

    #Plot distribution of entire sample
    dist = tab.groupby(['guesser','truth'])['truth'].count().unstack() 
    dist.sum().plot.bar(color=colors,
                        rot=70,
                        legend=None,
                        title=f'{candy.capitalize()} color distribution',
                        figsize=(8,5)
                        )   
    plt.ylabel('Number')
    plt.savefig(f'{candy}_sample_dist.png',bbox_inches='tight')
    plt.close()

    #Figure out the fraction correct by color.
    correct_frac_A = (tab.groupby(['guesser','truth'])['correct'].sum().unstack())/\
                   (tab.groupby(['guesser','truth'])['truth'].count().unstack())

    correct_frac_A.plot.bar(color=colors,
                            rot=70,
                            legend=None,
                            title=f'{candy.capitalize()} - Correct by color',
                            figsize=(12,5)
                            )
    plt.ylabel('Fraction')
    plt.savefig(f'{candy}_correct_by_color_A.png',bbox_inches='tight')
    plt.close()


    #Figure out the fraction correct by color.
    correct_frac_B = (tab.groupby(['truth','guesser'])['correct'].sum().unstack())/\
                   (tab.groupby(['truth','guesser'])['truth'].count().unstack())

    correct_frac_B.plot.bar(cmap='tab20',
                            rot=70,
                            title=f'{candy.capitalize()} - Correct by color',
                            figsize=(12,5)
                            )
    plt.legend(loc=2,fontsize='xx-small')
    plt.ylabel('Fraction')
    plt.savefig(f'{candy}_correct_by_color_B.png',bbox_inches='tight')
    plt.close()



    #Which color did people guess for each color.
    color_color = tab.groupby(['truth','guess'])['truth'].count().unstack().div(dist.sum(),axis=0)
    color_color.plot.bar(color=colors,
                         rot=70,
                         legend=None,
                         title=f'{candy.capitalize()} - Color guessed, by color',
                         figsize=(8,5)
                         )
    plt.ylabel('Fraction')
    plt.savefig(f'{candy}_colorbycolor.png',bbox_inches='tight')
    plt.close()

    return

def plot_all(opts):


    for keys in opts:

        plot_candy(opts[keys]['candy'],opts[keys]['colors'])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Can you taste the rainbow?')
    parser.add_argument('--candy',
                        type = str, 
                        default = None,
                        choices = ['all','skittles','starburst','gummybears'], 
                        help='Which plots to do you want to produce?')

    opts = {'skittles':{'candy':'skittles',
                        'colors':['g','darkorange','purple','r','gold']},
            'starburst':{'candy':'starburst',
                         'colors':['darkorange','pink','r','gold']},
            'gummybears':{'candy':'gummybears',
                          'colors':['green', 'darkorange', 'r', 'beige', 'gold']}
            }

    args = parser.parse_args()

    if args.candy == 'all':

        plot_all(opts)

    else:

        plot_candy(opts[args.candy]['candy'],opts[args.candy]['colors'])
