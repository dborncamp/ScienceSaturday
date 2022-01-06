import pandas as pd
from tabulate import tabulate

def make_table(filename):

    tab = pd.read_csv(f'../data/SS10_{filename.lower()}.csv',index_col=[0,1])

    a = tab.groupby(['person',filename],sort=False).mean().unstack()

    with open(f'SS10_{filename}_table.txt','w') as f1:

        print(tabulate(a,
                       tablefmt='github',
                       floatfmt='3.2f',
                       headers=list(zip(*a.columns))[1]
                       ),
              file=f1
             )

    return tab

if __name__ == "__main__":

    capn = make_table('capncrunch')
    #capnberries = make_table('capncrunchberries')
    chip = make_table('chip')
    cola = make_table('cola')
    cookie = make_table('cookie')
    drpepper = make_table('drpepper')
    icecream = make_table('icecream')
    life = make_table('life')
    #rumncoke = make_table('rumncoke')
    sourcream = make_table('sourcream')
