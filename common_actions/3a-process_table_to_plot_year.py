import pandas as pd

table_to_read = pd.read_csv( r''+str(file_name)+'', sep=',')
top_values = table_to_read.nlargest(20, str(year_input))