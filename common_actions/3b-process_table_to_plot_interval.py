import pandas as pd

# SELECTS THE COLUMNS TO SUM
dataset = pd.read_csv( r''+str(file_name)+'', index_col= 0)
dataset['sum_col'] = dataset.loc[:, selected_years].sum(axis = 1)
print(dataset)