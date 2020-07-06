'''
Code to figure out percentage of correct guesses.
'''
import pandas as pd
from tabulate import tabulate

def wine_color_guessed(input_tab,color):

    idx1 = g1['wine1_color']==color
    idx2 = g1['wine2_color']==color
    g1_correct = g1['wine1_correct'][idx1].sum()+g1['wine2_correct'][idx2].sum()
    g1_count = g1['wine1_correct'][idx1].count()+g1['wine2_correct'][idx2].count()

    idx1 = g2['wine1_color']==color
    idx2 = g2['wine2_color']==color
    g2_correct = g2['wine1_correct'][idx1].sum()+g2['wine2_correct'][idx2].sum()
    g2_count = g2['wine1_correct'][idx1].count()+g2['wine2_correct'][idx2].count()

    return input_tab.append({'Test':f'{color} wine',
                             'Group 1':g1_correct/g1_count,
                             'Group 2':g2_correct/g2_count,
                             'Everyone':(g1_correct+g2_correct)/(g1_count+g2_count)},
                             ignore_index=True)


#Reading in data and creating output table.
winetab = pd.read_csv('../data/SS5_WineInfo.csv')
g1 = pd.read_csv('../data/SS5_redvsWhiteGroup1.csv')
g2 = pd.read_csv('../data/SS5_redvsWhiteGroup2.csv')
tab = pd.concat([g1,g2],ignore_index=True)

results_tab = pd.DataFrame(columns=['Test','Group 1','Group 2','Everyone'],
                           index=None,
                           )
results_tab.style.format({'Group 1':'{.2f}',
                          'Group 2':'{.2f}',
                          'Everyone':'{.2f}'
                         })


#Figuring out overall results
g1_correct = g1['wine1_correct'].sum()+g1['wine2_correct'].sum()
g1_count =   g1['wine1_correct'].count()+g1['wine2_correct'].count()
    
g2_correct = g2['wine1_correct'].sum()+g2['wine2_correct'].sum()
g2_count =   g2['wine1_correct'].count()+g2['wine2_correct'].count()

results_tab = results_tab.append({'Test':'Overall',
                                  'Group 1':g1_correct/g1_count,
                                  'Group 2':g2_correct/g2_count,
                                  'Everyone':(g1_correct+g2_correct)/(g1_count+g2_count)},
                                 ignore_index=True)

#Figuring out results by color.
results_tab = wine_color_guessed(results_tab,'Red')
results_tab = wine_color_guessed(results_tab,'White')
results_tab = wine_color_guessed(results_tab,'Rose')

with open('guess_results.txt','w') as f1:

    f1.write(tabulate(results_tab,
                      headers=results_tab.columns,
                      showindex=False,
                      tablefmt='github')
            )
