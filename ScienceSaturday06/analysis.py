'''
Code to do analysis of Cookies data.
'''

#Global
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
import argparse
import numpy as np

#As always, we use xkcd style around these parts.
plt.xkcd()

def plot_characteristic(characteristic):

    '''
    Function to make plot of a given cookie characteristic.

    Supported characteristics:

    Appearance
    Bite
    ChocolateFlavor
    Moistness
    PersonalPreference
    Sweetness
    '''

    opts = {'Appearance': {'xlims':[1,3],
                           'xlabels':['Probably not','Would eat','Martha Stewart'],
                           'colors' : {1:'tomato', 2:'gold', 3:'seagreen'}
                           },
            'Bite': {'xlims':[1,4],
                     'xlabels':['Very crunchy','Crunchy','Chewy','Cakey'],
                     'colors' : {1:'tomato', 2:'darkorange', 3:'gold', 4:'seagreen'},
                     },
            'ChocolateFlavor': {'xlims':[1,3],
                                'xlabels':['Not choc.','Choc.','Too (very) choc.'],
                                'colors' : {1:'tomato', 2:'gold', 3:'seagreen'}
                                },
            'Moistness': {'xlims':[1,3],
                          'xlabels':['Dry','Neutral','Moist'],
                          'colors' : {1:'tomato', 2:'gold', 3:'seagreen'}
                          },
            'PersonalPreference': {'xlims':[0,5],
                                   'xlabels':['Coffin','Throwing up','Sweat sad face','Shrug','Drool','Head exploding'],
                                   'colors' : {0:'slategrey', 1:'tomato', 2:'darkorange', 3:'gold', 4:'greenyellow', 5:'seagreen'}
                                   },
            'Sweetness': {'xlims':[1,3],
                          'xlabels':['Not sweet','Sweet','Super sweet'],
                          'colors' : {1:'tomato', 2:'gold', 3:'seagreen'}
                          },
            }


    a = pd.read_csv(f'../data/SS6_cookie{characteristic}.csv',index_col='cookie_descrip')

    del a['Cookie']

    colors = [opts[characteristic]['colors'][np.round(temp_mean)] for temp_mean in a.mean(axis=1)]
    fig,ax = plt.subplots(1,1,figsize=(12,8),num=characteristic)
    a.mean(axis=1).plot(kind='barh',xerr=a.std(axis=1),
                        title=characteristic,fig=fig,ax=ax,
                        color=colors)

    ax.set_xlim(0.5,opts[characteristic]['xlims'][1])
    ax.invert_yaxis()
    ax.set_ylabel('')

    lims = list(range(opts[characteristic]['xlims'][0],opts[characteristic]['xlims'][1]+1))
    ax.xaxis.set_major_locator(ticker.FixedLocator(lims))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(opts[characteristic]['xlabels']))
    plt.setp(ax.get_xticklabels(),rotation=45,ha="right")

    plt.tight_layout()
    plt.savefig(f'cookie{characteristic}.png')
    print(f'Saved: cookie{characteristic}.png')


def plot_all(choices):
    '''
    Cycles through all the available characteristics and makes a plot for each.
    '''

    for choice in choices:

        if choice is not 'all':

            plot_characteristic(choice)




if __name__ == "__main__":

    choices = ['all','Appearance','Bite','ChocolateFlavor','Moistness','PersonalPreference','Sweetness']

    parser = argparse.ArgumentParser(description="What's in a cookie?")
    parser.add_argument('--characteristic', '-c',
                        type = str,
                        default = None,
                        choices = choices,
                        help='Which plots to do you want to produce?')

    args = parser.parse_args()

    if not args.characteristic:
        raise ValueError(f'Please select a characteristic to plot: {choices}.')

    elif args.characteristic == 'all':

        plot_all(choices)

    else:

        a = plot_characteristic(args.characteristic)
