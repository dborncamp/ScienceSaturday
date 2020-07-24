'''
Extracting Starburst data from google spreadsheet. 
raw_data.xlsx is the spreadsheet downloaded from Google.
'''
import pandas as pd

def clean_data(guesser,cols,rows):

    a = pd.read_excel('raw_data.xlsx',
                      sheet_name=guesser,
                      header=None,
                      names=['truth','guess','correct'],
                      skiprows=list(range(6)),
                      usecols=cols,
                      nrows=rows
                      )

    a['truth'] = a['truth'].str.lower()
    a['guess'] = a['guess'].str.lower()

    a['guesser'] = [guesser]*rows

    return a[['guesser','truth','guess','correct']]


df_list = []
guessers = ['Rachel','Roberto','Heather','MattB','Keira','Elaine','Chris','Jeff']
cols = ['F:H','F:H','F:H','G:I','G:I','F:H','F:H','F:H']
rows = [15,15,16,15,15,15,15,15]

for i,guesser in enumerate(guessers):

    df_list.append(clean_data(guesser,cols=cols[i],rows=rows[i]))

tab = pd.concat(df_list,ignore_index=True)

tab.to_csv('../data/SS7_starburst.csv')
