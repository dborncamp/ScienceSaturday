import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

matplotlib.style.use('bmh')

def read_tables():

    #Reading in cheese results and creating pandas dataframe
    f1  = pd.read_excel('SS4_pizza_tables.xlsx',
                        sheet_name='Cheese Results',
                        header=0,
                        usecols='C:K'
                        )

    pizzas = ['Pappa John\'s','Pizza Boli\'s','Digiorno','Little Caesar\'s','Dominos','Pizza Hut','Pizza Hut Stuffed Crust']
    categories = ['Sauce','Cheese','Greasiness','Crust','Overall','Chain Guess']
    arrays = [list(np.repeat(pizzas,6)),categories*7]
    tuples = list(zip(*arrays))
    mux = pd.MultiIndex.from_tuples(tuples, names = ['Brand','category'])

    tab1 = pd.DataFrame(f1.values,index=mux,columns=f1.columns.values)

    #Reading in pepperoni results and creating pandas dataframe
    f2  = pd.read_excel('SS4_pizza_tables.xlsx',
                         sheet_name='Pepperoni Results',
                         header=0,
                         usecols='C:L'
                         )

    pizzas = ['Digiorno','Pizza Hut','Dominos','Pizza Boli\'s','Pappa John\'s','Little Caesar\'s',]
    categories = ['Sauce','Cheese','Topping','Greasiness','Crust','Overall','Chain Guess']
    arrays = [list(np.repeat(pizzas,7)),categories*6]
    tuples = list(zip(*arrays))
    mux = pd.MultiIndex.from_tuples(tuples, names = ['Brand','category'])

    tab2 = pd.DataFrame(f2.values,index=mux,columns=f2.columns.values)

    tab3 = pd.read_excel('SS4_pizza_tables.xlsx',
                         sheet_name='Cheese temperatures',
                         header=1
                         )

    tab4 = pd.read_excel('SS4_pizza_tables.xlsx',
                         sheet_name='Pepperoni temperatures',
                         header=1
                         )
    return tab1,tab2,tab3,tab4
    return tab1,tab2

def cheese_overall_results(tab1):

    scores = tab1.xs('Overall',level='category').mean(axis=1)
    scores = scores.sort_values()
    errs = tab1.xs('Overall',level='category').std(axis=1)
    
    plt.figure(num='cheeseoverall',figsize=(12,5))
    scores.plot(kind='bar',
                ylim=[0,5.1],
                yerr=errs,
                color='dodgerblue',
                rot=45.,
                title='Cheese pizza overall scores'
                )
       
    plt.savefig('SS4_cheese_overall_scores.png',bbox_inches='tight')
    print('Cheese results saved')

def pepperoni_overall_results(tab2):

    scores = tab2.xs('Overall',level='category').mean(axis=1)
    scores = scores.sort_values()
    errs = tab2.xs('Overall',level='category').std(axis=1)

    plt.figure(num='pepoverall',figsize=(12,5))
    scores.plot(kind='bar',
                ylim=[0,5.1],
                yerr=errs,
                color='dodgerblue',
                rot=45.,
                title='Pepperoni pizza overall scores'
                )

    plt.savefig('SS4_pepperoni_overall_scores.png',bbox_inches='tight')
    print('Pepperoni results saved')

def check_temps(tab1,tab2,tab3,tab4):

    cheese_scores = tab1.xs('Overall',level='category').mean(axis=1)
    cheese_errs = tab1.xs('Overall',level='category').std(axis=1)

    pep_scores = tab2.xs('Overall',level='category').mean(axis=1)
    pep_errs = tab2.xs('Overall',level='category').std(axis=1)

    plt.figure(num='cheesevstemp',figsize=(12,5))
    plt.scatter(tab3['Temp (deg F)'],cheese_scores,
                marker='s',s=25,c='k'
                )
    plt.errorbar(tab3['Temp (deg F)'],cheese_scores,
                 yerr=cheese_errs,fmt='none',
                 c='k',elinewidth=0.5)
    plt.ylim(0,5.1)
    plt.xlabel('Temperature (deg F)',fontsize='large')
    plt.ylabel('Overall score',fontsize='large')
    plt.suptitle('Cheese scores vs temperature',fontsize='x-large')
    plt.savefig('cheese_vs_temp.png',bbox_inches='tight')

    plt.figure(num='pepvstemp',figsize=(12,5))
    plt.scatter(tab4['Temp (deg F)'],pep_scores,
                marker='s',s=25,c='k'
                )
    plt.errorbar(tab4['Temp (deg F)'],pep_scores,
                 yerr=pep_errs,fmt='none',
                 c='k',elinewidth=0.5)
    plt.ylim(0,5.1)
    plt.xlabel('Temperature (deg F)',fontsize='large')
    plt.ylabel('Overall score',fontsize='large')
    plt.suptitle('Pepperoni scores vs temperature',fontsize='x-large')
    plt.savefig('pep_vs_temp.png',bbox_inches='tight')

    print('Temperature checks plotted')
    
def main():

    cheese_tab,pep_tab,cheese_temp,pep_temp = read_tables()

    cheese_overall_results(cheese_tab)
    pepperoni_overall_results(pep_tab)
    check_temps(cheese_tab,pep_tab,cheese_temp,pep_temp)

if __name__ == "__main__":

    main()
