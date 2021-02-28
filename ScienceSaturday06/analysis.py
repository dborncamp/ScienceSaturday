'''
Code to do analysis of Cookies data.
'''

#Global
import pandas as pd
import matplotlib.pyplot as plt
import argparse

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

    a = pd.read_csv(f'../data/SS6_cookie{characteristic}.csv',index_col='cookie_descrip')

    del a['Cookie']

    fig,ax = plt.subplots(1,1,figsize=(12,8),num=characteristic)

    a.mean(axis=1).plot(kind='barh',xerr=a.std(axis=1),
                        title=characteristic,fig=fig,ax=ax)

    ax.invert_yaxis()

    ax.set_xlim(0,5)
    plt.tight_layout()

    return a

def plot_all(choices):

    for choice in choices:

        if choice is not 'all':

            plot_characteristic(choice)




if __name__ == "__main__":

    choices = ['all','Appearance','Bite','ChocolateFlavor','Moistness','PersonalPreference','Sweetness']

    parser = argparse.ArgumentParser(description="What's in a cookie?")
    parser.add_argument('--characteristic',
                        type = str,
                        default = None,
                        choices = choices,
                        help='Which plots to do you want to produce?')

    args = parser.parse_args()

    if args.characteristic== 'all':

        plot_all(choices)

    else:

        a = plot_characteristic(args.characteristic)

