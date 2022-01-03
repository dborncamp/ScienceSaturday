import pandas as pd
import matplotlib.pyplot as plt

plt.xkcd()


def make_fig(filename,label):

    tab = pd.read_csv(f'../data/SS10_{filename.lower()}.csv',index_col=[0,1])

    fig1,ax = plt.subplots(1,1,figsize=(10,10))

    erry = tab.groupby(filename).std()
    tab.groupby(filename).mean().plot(kind='bar',
                                    ax=ax,
                                    yerr=erry)
    ax.set_xlabel(label,fontsize='large')
    ax.set_ylim(0,5)

    fig1.tight_layout()
    fig1.savefig(f'{filename.lower()}.png',dpi=300)
    plt.close(fig1)


if __name__ == "__main__":

    make_fig('capncrunch',label='Cap n Crunch')
    #make_fig('capncrunchberries',label='Cap n Crunch Berries')
    make_fig('chip',label='Potato chips')
    make_fig('cola',label='Cola')
    make_fig('cookie',label='Oreos')
    make_fig('drpepper',label='Dr. Pepper')
    make_fig('icecream',label='Ice cream')
    make_fig('life',label='Life cereal')
    #make_fig('rumncoke',label='Rum and Coke')
    make_fig('sourcream',label='Sour cream')
