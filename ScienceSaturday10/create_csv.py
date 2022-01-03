import pandas as pd
import itertools

names=['Rachel','Matt D.','Jo','Roberto','Jenna','Tyler','Keira','Matt B.']

def make_csv(skiprows,nrows,colname):

    rawtab = pd.read_excel('../data/all_results.xlsx',
                           sheet_name='Generic vs. name brand',
                           names=names,
                           skiprows=skiprows,
                           nrows=nrows,
                           usecols='B:I'
                           )

    idx = pd.MultiIndex.from_product([names,range(1,int(nrows/4)+1)],names=['person','round'])

    outtab = pd.DataFrame(index=idx,columns=[colname,'score','guess/comment'])

    item = list(itertools.chain(*[rawtab[2::4][i].to_list() for i in rawtab.columns]))
    score = list(itertools.chain(*[rawtab[1::4][i].to_list() for i in rawtab.columns]))
    guess = list(itertools.chain(*[rawtab[3::4][i].to_list() for i in rawtab.columns]))

    outtab[colname] = item
    outtab['score'] = score
    outtab['guess/comment'] = guess

    outtab.to_csv(f'../data/SS10_{colname}.csv')

    return outtab

if __name__ == "__main__":

    chip = make_csv(1,36,'chip')
    cookie = make_csv(38,16,'cookie')
    drpepper = make_csv(55,16,'drpepper')
    cola = make_csv(72,16,'cola')
    capncrunch = make_csv(89,16,'capncrunch')
    life = make_csv(106,16,'life')
    sourcream = make_csv(123,24,'sourcream')
    icecream = make_csv(148,16,'icecream')
    rumncoke = make_csv(165,24,'rumncoke')
    capncrunchberries = make_csv(190,16,'capncrunchberries')
