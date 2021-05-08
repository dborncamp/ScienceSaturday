import pandas as pd
import matplotlib.pyplot as plt


def get_data():

    tab = pd.read_csv('SS9_Results.csv',index_col=[0,1])
    cat = pd.read_csv('SS9_BeerCatalog.csv',index_col=0)


    #Set the right data types of results table
    tab.loc[(slice(None),'Rating'),:] = tab.loc[(slice(None),'Rating'),:].astype(float)
    tab.loc[(slice(None),'Number'),:] = tab.loc[(slice(None),'Number'),:].astype(float)

    return tab,cat

