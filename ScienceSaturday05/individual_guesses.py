'''
Code to see how individuals did in their guesses. 
'''
import pandas as pd
from tabulate import tabulate

def person_results(name,temp_table):

    ind_tab = tab[tab['guesser']==name]

    red_correct,red_count = color_results('Red',ind_tab)
    white_correct,white_count = color_results('White',ind_tab)
    rose_correct,rose_count = color_results('Rose',ind_tab)
    all_correct = red_correct + white_correct + rose_correct
    all_count = red_count + white_count + rose_count

    return temp_table.append({'Name':name,
                              'Red':red_correct/red_count,
                              'White':white_correct/white_count,
                              'Rose':rose_correct/rose_count,
                              'Overall':all_correct/all_count},
                              ignore_index=True)


def color_results(color,ind_tab):

    color_correct = ind_tab['wine1_correct'][ind_tab['wine1_color']==color].sum()+\
                    ind_tab['wine2_correct'][ind_tab['wine2_color']==color].sum()
    color_count = ind_tab['wine1_correct'][ind_tab['wine1_color']==color].count()+\
                  ind_tab['wine2_correct'][ind_tab['wine2_color']==color].count()
    
    return color_correct,color_count



#Reading in data and creating output table.
winetab = pd.read_csv('../data/SS5_WineInfo.csv')
g1 = pd.read_csv('../data/SS5_redvsWhiteGroup1.csv')
g2 = pd.read_csv('../data/SS5_redvsWhiteGroup2.csv')
tab = pd.concat([g1,g2],ignore_index=True)

results_tab = pd.DataFrame(columns=['Name','Red','White','Rose','Overall'],
                           index=None,
                           )


for name in set(tab['guesser']):

    results_tab = person_results(name,results_tab)

results_tab.sort_values('Overall',ascending=False,inplace=True)

with open('person_results.txt','w') as f1:

    f1.write(tabulate(results_tab,
                      headers=results_tab.columns,
                      showindex=False,
                      tablefmt='github')
            )

