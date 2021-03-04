import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

data = pd.read_csv( r'0-Downloaded_files/arms_trade.csv', encoding = 'unicode_escape', engine='python' )
#DROPS LAST ROW, ITS UNNECSSARY BECASUE THEY ARE SUMS
data.drop( data.tail( 1 ).index, inplace=True )
#data.fillna(value=0, axis=1, inplace=True, downcast='infer') IF IT IS ADD IF GIVES MORE ERRORS ON ONE YEAR CHOICE

print(data)

