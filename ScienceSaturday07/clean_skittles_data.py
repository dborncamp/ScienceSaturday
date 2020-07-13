'''
Extracting Skittles data from google spreadsheet. 
raw_data.xlsx is the spreadsheet downloaded from Google.
'''
import pandas as pd

def clean_data(guesser):

    a = pd.read_excel('raw_data.xlsx',sheet_name=guesser,
            header=None,
            names=['truth','guess','correct'],
            usecols='B:D',
            skiprows=list(range(6)),
            nrows=15
            )

    a['truth'] = a['truth'].str.lower()
    a['guess'] = a['guess'].str.lower()

    a['guesser'] = [guesser]*15

    return a[['guesser','truth','guess','correct']]


df_list = []
guessers = ['Rachel','Roberto','Jo','Heather','Tyler','Jenna','MattB','Keira','Elaine','Chris','Dave','Megan']

for guesser in guessers:

    df_list.append(clean_data(guesser))

tab = pd.concat(df_list,ignore_index=True)

tab.to_csv('../data/SS7_skittles.csv')
