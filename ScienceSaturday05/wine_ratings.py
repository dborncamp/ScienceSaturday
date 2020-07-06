'''
Code to see what scores we gave the wines.
'''
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

def wine_score(wine,temp_tab):

    wine_info = winetab[winetab['wine_name']==wine]

    if wine_info['group'].values==1:
        data = g1
    elif wine_info['group'].values==2:
        data = g2
    else:
        print('WTF?')

    idx1 = (data['wine1_number']==wine_info['wine_number'].values[0])&(data['wine1_correct']==True)
    idx2 = (data['wine2_number']==wine_info['wine_number'].values[0])&(data['wine2_correct']==True)

    scores = pd.concat([data['wine1_rating'][idx1],data['wine2_rating'][idx2]],
                        ignore_index=True)

    return temp_tab.append({'Wine':wine_info['wine_name'].values[0],
                            'Type':wine_info['wine_type'].values[0],
                            'Color':wine_info['wine_color'].values[0],
                            'Rating':scores.mean(),
                            'STD':scores.std(),
                            'Price':wine_info['price'].values[0]},
                            ignore_index=True
                           )


#Reading in data and creating output table.
winetab = pd.read_csv('../data/SS5_WineInfo.csv')
g1 = pd.read_csv('../data/SS5_redvsWhiteGroup1.csv')
g2 = pd.read_csv('../data/SS5_redvsWhiteGroup2.csv')
tab = pd.concat([g1,g2],ignore_index=True)

results_tab = pd.DataFrame(columns=['Wine','Type','Color','Rating','STD','Price'],
                           index=None
                           )

for wine in winetab['wine_name']:

    results_tab = wine_score(wine,results_tab)

plt.errorbar(results_tab['Price'][results_tab['Color']=='Red'],
             results_tab['Rating'][results_tab['Color']=='Red'],
             yerr=results_tab['STD'][results_tab['Color']=='Red'],
             fmt='s',ms=5,color='darkred',label='Red'
             )
plt.errorbar(results_tab['Price'][results_tab['Color']=='White'],
             results_tab['Rating'][results_tab['Color']=='White'],
             yerr=results_tab['STD'][results_tab['Color']=='White'],
             fmt='s',ms=5,color='khaki',label='White'
             )
plt.errorbar(results_tab['Price'][results_tab['Color']=='Rose'],
             results_tab['Rating'][results_tab['Color']=='Rose'],
             yerr=results_tab['STD'][results_tab['Color']=='Rose'],
             fmt='s',ms=5,color='pink',label='Rose'
             )

plt.ylim(0,5)
plt.legend()
plt.xlabel('Price [$]',fontsize='large')
plt.ylabel('Rating',fontsize='large')
plt.suptitle('Cold wines ratings',fontsize='x-large')

plt.savefig('wine_scores.png',bbox_inches='tight')
